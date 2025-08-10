from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from io import BytesIO
import smtplib

class EmailService:
    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email_with_pdf(self, subject, recipient, pdf_buffer: BytesIO, filename="form.pdf"):
        """
        Sends an email with both HTML and plain-text bodies, attaching the given PDF.
        """

        # Reset buffer position to start
        pdf_buffer.seek(0)

        # Create a multipart/mixed container (for attachments)
        message = MIMEMultipart("mixed")
        message["From"] = self.smtp_user
        message["To"] = recipient
        message["Subject"] = subject

        # Create a multipart/alternative container for text + html bodies
        body = MIMEMultipart("alternative")

        # Plain-text fallback
        text_body = (
            f"Hello,\n\n"
            f"Someone requested for a quote.\n"
            f"Please find the details of their request in the attached pdf.\n\n"
            f"Best regards,\nNathan"
        )

        # HTML body with styling
        html_body = f"""
        <html>
            <body style="font-family: Arial, sans-serif; color: #333;">
                <h2 style="color: #004080;">New Quote Request</h2>
                <p>Dear user,</p>
                <p>Someone requested for a quote. Please find attached the PDF copy of the quote request details.</p>
                <p style="margin-top: 20px;">Don't forget to contact them through their email.</p>
                <br>
                <p style="font-size: 14px; color: #666;">Best regards,<br>Nathan</p>
            </body>
        </html>
        """

        # Attach plain and HTML parts to the alternative container
        body.attach(MIMEText(text_body, "plain"))
        body.attach(MIMEText(html_body, "html"))

        # Attach the alternative part to the main message
        message.attach(body)

        # Attach PDF file
        pdf_attachment = MIMEApplication(pdf_buffer.read(), _subtype="pdf")
        pdf_attachment.add_header("Content-Disposition", "attachment", filename=filename)
        message.attach(pdf_attachment)

        # Send the email
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            server.sendmail(self.smtp_user, recipient, message.as_string())
