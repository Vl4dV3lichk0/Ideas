from src.database.crud import *
from src.database.models import *
from typing import Optional

class CategoryService:
    """Category services"""

    @staticmethod
    def add_category(name: str) -> tuple[bool, str, Optional[Category]]:
        """
        Docstring for add_category
        
        :param name: len > 2, not None
        :type name: str
        :return: False if name is None + message + None, True + message + Category object
        :rtype: tuple[bool, str, Category | None]
        """

        # Validation
        if not name or len(name) < 3:
            return False, "Name is too short.", None
        
        category = CategoryCRUD.create_category(name)

        if not category:
            return False, "This category does already exist.", None
        
        return True, "Category is successfuly created.", category
    
    @staticmethod
    def get_category(id: int) -> Optional[Category]:
        """
        Docstring for get_category
        
        :param id: identifier
        :type id: int
        :return: category
        :rtype: dict | None
        """

        category = CategoryCRUD.get_category_by_id(id)

        if not category:
            return None
        
        return category
    
    @staticmethod
    def update_category(id: int, **kwargs) -> tuple[bool, str, Optional[Category]]:
        """
        Docstring for update_category
        
        :param id: identifier
        :type id: int
        :**kwargs:
        :    name: str
        :**kwargs:
        :    name: str
        :return: False if name is None + message + None, True + message + Category object
        :rtype: tuple[bool, str, Category]
        """
        category = CategoryCRUD.get_category_by_id(id)
        
        if not category:
            return False, "This category does not exist.", None
        
        if CategoryCRUD.update_category(id, **kwargs):
            return True, "Category is successfuly updated.", category
        else:
            return False, "Category is not updated.", None
        
class IdeaService:
    """Idea services"""

    @staticmethod
    def add_idea(name: str, category_id: Optional[int], priority: Optional[int], about: Optional[str], created_at: Optional[str]) -> tuple[bool, str, Optional[Idea]]:
        """
        Docstring for add_idea
        
        :param name: len > 2, not None
        :type name: str
        :param priority (1-5)
        :typepriority: int
        :return: False if name is None + message + None, True + message + Idea object
        :rtype: tuple[bool, str, Idea | None]
        """

        # Validation
        if not name or len(name) < 3:
            return False, "Name is too short.", None
        if priority and priority not in [1, 2, 3, 4, 5]:
            return False, "Priority must be from 1 to 5.", None
        
        idea = IdeaCRUD.create_idea(name, category_id, priority, about, created_at)

        if not idea:
            return False, "This idea does already exist.", None
        
        return True, "Idea is successfuly created.", idea
    
    @staticmethod
    def get_idea(id: int) -> Optional[Idea]:
        """
        Docstring for get_idea
        
        :param id: identifier
        :type id: int
        :return: idea
        :rtype: dict | None
        """

        idea = IdeaCRUD.get_idea_by_id(id)

        if not idea:
            return None
        
        return idea
    
    @staticmethod
    def update_idea(id: int, **kwargs) -> Optional[Idea]:
        """
        Docstring for update_idea
        
        :param id: identifier
        :type id: int
        :**kwargs:
        :   name: str
        :   category_id: int
        :   priority: int
        :   about: str
        :   created_at: str
        :return: False if name is None + message + None, True + message + Category object
        :rtype: tuple[bool, str, Category]
        """
        idea = IdeaCRUD.get_idea_by_id(id)
        
        if not idea:
            return False, "This idea does not exist.", None
        
        if IdeaCRUD.update_idea(id, **kwargs):
            return True, "Idea is successfuly updated.", idea
        else:
            return False, "Idea is not updated.", None