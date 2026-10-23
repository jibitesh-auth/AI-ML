/*
Q. Create a table to store student info (roll_no, name, city, marks).

Insert the following data into the table:

110, "adam", "Delhi", 76
108, "bob", "Mumbai", 65
124, "casey", "Pune", 94
112, "duke", "Pune", 80

Practice Questions:
1. Select all students who scored 75+.
2. Find names of all cities where students are from.
3. Find the maximum marks of students from each city.
4. Find the average marks of the class.
5. Add a new column `grade` and assign grades such that:
   - Marks > 80       -> Grade = 'O'
   - Marks 70 to 80   -> Grade = 'A'
   - Marks 60 to 70   -> Grade = 'B'
*/

Use college;
CREATE TABLE student_info(
	roll_no INT PRIMARY KEY,
    name VARCHAR(30),
    city VARCHAR(30),
    marks INT
);

INSERT INTO student_info
(roll_no,name,city,marks)
VALUES
(110,"adam","Delhi",76),
(108,"bob","Mumbai",65),
(124,"casey","Pune",94),
(112,"duke","Pune",80);

SELECT * FROM student_info;

-- 1)
SELECT *
FROM student_info
WHERE marks > 75;

-- 2)
SELECT DISTINCT city
FROM student_info;

-- 3)
SELECT city,max(marks)
FROM student_info
GROUP BY city;

-- 4)
SELECT avg(marks)
FROM student_info;

-- 5)
ALTER TABLE student_info
ADD COLUMN grade VARCHAR(1);

SELECT * FROM student_info;

UPDATE student_info
SET grade = "O"
WHERE marks >= 80;

UPDATE student_info
SET grade = "A"
WHERE marks >= 70 AND marks < 80;

UPDATE student_info
SET grade = "B"
WHERE marks >= 60 AND marks < 70;

SET SQL_SAFE_UPDATES = 0;


