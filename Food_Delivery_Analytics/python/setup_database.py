import sqlite3

conn = sqlite3.connect("../data/food_delivery.db")

cursor = conn.cursor()

# Create tables
with open("../sql/schema.sql", "r") as file:
    cursor.executescript(file.read())

# Insert data
with open("../sql/insert_data.sql", "r") as file:
    cursor.executescript(file.read())

conn.commit()
conn.close()

print("Database setup completed!")