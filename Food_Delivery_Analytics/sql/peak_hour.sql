SELECT
    strftime('%H', order_date) AS hour,
    COUNT(*) AS total_orders
FROM orders
GROUP BY hour
ORDER BY total_orders DESC;