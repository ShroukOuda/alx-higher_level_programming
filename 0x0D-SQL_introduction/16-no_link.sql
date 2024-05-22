-- list score, name order by desc
SELECT score, name FROM second_table WHERE name != '' OR name IS NOT NULL ORDER BY score DESC;

