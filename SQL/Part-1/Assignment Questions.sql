USE college;
CREATE TABLE Employee(
	EmpID INT PRIMARY KEY,
    FirstName VARCHAR(10),
    LastName VARCHAR(10),
    Department VARCHAR(10),
    Salary INT,
    HireDate DATE
);

INSERT INTO Employee
(EmpID, FirstName, LastName, Department, Salary, HireDate)
VALUES
(101, 'Alice', 'Johnson', 'IT', 6500, '2020-03-15'),
(102, 'Mark', 'Rivera', 'HR', 4800, '2019-07-22'),
(103, 'Sophia', 'Lee', 'Finance', 7200, '2021-01-10'),
(104, 'Daniel', 'Kim', 'IT', 5800, '2018-11-05'),
(105, 'Emma', 'Brown', 'Marketing', 5300, '2022-04-18'),
(106, 'Liam', 'Patel', 'Finance', 6900, '2020-09-29'),
(107, 'Olivia', 'Garcia', 'HR', 4600, '2017-06-30'),
(108, 'Noah', 'Thompson', 'IT', 7500, '2023-02-12'),
(109, 'Ava', 'Martinez', 'Marketing', 5100, '2019-12-02'),
(110, 'Ethan', 'Davis', 'Finance', 8000, '2016-05-14');


-- 1)
SELECT * FROM Employee;

-- 2)
SELECT FirstName,LastName,Salary
FROM Employee;

-- 3)
SELECT *
FROM Employee
WHERE Department = 'IT';

-- 4)
SELECT *
FROM Employee
WHERE salary > 6000;

-- 5) 
SELECT *
FROM Employee
ORDER BY HireDate DESC;

-- 6)
SELECT DISTINCT Department
FROM Employee;

-- 7)
SELECT * 
FROM Employee
WHERE FirstName Like 'A%';

-- 8)
SELECT *
FROM Employee
WHERE salary BETWEEN 4000 AND 7000;

-- 9)
SELECT avg(salary)
FROM Employee;

-- 10)
SELECT Department, COUNT(EmpID)
FROM Employee
GROUP BY Department
HAVING COUNT(EmpID) > 3;

