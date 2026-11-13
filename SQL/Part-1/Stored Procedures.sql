USE prime;
DELIMITER $$

CREATE PROCEDURE check_balance(IN acc_id INT)
BEGIN
	SELECT balance
    FROM accounts
    WHERE id = acc_id; 
END $$

DELIMITER ;

CALL check_balance(2);
DROP PROCEDURE IF EXISTS check_balance;

-- When we want to store our output in a variable and manually display it
DELIMITER $$
CREATE PROCEDURE check_balance1(IN acc_id INT, OUT bal DECIMAL(10,2))
BEGIN
	SELECT BALANCE INTO bal
    FROM accounts
    WHERE id = acc_id;
END $$
DELIMITER ;   

CALL check_balance1(1, @balance);
SELECT @balance; 

SELECT * FROM accounts;