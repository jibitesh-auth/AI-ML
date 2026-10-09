CREATE DATABASE college;

create database xyz_company;

DROP DATABASE xyz_company;

USE college;

-- Create Table
CREATE TABLE student(
	rollno 	INT,
    name VARCHAR(30),
    age int
);

-- Insert into Table
INSERT INTO student
VALUES
(101, "adam", 12),
(102, "bob", 14);

-- Display Table
SELECT * FROM student;