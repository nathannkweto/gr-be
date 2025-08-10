from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from io import BytesIO

def create_pdf_from_dict(data: dict, title: str = "Form Submission") -> BytesIO:
    """
    Creates a styled PDF from a dictionary of form fields.
    """
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Title
    pdf.setFont("Helvetica-Bold", 16)
    pdf.setFillColor(colors.darkblue)
    pdf.drawString(100, height - inch, title)
    pdf.setFillColor(colors.black)

    # Draw a separator line
    pdf.setStrokeColor(colors.grey)
    pdf.setLineWidth(0.5)
    pdf.line(100, height - inch - 5, width - 100, height - inch - 5)

    # Start position for form fields
    y_position = height - inch - 30

    pdf.setFont("Helvetica", 12)
    for key, value in data.items():
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(100, y_position, f"{key}:")
        pdf.setFont("Helvetica", 12)
        pdf.drawString(250, y_position, str(value))
        y_position -= 20

        # New page if content overflows
        if y_position < 50:
            pdf.showPage()
            y_position = height - inch

    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return buffer
