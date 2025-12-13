from database.crud import *
from database.models import *
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