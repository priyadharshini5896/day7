import sqlite3

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
""")

sample_data = [
    ('Apple', 10, 0.5),
    ('Banana', 20, 0.3),
    ('Orange', 15, 0.4),
    ('Apple', 5, 0.5),
    ('Banana', 10, 0.3),
    ('Orange', 5, 0.4)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)

conn.commit()
conn.close()

print(" sales_data.db created and populated with sample data.")
