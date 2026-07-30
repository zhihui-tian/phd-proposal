"""Extract vector experimental-metric figures from the manuscript PDF.

The proposal formerly compressed seven axes into one raster montage.  These
page crops preserve the manuscript's vector artwork and allow each evidence
level to be shown at nearly full text width in the proposal.
"""

from pathlib import Path

from pypdf import PdfReader, PdfWriter


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "Letter_draft__superset____Scripta_Materialia_target.pdf"

# Coordinates are PDF points measured from the lower-left corner.  The crops
# retain the plotted artwork only; proposal captions are supplied in LaTeX.
CROPS = {
    "experiment_metric_coarsening.pdf": (11, (108, 518, 502, 668)),
    "experiment_metric_size_distribution.pdf": (12, (109, 362, 501, 545)),
    "experiment_metric_topology.pdf": (13, (158, 432, 452, 627)),
    "experiment_metric_grain_response.pdf": (14, (113, 336, 498, 535)),
}


def extract_page_crop(reader, page_number, box, output):
    page = reader.pages[page_number - 1]
    page.mediabox.lower_left = (box[0], box[1])
    page.mediabox.upper_right = (box[2], box[3])
    page.cropbox.lower_left = (box[0], box[1])
    page.cropbox.upper_right = (box[2], box[3])

    writer = PdfWriter()
    writer.add_page(page)
    with output.open("wb") as stream:
        writer.write(stream)


def build():
    reader = PdfReader(SOURCE)
    for filename, (page_number, box) in CROPS.items():
        extract_page_crop(reader, page_number, box, ROOT / filename)


if __name__ == "__main__":
    build()
