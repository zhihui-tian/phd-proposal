"""Aim 1 support figure: single-window selection and temporal use.

Every number is taken from the experimental manuscript, Section 2:
  reconstruction 549 x 149 x 211 voxels, 5 um voxel;
  curated analysis window trimmed in place to 100 x 95 x 84 voxels;
  five states T0-T4 at cumulative holds of 8, 10, 12, 14, 16 h (uniform 2 h).

The left panel documents the actual one-window workflow rather than a
multi-window packing bound. The right panel distinguishes held out from fitting
from an unexamined confirmatory test.

Categories are separated by fill, outline style, and label -- never by hue
alone -- so the figure survives colour-vision deficiency, greyscale printing,
and projector colour shift.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "aim1_support.png"

# deck palette (figures/make_specific_aims_overview.py)
INK = (29, 45, 57)
MUTED = (89, 106, 118)
LINE = (200, 208, 213)
BLUE = (71, 119, 144)
SOFT = (238, 244, 247)
SHELL = (246, 248, 249)
WHITE = (255, 255, 255)

# dataset facts
NX, NY, NZ = 549, 149, 211
WX, WY, WZ = 100, 95, 84
HOLDS = [8, 10, 12, 14, 16]

S = 3                                   # supersample factor
W, H = 2600, 830
FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_B = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def f(sz, bold=False):
    return ImageFont.truetype(FONT_B if bold else FONT, sz * S)


def main():
    img = Image.new("RGB", (W * S, H * S), WHITE)
    d = ImageDraw.Draw(img)

    # ---------------------------------------------------------- panel A
    d.text((60 * S, 40 * S), "SINGLE-WINDOW SELECTION", font=f(26, True), fill=MUTED)
    d.text((60 * S, 84 * S), "one field of view selected, curated, and trained",
           font=f(30), fill=INK)

    steps = (
        ("FULL VOLUME", f"{NX}×{NY}×{NZ}", "five registered states"),
        ("CANDIDATES", "831 windows", "100³ before trimming"),
        ("RANKING", "residual driven", "residual + displacement gradient"),
        ("SELECTED + CURATED", "rank 15 → 100×95×84", "integer registration + linkage"),
    )
    x0, y0 = 60 * S, 205 * S
    bw, bh, gap = 285 * S, 205 * S, 55 * S
    for i, (title, value, note) in enumerate(steps):
        left = x0 + i * (bw + gap)
        box = [left, y0, left + bw, y0 + bh]
        final = i == len(steps) - 1
        d.rounded_rectangle(box, radius=14 * S, fill=BLUE if final else SOFT,
                            outline=BLUE if final else LINE, width=3 * S)
        d.text((left + bw / 2, y0 + 54 * S), title, font=f(20, True),
               fill=WHITE if final else MUTED, anchor="mm")
        d.text((left + bw / 2, y0 + 105 * S), value, font=f(27, True),
               fill=WHITE if final else INK, anchor="mm")
        d.text((left + bw / 2, y0 + 157 * S), note, font=f(17),
               fill=WHITE if final else MUTED, anchor="mm")
        if not final:
            ax = left + bw + 10 * S
            bx = left + bw + gap - 10 * S
            ay = y0 + bh / 2
            d.line([ax, ay, bx, ay], fill=BLUE, width=3 * S)
            d.polygon([(bx, ay), (bx - 12 * S, ay - 8 * S),
                       (bx - 12 * S, ay + 8 * S)], fill=BLUE)

    d.text((60 * S, 470 * S),
           "pending documentation: candidate stride · exact objective · rank-15 decision",
           font=f(22), fill=MUTED)

    # ---------------------------------------------------------- panel B
    bx = 1470 * S
    d.text((bx, 40 * S), "TEMPORAL SUPPORT", font=f(26, True), fill=MUTED)
    d.text((bx, 84 * S), "five states, four intervals of 2 h",
           font=f(30), fill=INK)

    tx0, tx1 = bx, (W - 90) * S
    ty = 292 * S
    d.line([tx0, ty, tx1, ty], fill=LINE, width=3 * S)
    xs = [tx0 + (tx1 - tx0) * i / (len(HOLDS) - 1) for i in range(len(HOLDS))]
    for i, (x, h) in enumerate(zip(xs, HOLDS)):
        used = i <= 1
        r = 13 * S
        d.ellipse([x - r, ty - r, x + r, ty + r],
                  fill=BLUE if used else WHITE, outline=BLUE, width=3 * S)
        d.text((x, ty - 44 * S), f"T{i}", font=f(25, True), fill=INK, anchor="mm")
        d.text((x, ty + 44 * S), f"{h} h", font=f(21), fill=MUTED, anchor="mm")

    def bracket(x_a, x_b, y, label, solid):
        d.line([x_a, y, x_b, y], fill=BLUE if solid else MUTED, width=3 * S)
        for x in (x_a, x_b):
            d.line([x, y - 10 * S, x, y + 10 * S],
                   fill=BLUE if solid else MUTED, width=3 * S)
        d.text(((x_a + x_b) / 2, y + 34 * S), label, font=f(22, True),
               fill=BLUE if solid else MUTED, anchor="mm")

    bracket(xs[0], xs[1], ty + 110 * S, "Aim 1: trained", True)
    bracket(xs[2], xs[4], ty + 110 * S, "Aim 2: held out from fitting", False)
    d.text((bx, ty + 210 * S),
           "same field of view · later states already examined",
           font=f(24), fill=INK)
    d.text((bx, ty + 248 * S),
           "retrospective temporal evaluation, not a new blind test",
           font=f(22), fill=MUTED)

    img.resize((W, H), Image.LANCZOS).save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
