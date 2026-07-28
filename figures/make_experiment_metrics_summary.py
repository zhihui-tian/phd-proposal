"""Re-layout the experimental metrics panels without altering plotted data.

The source montage contains four manuscript figures at inconsistent scales.
This script crops only existing pixels, rescales each plot uniformly, and
reassembles the panels on a compact three-row publication layout.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "experiment_metrics_summary.png"
OUTPUT = ROOT / "experiment_metrics_summary_relayout.png"

CANVAS_W = 2400
CANVAS_H = 2380
PAGE_MARGIN = 55
TITLE_SIZE = 42
SUBTITLE_SIZE = 29
INK = "#111111"
RULE = "#D0D5D8"

# Pixel boxes in the original 2664 x 1544 montage. Each box retains the
# complete plot frame, axes, legends, and annotations available in the source.
CROPS = {
    "a_radius": (0, 158, 650, 662),
    "a_count": (660, 158, 1310, 662),
    "b_t1": (1355, 80, 1988, 705),
    "b_t2": (2005, 80, 2635, 705),
    "c_faces": (220, 850, 1125, 1535),
    "d_train": (1405, 840, 1970, 1544),
    "d_holdout": (1985, 840, 2645, 1544),
}


def load_font(size, bold=False):
    candidates = [
        Path(
            "/System/Library/Fonts/Supplemental/"
            + ("Arial Bold.ttf" if bold else "Arial.ttf")
        ),
        Path(
            "/usr/share/fonts/truetype/dejavu/"
            + ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")
        ),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def contain(image, max_width, max_height):
    scale = min(max_width / image.width, max_height / image.height)
    size = (
        max(1, round(image.width * scale)),
        max(1, round(image.height * scale)),
    )
    return image.resize(size, Image.Resampling.LANCZOS)


def paste_centered(canvas, image, box):
    left, top, right, bottom = box
    x = left + (right - left - image.width) // 2
    y = top + (bottom - top - image.height) // 2
    canvas.paste(image, (x, y))


def draw_title(draw, x, y, label, title, title_font):
    draw.text((x, y), f"({label})", font=title_font, fill=INK)
    label_width = draw.textlength(f"({label})", font=title_font)
    draw.text((x + label_width + 16, y), title, font=title_font, fill=INK)


def draw_rotated_label(canvas, text, center_x, center_y, font):
    bbox = font.getbbox(text)
    label = Image.new(
        "RGBA",
        (bbox[2] - bbox[0] + 20, bbox[3] - bbox[1] + 20),
        (255, 255, 255, 0),
    )
    draw = ImageDraw.Draw(label)
    draw.text((10 - bbox[0], 10 - bbox[1]), text, font=font, fill=INK)
    rotated = label.rotate(90, expand=True, resample=Image.Resampling.BICUBIC)
    canvas.paste(
        rotated,
        (round(center_x - rotated.width / 2), round(center_y - rotated.height / 2)),
        rotated,
    )


def build():
    source = Image.open(SOURCE).convert("RGB")
    panels = {name: source.crop(box) for name, box in CROPS.items()}

    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), "white")
    draw = ImageDraw.Draw(canvas)
    title_font = load_font(TITLE_SIZE, bold=False)
    axis_font = load_font(SUBTITLE_SIZE, bold=False)

    # Row 1: aggregate coarsening metrics.
    row1_top = 35
    draw_title(
        draw,
        PAGE_MARGIN,
        row1_top,
        "a",
        "Coarsening trajectory",
        title_font,
    )
    a_radius = contain(panels["a_radius"], 840, 590)
    a_count = contain(panels["a_count"], 860, 590)
    row1_plot_top = row1_top + 65
    paste_centered(canvas, a_radius, (235, row1_plot_top, 1100, 690))
    paste_centered(canvas, a_count, (1130, row1_plot_top, 2195, 690))

    draw.line(
        (PAGE_MARGIN, 720, CANVAS_W - PAGE_MARGIN, 720),
        fill=RULE,
        width=2,
    )

    # Row 2: paired distribution comparisons.
    row2_top = 750
    draw_title(
        draw,
        PAGE_MARGIN,
        row2_top,
        "b",
        "Normalized grain-size distributions",
        title_font,
    )
    b_t1 = contain(panels["b_t1"], 900, 720)
    b_t2 = contain(panels["b_t2"], 900, 720)
    row2_plot_top = row2_top + 60
    paste_centered(canvas, b_t1, (200, row2_plot_top, 1170, 1510))
    paste_centered(canvas, b_t2, (1230, row2_plot_top, 2200, 1510))

    draw.line(
        (PAGE_MARGIN, 1550, CANVAS_W - PAGE_MARGIN, 1550),
        fill=RULE,
        width=2,
    )

    # Row 3: topology and individual-grain fidelity.
    row3_top = 1580
    draw_title(
        draw,
        PAGE_MARGIN,
        row3_top,
        "c",
        "Faces per grain",
        title_font,
    )
    draw_title(
        draw,
        960,
        row3_top,
        "d",
        "Grain-by-grain volume change",
        title_font,
    )

    c_faces = contain(panels["c_faces"], 760, 650)
    d_train = contain(panels["d_train"], 635, 650)
    d_holdout = contain(panels["d_holdout"], 635, 650)
    row3_plot_top = row3_top + 65

    paste_centered(canvas, c_faces, (120, row3_plot_top, 900, 2320))
    paste_centered(canvas, d_train, (955, row3_plot_top, 1645, 2320))
    paste_centered(canvas, d_holdout, (1680, row3_plot_top, 2370, 2320))

    # The source montage clipped these two shared y-axis labels. Restoring the
    # labels improves readability without inferring or changing numeric values.
    draw_rotated_label(
        canvas,
        "mean faces per grain",
        82,
        (row3_plot_top + 2320) / 2,
        axis_font,
    )
    draw_rotated_label(
        canvas,
        "predicted \u0394V (voxels)",
        925,
        (row3_plot_top + 2320) / 2,
        axis_font,
    )

    canvas.save(OUTPUT, dpi=(300, 300), optimize=True)


if __name__ == "__main__":
    build()
