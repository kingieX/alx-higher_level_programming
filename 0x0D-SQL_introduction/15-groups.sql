-- Lists the number of records with the same score in the table in desc count.
-- The result display the score, number of record and label number.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
