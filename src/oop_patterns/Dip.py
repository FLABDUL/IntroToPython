class MySQLDatabase:
    def connect(self):
        pass

class Application:
    def __init__(self):
        self.db = MySQLDatabase()  # tightly coupled

class Database:
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL")

class Application:
    def __init__(self, db: Database):
        self.db = db

# Usage
app = Application(MySQLDatabase())
