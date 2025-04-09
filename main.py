from database_manager import DatabaseManager
from item_manager import ItemManager
from menu import Menu

if __name__ == "__main__":
    db_manager = DatabaseManager('storage_management.db')
    item_manager = ItemManager(db_manager)
    menu = Menu(item_manager)
    menu.display_menu()
    db_manager.close_connection()