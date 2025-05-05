import unittest

from src.design_patterns.Observer import Subject, EmailSubscriber


class TestObserver(unittest.TestCase):
    def test_observer_notification(self):
        subject = Subject()
        subscriber1 = EmailSubscriber()
        subscriber2 = EmailSubscriber()

        subject.attach(subscriber1)
        subject.attach(subscriber2)

        subject.notify("New blog post!")

        self.assertIn("Email received: New blog post!", subscriber1.messages)
        self.assertIn("Email received: New blog post!", subscriber2.messages)
