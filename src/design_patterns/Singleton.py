class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # Create only one instance
            cls._instance = super().__new__(cls)
        return cls._instance
