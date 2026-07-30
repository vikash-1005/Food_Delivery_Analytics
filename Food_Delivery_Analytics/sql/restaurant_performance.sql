SELECT
    r.restaurant_name,
    SUM(o.order_amount) AS revenue
FROM restaurants r
JOIN orders o
    ON r.restaurant_id = o.restaurant_id
GROUP BY r.restaurant_name
ORDER BY revenue DESC;