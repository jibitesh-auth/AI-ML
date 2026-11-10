USE prime;

ALTER TABLE accounts
ADD COLUMN branch VARCHAR(50);

UPDATE accounts
SET branch = "Mumbai"
WHERE id = 1;

UPDATE accounts
SET branch = "Delhi"
WHERE id = 2;

UPDATE accounts
SET branch = "Bangalore"
WHERE id = 3;

INSERT INTO accounts VALUES
(4, "David", 1000.00, 'Noida');

SELECT * FROM accounts;

-- Index
CREATE INDEX idx_branch ON accounts(branch);
SHOW INDEX FROM accounts;

-- It will become way more faster --
SELECT *
FROM accounts
WHERE branch = "Mumbai";

DROP INDEX idx_branch ON accounts;

-- Composite Index
CREATE INDEX idx2 ON accounts(branch,balance);
SHOW INDEX FROM accounts;




