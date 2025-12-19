-- task
INSERT INTO second_table
VALUES (AVG(SELECT * FROM second_table))
