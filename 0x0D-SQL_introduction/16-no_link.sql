--  lists all records of the table second_table of a database except rows without a name value
SELECT `score`, `name` FROM second_table WHERE `name` IS NOT NULL ORDER BY `score` DESC;
