import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            quantity INTEGER NOT NULL CHECK (quantity >= 0),
            price REAL NOT NULL
        )
        ''')
        self.conn.commit()
    
    def execute_query(self, query, params=()): # I am structuring a function to execute queries, so I can use it in all the CRUD functions
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Database Error: {e}")

    def fetch_all(self, query, params=()): #
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close_connection(self):
        self.conn.close()