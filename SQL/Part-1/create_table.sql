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





    
    
	