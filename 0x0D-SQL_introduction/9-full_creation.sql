-- A script that creates a table `second_table` in the database `hbtn_0d_usa`.
CREATE TABLE second_table (id INT, name VARCHAR(256), score INT) IF NOT EXISTS;
INSERT INTO second_table (id, name, score)
VALUES (1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8);
