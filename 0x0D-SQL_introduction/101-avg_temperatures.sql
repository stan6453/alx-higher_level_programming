-- Some comment

SELECT city, AVG(value) FROM temperatures
GROUP BY city
ORDER BY value DESC;
