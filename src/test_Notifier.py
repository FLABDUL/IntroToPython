# test_notifier.py

import unittest

from Notifier import NotificationManager


# Mock class to simulate the EmailService
class MockEmailService:
    def send(self, message, to):
        # Simulated return value
        return f"[Mocked] Email to {to}: {message}"


class TestNotificationManager(unittest.TestCase):
    def test_notify_user_with_mock(self):
        # Inject mock service instead of real email service
        mock_service = MockEmailService()
        notifier = NotificationManager(mock_service)

        result = notifier.notify_user("user@example.com", "Hello!")

        # Validate mock behavior
        self.assertEqual(result, "[Mocked] Email to user@example.com: Hello!")


if __name__ == '__main__':
    unittest.main()
