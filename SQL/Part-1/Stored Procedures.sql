DELIMITER $$

CREATE PROCEDURE check_balance(IN acc_id INT)
BEGIN
	SELECT balance
    FROM accounts
    WHERE id = acc_id; 
END $$

DELIMITER ;

CALL check_balance(2);