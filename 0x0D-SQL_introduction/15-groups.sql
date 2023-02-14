-- lists the number of records with the same score in

SELECT score, COUNT(score) AS number 
FROM second_table
GROUP BY score
ORDER BY number DESC;
