import sqlite3


class DatabaseManager:
    def __init__(self, db_name="monitoring.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.init_db()

    def init_db(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                cpu_usage REAL,
                ram_usage REAL,
                disk_usage REAL
            )
            """
        )
        self.conn.commit()

    def insert_record(self, timestamp, cpu, ram, disk):
        self.cursor.execute(
            "INSERT INTO stats (timestamp, cpu_usage, ram_usage, disk_usage) VALUES (?, ?, ?, ?)",
            (timestamp, cpu, ram, disk),
        )
        self.conn.commit()

    def close(self):
        self.conn.close()
