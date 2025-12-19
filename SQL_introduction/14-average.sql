-- task
INSERT INTO second_table
VALUES (AVG(SELECT score FROM second_table))
