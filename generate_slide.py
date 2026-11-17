from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


OUTPUT = Path(__file__).with_name("Smartnode_customer_support_use_cases.pptx")

NAVY = RGBColor(17, 35, 62)
BLUE = RGBColor(31, 108, 186)
TEAL = RGBColor(0, 143, 143)
INK = RGBColor(38, 51, 68)
MUTED = RGBColor(91, 107, 124)
PALE = RGBColor(241, 246, 250)
WHITE = RGBColor(255, 255, 255)


def add_text(slide, text, x, y, w, h, size, color, bold=False, font="Aptos"):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    frame = box.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.margin_left = Inches(0)
    frame.margin_right = Inches(0)
    frame.margin_top = Inches(0)
    frame.margin_bottom = Inches(0)
    paragraph = frame.paragraphs[0]
    paragraph.text = text
    paragraph.font.name = font
    paragraph.font.size = Pt(size)
    paragraph.font.bold = bold
    paragraph.font.color.rgb = color
    return box


def add_card(slide, x, y, w, h, title, body, accent):
    card = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h)
    )
    card.fill.solid()
    card.fill.fore_color.rgb = WHITE
    card.line.color.rgb = RGBColor(222, 230, 238)
    card.line.width = Pt(0.8)
    card.adjustments[0] = 0.08

    strip = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(x), Inches(y + 0.05), Inches(0.055), Inches(h - 0.1)
    )
    strip.fill.solid()
    strip.fill.fore_color.rgb = accent
    strip.line.fill.background()

    add_text(slide, title, x + 0.2, y + 0.16, w - 0.38, 0.28, 14, NAVY, True)
    add_text(slide, body, x + 0.2, y + 0.52, w - 0.38, h - 0.62, 10.5, INK)


def build_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = PALE

    header = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.25)
    )
    header.fill.solid()
    header.fill.fore_color.rgb = NAVY
    header.line.fill.background()
    add_text(slide, "SMARTNODE  |  CUSTOMER SUPPORT", 0.55, 0.22, 7.5, 0.22, 10, RGBColor(151, 210, 225), True)
    add_text(slide, "Make every customer contact count", 0.55, 0.52, 9.5, 0.48, 25, WHITE, True)
    add_text(slide, "AI/ML opportunities to resolve faster, route smarter, and reduce avoidable work", 0.57, 1.00, 11.6, 0.22, 10, RGBColor(222, 232, 241))

    add_text(slide, "PRIORITY USE CASES", 0.58, 1.52, 4.0, 0.25, 10, BLUE, True)
    cards = [
        ("1  Voice triage + agent assist",
         "Transcribe calls, summarize the issue, extract product/serial/dealer, and route Closed / Open / Urgent. "
         "Target: 20–30% less after-call work; faster safety-case escalation.", BLUE),
        ("2  Guided self-service",
         "Ground answers in approved manuals, warranty terms, and troubleshooting steps; hand off with context. "
         "Target: 10–20% fewer repeat contacts for eligible intents.", TEAL),
        ("3  Dealer case intake",
         "Auto-check claim completeness, categorize warranty/service requests, and suggest the next queue. "
         "Target: fewer avoidable transfers and incomplete submissions.", BLUE),
        ("4  Proactive service signals",
         "Combine consented product telemetry and service history to flag likely failures before customers call. "
         "Target: prevent avoidable downtime and repeat visits.", TEAL),
        ("5  Quality + sentiment insights",
         "Find recurring defects, friction points, and coaching opportunities across calls and cases. "
         "Target: improve first-contact resolution and customer satisfaction.", BLUE),
        ("6  Demand + staffing forecast",
         "Forecast contact volume by season, product, and dealer; align staffing and parts/service capacity. "
         "Target: shorter queues and better peak coverage.", TEAL),
    ]
    positions = [
        (0.58, 1.88), (4.52, 1.88), (8.46, 1.88),
        (0.58, 3.28), (4.52, 3.28), (8.46, 3.28),
    ]
    for (title, body, accent), (x, y) in zip(cards, positions):
        add_card(slide, x, y, 3.68, 1.22, title, body, accent)

    band = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.58), Inches(4.78), Inches(12.0), Inches(0.72)
    )
    band.fill.solid()
    band.fill.fore_color.rgb = RGBColor(225, 239, 248)
    band.line.fill.background()
    add_text(slide, "PILOT SCORECARD  |  Targets to validate vs. baseline",
             0.80, 4.91, 4.2, 0.20, 10, NAVY, True)
    add_text(slide, "−20–30% after-call work     •     −10–20% repeat contacts     •     <5 min urgent routing     •     +5 pp first-contact resolution",
             0.80, 5.19, 11.5, 0.20, 11, INK, True)

    add_text(slide, "START SMALL", 0.60, 5.75, 1.3, 0.22, 10, BLUE, True)
    add_text(slide, "Pilot on a consented, redacted call set; validate triage with agents; measure time saved, routing accuracy, "
                    "repeat contacts, and CSAT. Keep urgent decisions human-reviewed.",
             1.72, 5.72, 10.75, 0.42, 10, INK)
    add_text(slide, "Assumptions: Smartnode supports installed/connected products and dealer service; targets are hypotheses, not measured results. "
                    "POC data: PolyAI MInDS-14 (CC-BY-4.0), banking speech only—not Smartnode calls. "
                    "Sources: huggingface.co/datasets/PolyAI/minds14. Privacy, consent, retention, and safety policy required before production.",
             0.60, 6.72, 12.0, 0.45, 7.5, MUTED)

    prs.save(OUTPUT)
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    build_deck()
