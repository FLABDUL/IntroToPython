from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, query: str):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL database...")

    def execute(self, query: str):
        print(f"MySQL executing query: {query}")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connecting to PostgreSQL database...")

    def execute(self, query: str):
        print(f"PostgreSQL executing query: {query}")

class Application:
    def __init__(self, database: Database):
        self.database = database

    def run(self):
        self.database.connect()
        self.database.execute("SELECT * FROM users")

# Using MySQL
mysql_db = MySQLDatabase()
app = Application(mysql_db)
app.run()

# Switch to PostgreSQL without changing Application code
postgres_db = PostgreSQLDatabase()
app = Application(postgres_db)
app.run()
