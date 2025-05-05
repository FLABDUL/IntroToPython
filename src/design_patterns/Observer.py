from abc import abstractmethod, ABC


class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

# Concrete observer
class EmailSubscriber(Observer):
    def __init__(self):
        self.messages = []

    def update(self, message: str):
        self.messages.append(f"Email received: {message}")
