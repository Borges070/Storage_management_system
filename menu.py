
class Menu:
    def __init__(self, item_manager):
        self.item_manager = item_manager

    def display_menu(self):
        while True:
            print("=====================")
            print("\n Borges Amazing Storage House ")
            print("1. Add Item")
            print("2. View Items")
            print("3. Update Item")
            print("4. Delete Item")
            print("5. Exit")
            
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                try:
                    name = (input("Enter item name: ")).strip().upper()
                    if len(name) < 1:
                        raise ValueError("Item name cannot be empty.")
                    
                     

                    self.item_manager.add_item(name)
                except ValueError:
                    print("Invalid input. Please enter valid data types.")
            
            elif choice == 2:
                self.item_manager.view_items()
            
            elif choice == 3:
                try:
                    self.item_manager.view_items()
                    item_id = int(input("Enter item ID to update: "))
                    
                    self.item_manager.update_item(item_id)
                except ValueError:
                    print("Invalid input. Please enter valid data types.")
            
            elif choice == 4:
                try:
                    item_id = int(input("Enter item ID to delete: "))
                    self.item_manager.delete_item(item_id)
                except ValueError:
                    print("Invalid input. Please enter valid data types.")
            
            elif choice == 5:
                print("Exiting...")
                break
            
            else:
                print("Invalid choice. Please try again.")