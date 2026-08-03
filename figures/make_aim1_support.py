"""Aim 1 support figure: single-window selection and temporal use.

Every number is taken from the experimental manuscript, Section 2:
  reconstruction 549 x 149 x 211 voxels, 5 um voxel;
  curated analysis window trimmed in place to 100 x 95 x 84 voxels;
  five states T0-T4 at cumulative holds of 8, 10, 12, 14, 16 h (uniform 2 h).

The upper panel documents the actual two-stage one-window workflow rather than
a multi-window packing bound. The lower panel distinguishes held out from
fitting from an unexamined confirmatory test.

Layout note: the two panels are stacked rather than placed side by side. The
figure is included at \textwidth = 6.5 in = 468 pt, so a design pixel renders
at 468/W pt. A side-by-side layout needs W of about 2600, which puts every
label below 5.5 pt against 12 pt body text. Stacking holds W near 1160, so the
smallest label renders near 7.7 pt. Secondary per-step detail that does not
survive that budget lives in the LaTeX caption instead.

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
WHITE = (255, 255, 255)

# dataset facts
NX, NY, NZ = 549, 149, 211
WX, WY, WZ = 100, 95, 84
HOLDS = [8, 10, 12, 14, 16]

S = 3                                   # supersample factor
W, H = 1160, 770                        # design units; see layout note above
FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_B = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

# design-unit font sizes; at W = 1160 one unit renders at 0.403 pt
F_EYEBROW, F_LEAD = 21, 25              # 8.5 pt, 10.1 pt
F_BOX_TITLE, F_BOX_VALUE = 19, 26       # 7.7 pt, 10.5 pt
F_NODE, F_NODE_SUB = 22, 19             # 8.9 pt, 7.7 pt
F_BRACKET, F_NOTE, F_NOTE_SUB = 20, 20, 19


def f(sz, bold=False):
    return ImageFont.truetype(FONT_B if bold else FONT, sz * S)


def text_w(d, s, font):
    return d.textbbox((0, 0), s, font=font)[2]


def main():
    img = Image.new("RGB", (W * S, H * S), WHITE)
    d = ImageDraw.Draw(img)

    # ------------------------------------------------- panel A: selection
    d.text((50 * S, 30 * S), "SINGLE-WINDOW SELECTION",
           font=f(F_EYEBROW, True), fill=MUTED)
    d.text((50 * S, 64 * S), "one field of view selected, curated, and trained",
           font=f(F_LEAD), fill=INK)

    steps = (
        ("FULL VOLUME", f"{NX}×{NY}×{NZ}"),
        ("FINE SCAN", "831 retained"),
        ("RANKING", "residual + ramp"),
        ("SELECTED", f"{WX}×{WY}×{WZ}"),
    )

    # size the boxes to the widest label they must hold, then centre the row
    pad = 26 * S
    need = max(max(text_w(d, t, f(F_BOX_TITLE, True)),
                   text_w(d, v, f(F_BOX_VALUE, True))) for t, v in steps)
    bw = need + 2 * pad
    gap = 44 * S
    row_w = 4 * bw + 3 * gap
    x0 = (W * S - row_w) / 2
    y0, bh = 132 * S, 150 * S

    for i, (title, value) in enumerate(steps):
        left = x0 + i * (bw + gap)
        final = i == len(steps) - 1
        d.rounded_rectangle([left, y0, left + bw, y0 + bh], radius=14 * S,
                            fill=BLUE if final else SOFT,
                            outline=BLUE if final else LINE, width=3 * S)
        d.text((left + bw / 2, y0 + 52 * S), title, font=f(F_BOX_TITLE, True),
               fill=WHITE if final else MUTED, anchor="mm")
        d.text((left + bw / 2, y0 + 100 * S), value, font=f(F_BOX_VALUE, True),
               fill=WHITE if final else INK, anchor="mm")
        if not final:
            ax = left + bw + 8 * S
            bxx = left + bw + gap - 8 * S
            ay = y0 + bh / 2
            d.line([ax, ay, bxx, ay], fill=BLUE, width=3 * S)
            d.polygon([(bxx, ay), (bxx - 12 * S, ay - 8 * S),
                       (bxx - 12 * S, ay + 8 * S)], fill=BLUE)

    d.text((50 * S, 312 * S),
           "rank 15 of 831 · same low-distortion family as rank 6, "
           "with less surface contact",
           font=f(F_NOTE_SUB), fill=MUTED)

    # ------------------------------------------------- panel B: time states
    d.text((50 * S, 392 * S), "TEMPORAL SUPPORT",
           font=f(F_EYEBROW, True), fill=MUTED)
    d.text((50 * S, 426 * S), "five states, four intervals of 2 h",
           font=f(F_LEAD), fill=INK)

    tx0, tx1 = 78 * S, (W - 78) * S
    ty = 540 * S
    d.line([tx0, ty, tx1, ty], fill=LINE, width=3 * S)
    xs = [tx0 + (tx1 - tx0) * i / (len(HOLDS) - 1) for i in range(len(HOLDS))]
    for i, (x, h) in enumerate(zip(xs, HOLDS)):
        trained = i <= 1
        r = 13 * S
        d.ellipse([x - r, ty - r, x + r, ty + r],
                  fill=BLUE if trained else WHITE, outline=BLUE, width=3 * S)
        d.text((x, ty - 42 * S), f"T{i}", font=f(F_NODE, True), fill=INK,
               anchor="mm")
        d.text((x, ty + 42 * S), f"{h} h", font=f(F_NODE_SUB), fill=MUTED,
               anchor="mm")

    def bracket(x_a, x_b, y, label, solid):
        colour = BLUE if solid else MUTED
        d.line([x_a, y, x_b, y], fill=colour, width=3 * S)
        for x in (x_a, x_b):
            d.line([x, y - 10 * S, x, y + 10 * S], fill=colour, width=3 * S)
        d.text(((x_a + x_b) / 2, y + 32 * S), label, font=f(F_BRACKET, True),
               fill=colour, anchor="mm")

    # Both intervals belong to Aim 1; the labels name the role, not the aim,
    # so that renumbering the aims cannot make the figure wrong again.
    bracket(xs[0], xs[1], ty + 98 * S, "training transition", True)
    bracket(xs[2], xs[4], ty + 98 * S, "held out from fitting", False)

    d.text((50 * S, 698 * S),
           "same field of view · later states already examined",
           font=f(F_NOTE), fill=INK)
    d.text((50 * S, 732 * S),
           "retrospective temporal evaluation, not a new blind test",
           font=f(F_NOTE_SUB), fill=MUTED)

    img.resize((W, H), Image.LANCZOS).save(OUT)
    print(f"wrote {OUT}  {W}x{H}")


if __name__ == "__main__":
    main()
