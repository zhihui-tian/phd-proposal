from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas


OUTPUT = Path(__file__).resolve().parent / "proposal_framework.pdf"

PAGE_W = 468
PAGE_H = 384

INK = HexColor("#1D2D39")
MUTED = HexColor("#596A76")
LINE = HexColor("#C8D0D5")
BLUE = HexColor("#477790")
TEAL = HexColor("#4E8982")
SOFT_BLUE = HexColor("#EEF4F7")
SOFT_TEAL = HexColor("#EEF6F5")


def draw_spaced_label(c, x, y, text, align="left"):
    obj = c.beginText()
    obj.setFont("Helvetica-Bold", 6.8)
    obj.setFillColor(MUTED)
    obj.setCharSpace(0.65)
    width = c.stringWidth(text, "Helvetica-Bold", 6.8) + 0.65 * max(len(text) - 1, 0)
    if align == "center":
        obj.setTextOrigin(x - width / 2, y)
    else:
        obj.setTextOrigin(x, y)
    obj.textLine(text)
    c.drawText(obj)


def draw_right_arrow(c, x1, y, x2, color=BLUE):
    c.setStrokeColor(color)
    c.setLineWidth(0.9)
    c.line(x1, y, x2, y)
    c.line(x2 - 4, y + 3, x2, y)
    c.line(x2 - 4, y - 3, x2, y)


def draw_foundation_text(c, x, y, status, title, subtitle):
    draw_spaced_label(c, x, y + 24, status.upper())
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 9.2)
    c.drawString(x, y + 9, title)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 7.7)
    c.drawString(x, y - 4, subtitle)


def draw_simulation_schematic(c, x, y):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.65)
    c.circle(x + 16, y + 18, 14, fill=0, stroke=1)
    c.setFillColor(BLUE)
    for px, py in ((9, 14), (17, 25), (25, 12)):
        c.circle(x + px, y + py, 1.5, fill=1, stroke=0)

    draw_right_arrow(c, x + 34, y + 18, x + 51)

    c.setFillColor(SOFT_BLUE)
    c.setStrokeColor(LINE)
    c.rect(x + 60, y + 3, 31, 30, fill=1, stroke=1)
    c.setStrokeColor(MUTED)
    c.setLineWidth(0.55)
    c.line(x + 60, y + 20, x + 70, y + 14)
    c.line(x + 70, y + 14, x + 80, y + 18)
    c.line(x + 80, y + 18, x + 91, y + 9)
    c.line(x + 70, y + 14, x + 68, y + 3)
    c.line(x + 80, y + 18, x + 82, y + 33)


def draw_scaling_schematic(c, x, y):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.65)
    c.line(x + 4, y + 14, x + 17, y + 7)
    c.line(x + 17, y + 7, x + 30, y + 14)
    c.line(x + 30, y + 14, x + 17, y + 21)
    c.line(x + 17, y + 21, x + 4, y + 14)
    c.line(x + 4, y + 14, x + 4, y + 29)
    c.line(x + 17, y + 21, x + 17, y + 36)
    c.line(x + 30, y + 14, x + 30, y + 29)
    c.line(x + 4, y + 29, x + 17, y + 36)
    c.line(x + 17, y + 36, x + 30, y + 29)

    draw_right_arrow(c, x + 36, y + 21, x + 52)

    c.line(x + 60, y + 11, x + 77, y + 2)
    c.line(x + 77, y + 2, x + 94, y + 11)
    c.line(x + 94, y + 11, x + 77, y + 20)
    c.line(x + 77, y + 20, x + 60, y + 11)
    c.line(x + 60, y + 11, x + 60, y + 31)
    c.line(x + 77, y + 20, x + 77, y + 40)
    c.line(x + 94, y + 11, x + 94, y + 31)
    c.line(x + 60, y + 31, x + 77, y + 40)
    c.line(x + 77, y + 40, x + 94, y + 31)
    c.line(x + 68, y + 16, x + 68, y + 35)
    c.line(x + 86, y + 16, x + 86, y + 35)


def draw_experiment_schematic(c, x, y):
    for offset, variant in ((0, 0), (42, 1)):
        left = x + offset
        c.setFillColor(SOFT_TEAL)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.65)
        c.rect(left, y + 5, 31, 31, fill=1, stroke=1)
        c.setStrokeColor(MUTED if variant == 0 else TEAL)
        c.setLineWidth(0.55)
        c.line(left, y + 23, left + 11, y + 16)
        c.line(left + 11, y + 16, left + 21, y + 20)
        c.line(left + 21, y + 20, left + 31, y + 10)
        c.line(left + 11, y + 16, left + 9, y + 5)
        c.line(left + 21, y + 20, left + 23, y + 36)
    draw_right_arrow(c, x + 33, y + 21, x + 40, TEAL)

    draw_right_arrow(c, x + 75, y + 21, x + 88, TEAL)
    c.setStrokeColor(LINE)
    c.line(x + 94, y + 7, x + 94, y + 35)
    c.line(x + 94, y + 7, x + 115, y + 7)
    c.setStrokeColor(TEAL)
    c.setLineWidth(1.0)
    c.bezier(x + 97, y + 11, x + 102, y + 12, x + 108, y + 28, x + 114, y + 31)


def draw_foundation_merge(c):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.65)
    c.line(53, 250, 53, 241)
    c.line(234, 250, 234, 233)
    c.line(415, 250, 415, 241)
    c.line(53, 241, 415, 241)
    c.line(234, 233, 234, 224)
    c.setStrokeColor(BLUE)
    c.line(230, 229, 234, 224)
    c.line(238, 229, 234, 224)


def draw_focus(c):
    draw_spaced_label(c, PAGE_W / 2, 210, "EXPERIMENT-CENTERED AIMS", align="center")
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 10.2)
    c.drawCentredString(PAGE_W / 2, 195, "Measured 4D grain evolution is the scientific target")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8.1)
    c.drawCentredString(
        PAGE_W / 2,
        181,
        "Local learning is the tool; experimental behavior defines the claims",
    )


def draw_aim_text(c, x, y, aim, title, subtitle):
    draw_spaced_label(c, x, y + 33, aim.upper())
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 11.2)
    c.drawString(x, y + 15, title)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8.5)
    c.drawString(x, y, subtitle)


def draw_aim_gate(c, y):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.65)
    c.line(153, y, 280, y)
    c.line(302, y, PAGE_W - 22, y)
    c.setStrokeColor(BLUE)
    c.setLineWidth(0.9)
    c.line(285, y - 4, 291, y - 10)
    c.line(291, y - 10, 297, y - 4)


def draw_aim1_schematic(c, x, y):
    for offset in (0, 36, 72):
        left = x + offset
        c.setFillColor(SOFT_TEAL)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.65)
        c.rect(left, y + 7, 29, 29, fill=1, stroke=1)
        c.setStrokeColor(MUTED)
        c.setLineWidth(0.5)
        c.line(left, y + 23, left + 10, y + 17)
        c.line(left + 10, y + 17, left + 20, y + 21)
        c.line(left + 20, y + 21, left + 29, y + 12)
        c.line(left + 10, y + 17, left + 8, y + 7)
        c.line(left + 20, y + 21, left + 21, y + 36)
        c.setFillColor(BLUE)
        c.circle(left + 15, y + 11, 1.4, fill=1, stroke=0)


def draw_hat_label(c, x, y, label, color):
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", 8.2)
    c.drawCentredString(x, y, label)
    c.setStrokeColor(color)
    c.setLineWidth(0.7)
    c.line(x - 3, y + 9, x, y + 12)
    c.line(x, y + 12, x + 3, y + 9)


def draw_aim2_schematic(c, x, y):
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 8.2)
    c.drawCentredString(x + 4, y + 29, "S")
    c.drawCentredString(x + 4, y + 5, "E")
    draw_hat_label(c, x + 80, y + 29, "S", TEAL)
    draw_hat_label(c, x + 80, y + 5, "E", TEAL)

    c.setStrokeColor(LINE)
    c.setLineWidth(0.55)
    c.line(x + 16, y + 25, x + 16, y + 38)
    c.line(x + 16, y + 25, x + 64, y + 25)
    c.line(x + 16, y + 1, x + 16, y + 14)
    c.line(x + 16, y + 1, x + 64, y + 1)
    c.setStrokeColor(BLUE)
    c.setLineWidth(1.0)
    c.bezier(x + 18, y + 29, x + 31, y + 42, x + 45, y + 21, x + 62, y + 34)
    c.setStrokeColor(TEAL)
    c.bezier(x + 18, y + 5, x + 31, y + 18, x + 45, y - 3, x + 62, y + 10)

    c.setStrokeColor(LINE)
    c.line(x + 92, y + 2, x + 92, y + 38)
    c.line(x + 92, y + 2, x + 115, y + 2)
    c.setFillColor(BLUE)
    c.circle(x + 100, y + 12, 1.6, fill=1, stroke=0)
    c.setFillColor(TEAL)
    c.circle(x + 108, y + 22, 1.6, fill=1, stroke=0)


def draw_aim3_schematic(c, x, y):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.65)
    c.line(x, y + 2, x, y + 39)
    c.line(x, y + 2, x + 42, y + 2)
    c.setStrokeColor(BLUE)
    c.setLineWidth(1.05)
    c.bezier(x + 4, y + 6, x + 14, y + 8, x + 22, y + 28, x + 39, y + 34)
    c.setFillColor(BLUE)
    c.circle(x + 11, y + 9, 1.6, fill=1, stroke=0)
    c.circle(x + 25, y + 26, 1.6, fill=1, stroke=0)
    draw_right_arrow(c, x + 49, y + 21, x + 64)

    c.setFillColor(SOFT_TEAL)
    c.setStrokeColor(LINE)
    c.circle(x + 88, y + 21, 18, fill=1, stroke=1)
    c.setStrokeColor(TEAL)
    c.setLineWidth(0.9)
    c.bezier(x + 75, y + 27, x + 82, y + 9, x + 94, y + 11, x + 102, y + 22)
    c.bezier(x + 75, y + 15, x + 84, y + 17, x + 94, y + 32, x + 102, y + 29)


def build():
    c = canvas.Canvas(str(OUTPUT), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    c.setTitle("Dissertation research framework")
    c.setAuthor("Zhihui Tian")
    c.setFillColor(white)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    draw_spaced_label(c, 20, 366, "COMPLETED AND PRELIMINARY FOUNDATIONS")

    col_x = (20, 181, 342)
    draw_simulation_schematic(c, col_x[0], 304)
    draw_foundation_text(
        c,
        col_x[0],
        274,
        "Completed",
        "Control simulation physics",
        "Neighborhood-defined labels",
    )

    draw_right_arrow(c, 144, 326, 166)

    draw_scaling_schematic(c, col_x[1], 301)
    draw_foundation_text(
        c,
        col_x[1],
        274,
        "Completed - under review",
        "Scale local learning",
        "Scalable 3D-PRIMME rollouts",
    )

    draw_right_arrow(c, 305, 326, 327)

    draw_experiment_schematic(c, col_x[2], 303)
    draw_foundation_text(
        c,
        col_x[2],
        274,
        "Stable preliminary work",
        "Curate 4D experiments",
        "Registered grain evolution",
    )

    draw_foundation_merge(c)
    draw_focus(c)

    draw_aim1_schematic(c, 26, 128)
    draw_aim_text(
        c,
        160,
        132,
        "Aim 1",
        "Establish reliable experimental learning",
        "Cross-window generalization, uncertainty, and applicability limits",
    )
    draw_aim_gate(c, 119)

    draw_aim2_schematic(c, 26, 68)
    draw_aim_text(
        c,
        160,
        72,
        "Aim 2",
        "Quantify domain-specific surrogate fidelity",
        "Paired reference and trained evolution within each domain",
    )
    draw_aim_gate(c, 59)

    draw_aim3_schematic(c, 26, 8)
    draw_aim_text(
        c,
        160,
        12,
        "Aim 3",
        "Interpret learned evolution mechanisms",
        "Robust rules tested against independent physical evidence",
    )

    c.showPage()
    c.save()


if __name__ == "__main__":
    build()
