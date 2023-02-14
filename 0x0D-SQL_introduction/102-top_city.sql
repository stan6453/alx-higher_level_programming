-- Some comment

SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month BETWEEN 7 AND 8
ORDER BY AVG(value) DESC LIMIT 3;
