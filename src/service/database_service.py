import sqlite3
from pathlib import Path
from model.backup_model import BackupModel
from model.history_backup_model import HistoryBackupModel


class DatabaseService:
    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent
        db_dir = base_dir / "db"
        db_dir.mkdir(exist_ok=True)

        self.DB = db_dir / "database.sqlite3"
        self._create_tables()

    def _get_connection(self):
        conn = sqlite3.connect(self.DB)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn


    def _create_tables(self):
        with self._get_connection() as connection:
            connection.executescript("""
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

    def get_all_backups(self):
        try:
            with self._get_connection() as connection:
                cursor = connection.cursor()
                rows = cursor.execute("SELECT * FROM backups").fetchall()
                return [dict(row) for row in rows]

        except Exception as e:
            raise ValueError(f"Hubo un error obteniendo los backups", e)

    def get_backup_by_id(self, backup_id: int):
        try:
            with self._get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute(
                    "SELECT * FROM backups WHERE id = ?",
                    (backup_id,)
                )
                return cursor.fetchone()
        
        except Exception as e:
            raise ValueError(
                f"Hubo un error obteniendo el backup {backup_id}", e
            )

    def add_backup(self, backup: BackupModel):
        try:
            with self._get_connection() as connection:
                cursor = connection.cursor()

                cursor.execute("""
                INSERT INTO backups (
                    name,
                    backup_path,
                    destination_path,
                    frequency,
                    time,
                    day_of_week,
                    day_of_month,
                    history_enabled
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    backup.name,
                    backup.backup_path,
                    backup.destination_path,
                    backup.frequency,
                    backup.time,
                    backup.day_of_week,
                    backup.day_of_month,
                    int(backup.history_enabled)
                ))

                connection.commit()
        
        except Exception as e:
            raise ValueError(f"Hubo un error creando el backup", e)
    
    def update_backup_by_id(self, backup: BackupModel):
        try:
            with self._get_connection() as connection:
                cursor = connection.cursor()

                cursor.execute("""
                UPDATE backups
                SET
                    name = ?,
                    backup_path = ?,
                    destination_path = ?,
                    frequency = ?,
                    time = ?,
                    day_of_week = ?,
                    day_of_month = ?,
                    history_enabled = ?
                WHERE id = ?
                """, (
                    backup.name,
                    backup.backup_path,
                    backup.destination_path,
                    backup.frequency,
                    backup.time,
                    backup.day_of_week,
                    backup.day_of_month,
                    int(backup.history_enabled),
                    backup.id
                ))

                if cursor.rowcount == 0:
                    raise ValueError(f"No existe un backup con id {backup.id}")
                
                connection.commit()
        
        except Exception as e:
            raise ValueError(f"Hubo un error actualizando el backup", e)

    def delete_backup_by_id(self, backup_id: int):
        try:
            with self._get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute(
                    "DELETE FROM backups WHERE id = ?", 
                    (backup_id,)
                )

                if cursor.rowcount == 0:
                    raise ValueError(f"No existe un backup con id {backup_id}")

                connection.commit()
        
        except Exception as e:
            raise ValueError(f"Hubo un error eliminando el backup", e)
        
    # methods for history_backup
    def get_all_history_backups(self):
        try:
            with self._get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    SELECT * FROM history_backups
                    ORDER BY created_at DESC
                """)
                return cursor.fetchall()

        except Exception as e:
            raise ValueError(
                "Hubo un error obteniendo el historial de backups", e
            )

    def get_history_by_backup_id(self, backup_id: int):
        try:
            with self._get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    SELECT * FROM history_backups
                    WHERE backup_id = ?
                    ORDER BY created_at DESC
                """, (backup_id,))
                return cursor.fetchall()

        except Exception as e:
            raise ValueError(
                f"Hubo un error obteniendo el historial del backup {backup_id}", e
            )

    def add_history_backup(self, history: HistoryBackupModel):
        try:
            with self._get_connection() as connection:
                cursor = connection.cursor()

                cursor.execute("""
                    INSERT INTO history_backups (
                        backup_id,
                        backup_name
                    ) VALUES (?, ?)
                """, (
                    history.backup_id,
                    history.backup_name
                ))

                connection.commit()

        except Exception as e:
            raise ValueError(
                "Hubo un error creando el historial del backup", e
            )

    def delete_history_by_id(self, history_id: int):
        try:
            with self._get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute(
                    "DELETE FROM history_backups WHERE id = ?",
                    (history_id,)
                )

                if cursor.rowcount == 0:
                    raise ValueError(
                        f"No existe un historial con id {history_id}"
                    )

                connection.commit()

        except Exception as e:
            raise ValueError(
                "Hubo un error eliminando el historial", e
            )
