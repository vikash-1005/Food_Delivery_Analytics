WITH customer_spend AS
(
    SELECT
        customer_id,
        SUM(order_amount) AS total_spending
    FROM orders
    GROUP BY customer_id
)

SELECT *
FROM customer_spend
ORDER BY total_spending DESC;