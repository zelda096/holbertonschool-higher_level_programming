-- list score and name and sort by score above 9

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
