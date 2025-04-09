import sqlite3


class ItemManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_item(self, name):
        duplicate = self.db_manager.fetch_one('SELECT * FROM items WHERE name = ?', (name,))
        if duplicate:
            print(f"Error: Item with the same name already exists. {sqlite3.IntegrityError}. This item already exists" )    
            # This try method works to show the error, but the try method is accepted before the except method. 
        else:
            try:
                quantity = int(input("Enter item quantity: "))
                if quantity > 2**32 -1:
                    raise ValueError("Quantity exceeds maximum limit.")
                    
                price = float(input("Enter item price: "))
                self.db_manager.execute_query(
                    'INSERT INTO items (name, quantity, price) VALUES (?, ?, ?)',
                    (name, quantity, price)
                )
                print("Item added successfully!")
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter valid data types.")
            

    def view_items(self):
        items = self.db_manager.fetch_all('SELECT * FROM items')
        if items:
            for item in items:
                print(item)
        else:
            print("No items found in storage.")

    def update_item(self, item_id):
        item = self.db_manager.fetch_one('SELECT * FROM items WHERE id = ?', (item_id,))
        if item:
            print("Item found:", item)
            name = input("Enter new item name: ").strip().upper()
            quantity = int(input("Enter new item quantity: "))
            price = float(input("Enter new item price: "))
            self.db_manager.execute_query(
                'UPDATE items SET name = ?, quantity = ?, price = ? WHERE id = ?',
                (name, quantity, price, item_id)
            )
            print("Item updated successfully!")
        else:
            print("Error: Item with the provided ID not found.")

    def delete_item(self, item_id):
        item = self.db_manager.fetch_one('SELECT * FROM items WHERE id = ?', (item_id,))
        if item:
            print(f"Item found: {item}")
            self.db_manager.execute_query('DELETE FROM items WHERE id = ?', (item_id,))
            print(f"Item {item_id} deleted successfully!")
        else:
            print("Error: Item with the provided ID not found.")
