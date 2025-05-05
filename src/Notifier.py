# notifier.py

class EmailService:
    def send(self, message: str, to: str) -> str:
        # Simulates sending an email
        return f"Email sent to {to}: {message}"


class NotificationManager:
    """
    This class depends on an email service, which is injected.
    This allows for flexibility and testability.
    """
    def __init__(self, email_service: EmailService):
        # Dependency is injected through the constructor
        self.email_service = email_service

    def notify_user(self, user_email: str, message: str) -> str:
        # Delegates sending to the injected email service
        return self.email_service.send(message, user_email)
