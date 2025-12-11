# Connection file
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

class DatabaseConnection:
    """Database connection manager"""

    def __init__(self, db_path: str = "data/database.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(exist_ok=True)

    @contextmanager
    def get_connection(self) -> Iterator[sqlite3.Connection]:
        """Database context manager"""

        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row # return strings as dictionaries
            yield conn
            conn.commit()
        except sqlite3.Error as e:
            if conn:
                conn.rollback()
            raise e
        finally:
            if conn:
                conn.close()

db = DatabaseConnection()