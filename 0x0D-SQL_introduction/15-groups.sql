--lists the number of records with the same score in the table second_table of the database hbtn_0c_0

SELECT DISTINCT score, COUNT(DISTINCT score) AS number FROM hbtn_0c_0.second_table;
