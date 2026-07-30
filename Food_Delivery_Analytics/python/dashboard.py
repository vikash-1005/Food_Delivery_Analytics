import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("../data/food_delivery.db")

# -----------------------------
# Restaurant Revenue
# -----------------------------
revenue_query = """
SELECT
    r.restaurant_name,
    SUM(o.order_amount) AS revenue
FROM restaurants r
JOIN orders o
ON r.restaurant_id = o.restaurant_id
GROUP BY r.restaurant_name
ORDER BY revenue DESC
"""

revenue_df = pd.read_sql_query(revenue_query, conn)

plt.figure(figsize=(8,5))
plt.bar(revenue_df["restaurant_name"], revenue_df["revenue"])
plt.title("Restaurant Revenue Analysis")
plt.xlabel("Restaurant")
plt.ylabel("Revenue")
plt.show()

# -----------------------------
# Peak Hour Demand
# -----------------------------
peak_query = """
SELECT
    strftime('%H', order_date) AS hour,
    COUNT(*) AS total_orders
FROM orders
GROUP BY hour
ORDER BY hour
"""

peak_df = pd.read_sql_query(peak_query, conn)

plt.figure(figsize=(8,5))
plt.bar(peak_df["hour"], peak_df["total_orders"])
plt.title("Peak Hour Demand")
plt.xlabel("Hour")
plt.ylabel("Orders")
plt.show()

# -----------------------------
# Customer Retention
# -----------------------------
retention_query = """
SELECT
    customer_id,
    COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id
ORDER BY total_orders DESC
"""

retention_df = pd.read_sql_query(retention_query, conn)

plt.figure(figsize=(8,5))
plt.bar(retention_df["customer_id"].astype(str),
        retention_df["total_orders"])
plt.title("Customer Retention")
plt.xlabel("Customer ID")
plt.ylabel("Number of Orders")
plt.show()

conn.close()