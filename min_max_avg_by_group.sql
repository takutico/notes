-- Table: product
-- Colums: id, name, price, type

SELECT type, MIN(price) 
FROM product 
GROUP BY type


SELECT type, MAX(price) 
FROM product 
GROUP BY type


SELECT type, AVG(price) 
FROM product 
GROUP BY type