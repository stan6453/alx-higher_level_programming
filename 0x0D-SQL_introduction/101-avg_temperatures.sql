-- Some comment

SELECT city, AVG(value) FROM temperatures
ORDER BY value DESC
GROUP BY city;
