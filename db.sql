# Inner join
SELECT *
FROM table_A a
INNER JOIN table_B b
WHERE a.fk = b.id

# Left join
SELECT *
FROM left_table_a a
LEFT JOIN right_table_b b
WHERE a.fk = b.id

# Left outer join
SELECT *
FROM left_table a
LEFT OUTER JOIN right_table b
on a.fk = b.id
WHERE b.id is null;
