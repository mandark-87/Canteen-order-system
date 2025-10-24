from app import create_app
import sqlite3
from config import Config

def init_sqlite_db():
    conn = sqlite3.connect(Config.SQLITE_DB_PATH)
    c = conn.cursor()

    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS menu_items
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  price REAL NOT NULL,
                  category TEXT,
                  available BOOLEAN DEFAULT TRUE)''')

    # Check if available column exists, if not add it
    try:
        c.execute("SELECT available FROM menu_items LIMIT 1")
    except sqlite3.OperationalError:
        # Column doesn't exist, add it
        c.execute("ALTER TABLE menu_items ADD COLUMN available BOOLEAN DEFAULT TRUE")
        print("✅ Added 'available' column to menu_items table")

    c.execute('''CREATE TABLE IF NOT EXISTS orders
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  items TEXT NOT NULL,
                  total REAL NOT NULL,
                  token INTEGER NOT NULL,
                  status TEXT DEFAULT 'pending',
                  customer_name TEXT,
                  customer_phone TEXT,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")

app = create_app()

if __name__ == '__main__':
    # Initialize database BEFORE running the app
    #init_sqlite_db()
    app.run(debug=True, host='127.0.0.1', port=5000)