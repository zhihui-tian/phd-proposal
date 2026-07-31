"""Aim 1 support figure: what the single reconstructed volume can actually carry.

Every number is taken from the experimental manuscript, Section 2:
  reconstruction 549 x 149 x 211 voxels, 5 um voxel;
  curated analysis window trimmed in place to 100 x 95 x 84 voxels;
  five states T0-T4 at cumulative holds of 8, 10, 12, 14, 16 h (uniform 2 h).

The slot count is arithmetic on those dimensions, not a claim from the
manuscript: it is a geometric upper bound on non-overlapping windows, drawn so
that the committee can see the support rather than be told about it. How many
slots survive curation is the first question Aim 1 answers.

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


def dashed_rect(d, box, colour, width, dash=18, gap=12):
    x0, y0, x1, y1 = box
    for (ax, ay, bx, by) in ((x0, y0, x1, y0), (x1, y0, x1, y1),
                             (x1, y1, x0, y1), (x0, y1, x0, y0)):
        span = max(abs(bx - ax), abs(by - ay))
        if not span:
            continue
        ux, uy = (bx - ax) / span, (by - ay) / span
        t = 0
        while t < span:
            e = min(t + dash, span)
            d.line([ax + ux * t, ay + uy * t, ax + ux * e, ay + uy * e],
                   fill=colour, width=width)
            t = e + gap


def main():
    img = Image.new("RGB", (W * S, H * S), WHITE)
    d = ImageDraw.Draw(img)

    # ---------------------------------------------------------- panel A
    d.text((60 * S, 40 * S), "SPATIAL SUPPORT", font=f(26, True), fill=MUTED)
    d.text((60 * S, 84 * S),
           f"x–z face of the reconstruction, {NX} × {NZ} voxels",
           font=f(30), fill=INK)

    ax0, ay0 = 60 * S, 160 * S
    scale = (1300 * S) / NX
    aw, ah = NX * scale, NZ * scale
    d.rectangle([ax0, ay0, ax0 + aw, ay0 + ah], fill=SHELL, outline=LINE, width=2 * S)

    ncols, nrows = NX // WX, NZ // WZ
    sw, sh = WX * scale, WZ * scale
    for r in range(nrows):
        for c in range(ncols):
            x0 = ax0 + c * sw
            y0 = ay0 + r * sh
            box = [x0 + 3 * S, y0 + 3 * S, x0 + sw - 3 * S, y0 + sh - 3 * S]
            if r == 0 and c == 0:                       # the window actually used
                d.rectangle(box, fill=BLUE)
                d.text((x0 + sw / 2, y0 + sh / 2 - 26 * S), "CURRENT",
                       font=f(21, True), fill=WHITE, anchor="mm")
                d.text((x0 + sw / 2, y0 + sh / 2 + 8 * S), "100×95×84",
                       font=f(19), fill=WHITE, anchor="mm")
            else:
                d.rectangle(box, fill=SOFT)
                dashed_rect(d, box, BLUE, 2 * S)
                d.text((x0 + sw / 2, y0 + sh / 2), "slot",
                       font=f(19), fill=MUTED, anchor="mm")

    d.text((ax0 + aw - 14 * S, ay0 + ah - 14 * S), "remainder < one window",
           font=f(19), fill=MUTED, anchor="rs")
    d.text((ax0, ay0 + ah + 22 * S),
           f"{ncols} × {nrows} = {ncols * nrows} non-overlapping slots"
           f"    ·    y = {NY} voxels admits one {WY}-voxel window",
           font=f(24), fill=INK)
    d.text((ax0, ay0 + ah + 60 * S),
           "geometric upper bound — the selected window ranked 15 of 831 "
           "candidate placements",
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

    bracket(xs[0], xs[1], ty + 110 * S, "trained", True)
    bracket(xs[2], xs[4], ty + 110 * S, "held out", False)
    d.text((bx, ty + 210 * S),
           "one field of view · one training interval",
           font=f(24), fill=INK)
    d.text((bx, ty + 248 * S),
           "extending beyond it is Aim 1",
           font=f(22), fill=MUTED)

    img.resize((W, H), Image.LANCZOS).save(OUT)
    print(f"wrote {OUT}  ({ncols * nrows} slots)")


if __name__ == "__main__":
    main()
