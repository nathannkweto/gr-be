from flask import Flask
from flask_cors import CORS
from config import Config
from routes.api import form_bp
from services.email_service import EmailService

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize EmailService with config values
    email_service = EmailService(
        smtp_server=app.config['MAIL_SERVER'],
        smtp_port=app.config['MAIL_PORT'],
        smtp_user=app.config['MAIL_USERNAME'],
        smtp_password=app.config['MAIL_PASSWORD'],
    )

    # Attach email_service instance to app context for access in routes
    app.extensions = getattr(app, "extensions", {})

    app.email_service = email_service

    CORS(app)

    # Register Blueprint
    app.register_blueprint(form_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
