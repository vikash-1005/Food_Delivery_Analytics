SELECT
    customer_id,
    SUM(order_amount) AS total_spending,

    RANK() OVER(
        ORDER BY SUM(order_amount) DESC
    ) AS customer_rank

FROM orders
GROUP BY customer_id;