import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
              CREATE TABLE IF NOT EXISTS mouse_data (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT NOT NULL,
                  x INTEGER NOT NULL,
                  y INTEGER NOT NULL,
                  image_path TEXT NOT NULL
              )
              ''')
    conn.commit()
    conn.close()
    print("Database initialized.")

def save_to_db(timestamp, x, y, image_path):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO mouse_data (timestamp, x, y, image_path) VALUES (?, ?, ?, ?)",
              (timestamp, x, y, image_path))
    conn.commit()
    conn.close()
