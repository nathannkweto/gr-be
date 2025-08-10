from flask import Blueprint, request, jsonify, current_app
from services.pdf_service import create_pdf_from_dict
from config import Config
from services.email_service import EmailService

form_bp = Blueprint("form", __name__)


@form_bp.route("/submit", methods=["POST"])
def submit_form():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid request"}), 400

    pdf_buffer = create_pdf_from_dict(data)

    recipient = current_app.config.get("EMAIL_RECIPIENT")
    if not recipient:
        return jsonify({"error": "Recipient email not configured"}), 500

    email_service = current_app.email_service
    email_service.send_email_with_pdf(
        subject="New Quote Request",
        recipient=recipient,
        pdf_buffer=pdf_buffer,
        filename="project_overview.pdf"
    )

    return jsonify({"status": "success", "message": f"PDF sent to {recipient}"}), 200
