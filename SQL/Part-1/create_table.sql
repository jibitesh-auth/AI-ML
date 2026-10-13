USE instagram;

CREATE TABLE user (
	id INT /* PRIMARY KEY */,
    age INT,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(50) UNIQUE,
    followers INT DEFAULT 0,
    following INT DEFAULT 0
    CONSTRAINT age_check CHECK(age >= 13),
    PRIMARY KEY(id)
);
    
	