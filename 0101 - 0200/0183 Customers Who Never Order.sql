SELECT c.name as Customers
FROM Customers c LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.customerId IS NULL
