from src.oop_patterns.DipExpanded import Database, Application


class MockDatabase(Database):
    def connect(self):
        print("Mock connect called")

    def execute(self, query: str):
        print(f"Mock executing: {query}")

# Use for testing
mock_db = MockDatabase()
test_app = Application(mock_db)
test_app.run()
