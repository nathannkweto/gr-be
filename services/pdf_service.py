from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from io import BytesIO

def create_pdf_from_dict(data: dict, title: str = "Quote Request") -> BytesIO:
    """
    Creates a styled PDF from a dictionary of form fields with proper word wrapping.
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            rightMargin=50, leftMargin=50,
                            topMargin=50, bottomMargin=50)

    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.darkblue,
        spaceAfter=12
    )
    key_style = ParagraphStyle(
        'KeyStyle',
        parent=styles['Normal'],
        fontName="Helvetica-Bold",
        spaceAfter=2
    )
    value_style = ParagraphStyle(
        'ValueStyle',
        parent=styles['Normal'],
        fontName="Helvetica",
        spaceAfter=10
    )

    elements = []

    # Add title
    elements.append(Paragraph(title, title_style))
    elements.append(Spacer(1, 12))

    # Add a separator line (fake using underscores)
    elements.append(Paragraph("<font color='grey'>__________________________________________________</font>", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Add form fields
    for key, value in data.items():
        elements.append(Paragraph(f"{key}:", key_style))
        elements.append(Paragraph(str(value), value_style))

    # Build PDF
    doc.build(elements)
    buffer.seek(0)
    return buffer
