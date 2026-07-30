import sqlite3
import pandas as pd

conn = sqlite3.connect("../data/food_delivery.db")

query_file = input("Enter SQL file path: ")

with open(query_file, "r") as file:
    query = file.read()

df = pd.read_sql_query(query, conn)

print("\nResult:\n")
print(df)

conn.close()