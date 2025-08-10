import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
    MAIL_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
    MAIL_PORT = int(os.getenv("SMTP_PORT", 587))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "true").lower() in ["true", "1", "yes"]
    MAIL_USERNAME = os.getenv("SMTP_USER")
    MAIL_PASSWORD = os.getenv("SMTP_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", MAIL_USERNAME)
    EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")