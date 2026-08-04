"""Extract the experimental-metric figures from the manuscript PDF.

The proposal formerly compressed seven axes into one raster montage.  These
page extracts preserve the manuscript's own artwork and allow each evidence
level to be shown at nearly full text width in the proposal.

Setting a crop box is not enough.  A crop box changes what a viewer displays,
not what the file contains, so an earlier version of this script shipped four
figures that each carried a whole manuscript page: its caption, its running
text, and its page number.  None of that was visible, but it survived into the
compiled proposal, where a text search or a screen reader still found it.

Each of these manuscript pages happens to have a clean structure: the figure is
a single image XObject invoked once, and every piece of text on the page sits
in one BT ... ET block.  So the page content stream is rewritten with that block
removed and the page-level font resources dropped.  What remains draws the
figure and nothing else.  Run verify() to confirm that on the written files.
"""

import re
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import DecodedStreamObject, NameObject


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "Letter_draft__superset____Scripta_Materialia_target.pdf"

TEXT_BLOCK = re.compile(rb"BT\b.*?\bET\b", re.S)

# Coordinates are PDF points measured from the lower-left corner of the page.
CROPS = {
    "experiment_metric_coarsening.pdf": (11, (108, 518, 502, 668)),
    "experiment_metric_size_distribution.pdf": (12, (109, 362, 501, 545)),
    "experiment_metric_topology.pdf": (13, (158, 432, 452, 627)),
    "experiment_metric_grain_response.pdf": (14, (113, 336, 498, 535)),
}


def extract_figure(reader, page_number, box, output):
    # Set the boxes on the source page, where an inherited MediaBox can still
    # be resolved, before the page is copied into the writer.
    source = reader.pages[page_number - 1]
    source.mediabox.lower_left = (box[0], box[1])
    source.mediabox.upper_right = (box[2], box[3])
    source.cropbox.lower_left = (box[0], box[1])
    source.cropbox.upper_right = (box[2], box[3])

    writer = PdfWriter()
    writer.add_page(source)
    page = writer.pages[0]

    content = page.get_contents().get_data()
    kept = TEXT_BLOCK.sub(b"", content)
    if kept == content:
        raise RuntimeError(f"no text block found on page {page_number}")

    stream = DecodedStreamObject()
    stream.set_data(kept)
    page[NameObject("/Contents")] = writer._add_object(stream)

    resources = page.get("/Resources")
    if resources is not None:
        resources = resources.get_object()
        if "/Font" in resources:
            del resources[NameObject("/Font")]

    with output.open("wb") as stream_out:
        writer.write(stream_out)


def verify():
    """Every written figure must yield no extractable text and no font."""
    for filename in CROPS:
        page = PdfReader(ROOT / filename).pages[0]
        text = (page.extract_text() or "").strip()
        fonts = (page.get("/Resources") or {}).get("/Font")
        status = "ok" if not text and not fonts else "FAIL"
        print(f"  {status:4s} {filename}  text={len(text)} chars  fonts={bool(fonts)}")
        if status == "FAIL":
            raise SystemExit(f"{filename} still carries text or fonts")


def build():
    reader = PdfReader(SOURCE)
    for filename, (page_number, box) in CROPS.items():
        extract_figure(reader, page_number, box, ROOT / filename)
        print(f"wrote {filename}")
    verify()


if __name__ == "__main__":
    build()
