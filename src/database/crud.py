# CRUD file
from .connection import db
from .models import Category, Idea
import sqlite3
from typing import List, Optional

class CategoryCRUD:
    """CRUD operations for categories"""

    @staticmethod
    def init_db():
        """Tables initialisation"""
        with db.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS Categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS Ideas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    category_id INTEGER,
                    priority INTEGER,
                    about TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    CONSTRAINT fk_category_id FOREIGN KEY (category_id) REFERENCES Categories (id),
                    ON DELETE SET NULL,
                    ON UPDATE CASCADE
                )
            """)
    
    @staticmethod
    def create_category(name: str) -> Optional[Category]:
        """Category creation"""

        # Validation
        if not name or len(name.strip()) == 0:
            return None

        with db.get_connection() as conn:
            cursor = conn.cursor()
            
            try:
                cursor.execute(
                    "INSERT INTO Categories (name) VALUES (?)",
                    (name,)
                )
                category_id = cursor.lastrowid
                if not category_id:
                    raise sqlite3.IntegrityError
                return CategoryCRUD.get_category_by_id(category_id)
            except sqlite3.IntegrityError as e:
                print(f"IntegrityError: {e}")
                return None
            except sqlite3.Error as e:
                print(f"Database error: {e}")
                return None
    
    @staticmethod
    def get_category_by_id(category_id: int) -> Optional[Category]:
        """Get category by ID"""
        with db.get_connection() as conn:
            cursor = conn.execute(
                "SELECT * FROM Categories WHERE id = ?",
                (category_id,)
            )
            row = cursor.fetchone()
            return Category.from_row(dict(row)) if row else None
    
    @staticmethod
    def get_all_categories() -> List[Category]:
        """Get all categories"""
        with db.get_connection() as conn:
            cursor = conn.execute(
                "SELECT * FROM Categories"
            )
            return [Category.from_row(dict(row)) for row in cursor.fetchall()]
        
    @staticmethod
    def update_category(category_id, **kwargs) -> bool:
        """Category update"""
        allowed_fields = {'name'}
        updates = {k: v for k, v in kwargs.items() if k in allowed_fields}

        if not updates:
            return False
        
        set_clause = ", ".join(f"{field} = ?" for field in updates.keys())
        values = list(updates.values())
        values.append(category_id)

        with db.get_connection() as conn:
            cursor = conn.execute(
                f"UPDATE Categories SET {set_clause} WHERE id = ?",
                tuple(values)
            )
            return cursor.rowcount > 0
        
    @staticmethod
    def delete_category(category_id: int) -> bool:
        """Category deletion"""
        with db.get_connection() as conn:
            cursor = conn.execute(
                "DELETE FROM Categories WHERE id = ?",
                (category_id,)
            )
            return cursor.rowcount > 0

class IdeaCRUD:
    """CRUD operations for ideas"""
    
    @staticmethod
    def create_idea(name: str, category_id: int, priority: int, about: str, created_at: Optional[str]) -> Optional[Idea]:
        """Idea creation"""
        with db.get_connection() as conn:
            cursor = conn.cursor()
            
            try:
                if created_at:
                    cursor.execute(
                        "INSERT INTO Ideas (name, category_id, priority, about, created_at) VALUES (?, ?, ?, ?, ?)",
                        (name, category_id, priority, about, created_at)
                    )
                else:
                    cursor.execute(
                        "INSERT INTO Ideas (name, category_id, priority, about) VALUES (?, ?, ?, ?)",
                        (name, category_id, priority, about, created_at)
                    )
                idea_id = cursor.lastrowid
                if not idea_id:
                    raise sqlite3.IntegrityError
                return IdeaCRUD.get_idea_by_id(idea_id)
            except sqlite3.IntegrityError as e:
                print(f"IntegrityError: {e}")
                return None
            except sqlite3.Error as e:
                print(f"Database error: {e}")
                return None
    
    @staticmethod
    def get_idea_by_id(idea_id: int) -> Optional[Idea]:
        """Get idea by ID"""
        with db.get_connection() as conn:
            cursor = conn.execute(
                "SELECT * FROM Ideas WHERE id = ?",
                (idea_id,)
            )
            row = cursor.fetchone()
            return Idea.from_row(dict(row)) if row else None
    
    @staticmethod
    def get_all_ideas() -> List[Idea]:
        """Get all ideas"""
        with db.get_connection() as conn:
            cursor = conn.execute(
                "SELECT * FROM Ideas"
            )
            return [Idea.from_row(dict(row)) for row in cursor.fetchall()]
        
    @staticmethod
    def update_idea(idea_id, **kwargs) -> bool:
        """Idea update"""
        allowed_fields = {'name', 'category_id', 'priority', 'about', 'created_at'}
        updates = {k: v for k, v in kwargs.items() if k in allowed_fields}

        if not updates:
            return False
        
        set_clause = ", ".join(f"{field} = ?" for field in updates.keys())
        values = list(updates.values())
        values.append(idea_id)

        with db.get_connection() as conn:
            cursor = conn.execute(
                f"UPDATE Ideas SET {set_clause} WHERE id = ?",
                tuple(values)
            )
            return cursor.rowcount > 0
        
    @staticmethod
    def delete_idea(idea_id: int) -> bool:
        """Idea deletion"""
        with db.get_connection() as conn:
            cursor = conn.execute(
                "DELETE FROM Ideas WHERE id = ?",
                (idea_id,)
            )
            return cursor.rowcount > 0