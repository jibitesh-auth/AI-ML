USE instagram;

-- USER TABLE
CREATE TABLE user (
	id INT /* PRIMARY KEY */,
    age INT,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(50) UNIQUE,
    followers INT DEFAULT 0,
    following INT DEFAULT 0,
    CONSTRAINT age_check CHECK(age >= 13),
    PRIMARY KEY(id)
);

/*
INSERT INTO user
(id, age, name)
VALUES
(2,20,"random");  -- [Error]Duplicate Entry->PRIMARY KEY
*/

/*
INSERT INTO user
(id, age)
VALUES
(2,20);  -- [Error]NULL
*/

/*
INSERT INTO user
(id, age, name,email)
VALUES
(10,20,"random","bear@yahoo.in");  -- [Error]Duplicate Entry-> email(unique)
*/

/*
INSERT INTO user
(id, age, name)
VALUES
(2,10,"random");  -- [Error]age constraint
*/


INSERT INTO user
(id, age, name, email, followers, following)
VALUES
(1,14,"adam","adam@yahoo.in",123,125),
(2,18,"bob","bob@yahoo.in",150,125),
(3,21,"bear","bear@yahoo.in",2000,125),
(4,20,"gorilla","gorilla@yahoo.in",1000,125);

SELECT id,age FROM user;
SELECT * FROM user;
SELECT DISTINCT age FROM user;

SELECT *
FROM user
WHERE followers >= 200;

SELECT name,followers
FROM user
WHERE followers >= 200;


SELECT name, age, followers
FROM user
WHERE age < 16;

SELECT name,age
FROM user
WHERE age+1=19;

SELECT name,age,followers
FROM user
WHERE age > 15 AND followers > 200;

SELECT name,followers
FROM user
WHERE age > 15 OR followers > 200;

SELECT name,age
FROM user
WHERE age BETWEEN 15 AND 18;

SELECT name, age,followers,email
FROM user
WHERE email IN ("adam@yahoo.in","gorilla@gmail.com","bear@yahoo.in");

INSERT INTO user
(id, age, name, email, followers, following)
VALUES
(5, 14, "eve","eve@yahoo.in",123,145),
(6, 16, "farah", "farah@gmail.com",1000, 1000);

SELECT name, followers, email
FROM user
WHERE age IN (14, 16);

SELECT name, followers, email
FROM user
WHERE age NOT IN (14,16);

-- Limit Clause
SELECT name,age,email
FROM user
WHERE age > 15
LIMIT 2;

SELECT name, age, email
FROM user
LIMIT 3;

-- ORDER BY
SELECT name,age,followers
FROM user
ORDER BY followers ASC;

SELECT name,age,followers
FROM user
ORDER BY followers DESC;

SELECT name,age,followers
FROM user
ORDER BY followers;

-- Aggregate Funtions
SELECT max(followers)
FROM user;

SELECT max(age)
FROM user;

SELECT count(age)
FROM user
WHERE age = 14;

SELECT min(age)
FROM user;

SELECT avg(age)
FROM user;

SELECT sum(followers)
FROM user;

-- Group By
SELECT age,COUNT(id)
FROM user
GROUP BY age;

SELECT age,max(followers)
FROM user
GROUP BY age;

/*
SELECT name,age,max(followers)
FROM user
GROUP BY age;  -- Error
*/
-- We can't put extra coloumn except the column used for [GROUP BY]
-- We can put extra column inside aggregate function

SELECT age, max(followers),min(name)
FROM user
GROUP BY age;

-- Having Clause
SELECT age,max(followers)
FROM user
GROUP BY age
HAVING max(followers) > 200
ORDER BY age ASC;

-- UPDATE
UPDATE user
SET followers = 10000009
WHERE age = 16;

SET SQL_SAFE_UPDATES = 0;

SELECT *
FROM user;

-- DELETE
DELETE FROM user
WHERE age = 14;

SELECT * FROM user;









-- POST TABLE
CREATE TABLE post (
	id INT PRIMARY KEY,
    content VARCHAR(100),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

INSERT INTO post
(id, content, user_id)
VALUES
(101, "Hello World", 3),
(102, "Bye Bye", 1),
(103, "Hello Delta", 3);

SELECT * FROM post





    
    
	