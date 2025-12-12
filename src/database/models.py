# Models file
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Category:
    """Category model"""
    id: Optional[int] = None
    name: str = ""

    @classmethod
    def from_row(cls, row: dict) -> 'Category':
        """Creating Category object from a database row"""
        return cls(
            id=row['id'],
            name=row['name']
        )


@dataclass
class Idea:
    """Idea model"""
    id: Optional[int] = None
    name: str = ""
    category_id: int = None
    priority: int = None
    about: str = ""
    creation_date: datetime = None

    @classmethod
    def from_row(cls, row: dict) -> 'Idea':
        """Creating Idea object from a database row"""
        return cls(
            id=row['id'],
            name=row['name'],
            category_id=row['category_id'],
            priority=row['priority'],
            about=row['about'],
            creation_date=row['creation_date']
        )