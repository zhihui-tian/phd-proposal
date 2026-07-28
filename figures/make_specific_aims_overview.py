from pathlib import Path

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white


OUTPUT = Path(__file__).resolve().parent / "specific_aims_overview.pdf"

PAGE_W = 468
PAGE_H = 276

INK = HexColor("#1D2D39")
MUTED = HexColor("#596A76")
LINE = HexColor("#C8D0D5")
BLUE = HexColor("#477790")
TEAL = HexColor("#4E8982")
SOFT_BLUE = HexColor("#EEF4F7")
SOFT_TEAL = HexColor("#EEF6F5")


def draw_text(c, x, y, aim, title, subtitle):
    label = c.beginText(x, y + 38)
    label.setFont("Helvetica-Bold", 7.5)
    label.setFillColor(MUTED)
    label.setCharSpace(0.7)
    label.textLine(aim.upper())
    c.drawText(label)

    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x, y + 19, title)

    c.setFillColor(MUTED)
    c.setFont("Helvetica", 9)
    c.drawString(x, y + 3, subtitle)


def draw_arrow(c, x1, y, x2, color=BLUE):
    c.setStrokeColor(color)
    c.setLineWidth(1.05)
    c.line(x1, y, x2, y)
    c.line(x2 - 4, y + 3, x2, y)
    c.line(x2 - 4, y - 3, x2, y)


def draw_gate(c, y):
    center_x = 262
    c.setStrokeColor(LINE)
    c.setLineWidth(0.65)
    c.line(145, y, center_x - 11, y)
    c.line(center_x + 11, y, PAGE_W - 22, y)

    c.setStrokeColor(BLUE)
    c.setLineWidth(0.9)
    c.line(center_x - 6, y - 4, center_x, y - 10)
    c.line(center_x, y - 10, center_x + 6, y - 4)


def draw_aim1_schematic(c, x, y):
    size = 33
    gap = 24

    for offset, variant in ((0, 0), (size + gap, 1)):
        left = x + offset
        bottom = y + 6
        c.setFillColor(SOFT_BLUE)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.65)
        c.rect(left, bottom, size, size, fill=1, stroke=1)

        c.setStrokeColor(MUTED)
        c.setLineWidth(0.55)
        if variant == 0:
            c.line(left + 11, bottom, left + 9, bottom + 16)
            c.line(left + 9, bottom + 16, left + 17, bottom + 33)
            c.line(left, bottom + 22, left + 9, bottom + 16)
            c.line(left + 9, bottom + 16, left + 25, bottom + 15)
            c.line(left + 25, bottom + 15, left + 33, bottom + 25)
            c.line(left + 25, bottom + 15, left + 24, bottom)
        else:
            c.line(left + 8, bottom, left + 12, bottom + 14)
            c.line(left + 12, bottom + 14, left + 20, bottom + 33)
            c.line(left, bottom + 23, left + 12, bottom + 14)
            c.line(left + 12, bottom + 14, left + 27, bottom + 17)
            c.line(left + 27, bottom + 17, left + 33, bottom + 27)
            c.line(left + 27, bottom + 17, left + 25, bottom)

        c.setFillColor(BLUE)
        for px, py in ((7, 27), (18, 8), (27, 24)):
            c.circle(left + px, bottom + py, 1.4, fill=1, stroke=0)

    draw_arrow(c, x + size + 5, y + 22, x + size + gap - 5)


def draw_hat_label(c, x, y, label, color=INK):
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawCentredString(x, y, label)
    c.setStrokeColor(color)
    c.setLineWidth(0.75)
    c.line(x - 3, y + 10, x, y + 13)
    c.line(x, y + 13, x + 3, y + 10)


def draw_aim2_schematic(c, x, y):
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 8.5)

    c.drawCentredString(x + 6, y + 33, "S")
    draw_hat_label(c, x + 90, y + 33, "S", TEAL)
    draw_arrow(c, x + 16, y + 36, x + 79, TEAL)

    c.drawCentredString(x + 6, y + 7, "E")
    draw_hat_label(c, x + 90, y + 7, "E", TEAL)
    draw_arrow(c, x + 16, y + 10, x + 79, TEAL)

    c.setStrokeColor(LINE)
    c.setLineWidth(0.55)
    c.line(x + 22, y + 29, x + 22, y + 43)
    c.line(x + 22, y + 29, x + 72, y + 29)
    c.line(x + 22, y + 3, x + 22, y + 17)
    c.line(x + 22, y + 3, x + 72, y + 3)

    c.setStrokeColor(BLUE)
    c.setLineWidth(1.0)
    c.bezier(x + 24, y + 33, x + 38, y + 48, x + 54, y + 25, x + 70, y + 39)

    c.setStrokeColor(TEAL)
    c.bezier(x + 24, y + 7, x + 39, y + 20, x + 53, y - 1, x + 70, y + 12)


def draw_aim3_schematic(c, x, y):
    plot_x = x
    plot_y = y + 4
    c.setStrokeColor(LINE)
    c.setLineWidth(0.65)
    c.line(plot_x, plot_y, plot_x, plot_y + 38)
    c.line(plot_x, plot_y, plot_x + 42, plot_y)

    c.setStrokeColor(BLUE)
    c.setLineWidth(1.15)
    c.bezier(
        plot_x + 4,
        plot_y + 5,
        plot_x + 13,
        plot_y + 7,
        plot_x + 22,
        plot_y + 27,
        plot_x + 38,
        plot_y + 33,
    )
    c.setFillColor(BLUE)
    for px, py in ((8, 8), (21, 21), (35, 31)):
        c.circle(plot_x + px, plot_y + py, 1.7, fill=1, stroke=0)

    draw_arrow(c, x + 49, y + 24, x + 65)

    cx = x + 87
    cy = y + 24
    c.setFillColor(SOFT_TEAL)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.7)
    c.circle(cx, cy, 19, fill=1, stroke=1)

    c.setStrokeColor(TEAL)
    c.setLineWidth(0.9)
    c.bezier(cx - 13, cy - 8, cx - 4, cy + 14, cx + 4, cy + 7, cx + 13, cy - 2)
    c.bezier(cx - 12, cy + 7, cx - 1, cy + 3, cx + 5, cy - 12, cx + 13, cy - 9)


def build():
    c = canvas.Canvas(str(OUTPUT), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    c.setTitle("Specific Aims overview")
    c.setAuthor("Zhihui Tian")
    c.setFillColor(white)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    row_y = (207, 115, 23)
    text_x = 160

    draw_aim1_schematic(c, 28, row_y[0] + 2)
    draw_text(
        c,
        text_x,
        row_y[0],
        "Aim 1",
        "Establish reliable experimental learning",
        "Cross-window generalization, uncertainty, and applicability limits",
    )

    draw_gate(c, 185)

    draw_aim2_schematic(c, 28, row_y[1] + 3)
    draw_text(
        c,
        text_x,
        row_y[1],
        "Aim 2",
        "Quantify domain-specific surrogate fidelity",
        "Paired reference and trained evolution within each domain",
    )

    draw_gate(c, 93)

    draw_aim3_schematic(c, 28, row_y[2] + 3)
    draw_text(
        c,
        text_x,
        row_y[2],
        "Aim 3",
        "Interpret learned evolution mechanisms",
        "Robust rules tested against independent physical evidence",
    )

    c.showPage()
    c.save()


if __name__ == "__main__":
    build()
