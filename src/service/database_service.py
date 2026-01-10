import sqlite3
from pathlib import Path


class DatabaseService:
    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent
        db_dir = base_dir / "db"
        db_dir.mkdir(exist_ok=True)

        self.DB = db_dir / "database.sqlite3"
        self._create_tables()

    def _create_tables(self):
        with sqlite3.connect(self.DB) as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.cursor()

            cursor.executescript("""
            CREATE TABLE IF NOT EXISTS backups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                backup_path TEXT,
                destination_path TEXT,
                frequency TEXT NOT NULL
                    CHECK (frequency IN ('monthly', 'weekly', 'daily')),
                time TEXT,
                day_of_week TEXT,
                day_of_month TEXT,
                history_enabled INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
            );

            CREATE TABLE IF NOT EXISTS history_backups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                backup_id INTEGER NOT NULL,
                backup_name TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
                FOREIGN KEY (backup_id)
                    REFERENCES backups(id)
                    ON DELETE CASCADE
            );
            """)

            connection.commit()
            print("Base de datos y tablas creadas correctamente")


db = DatabaseService()
