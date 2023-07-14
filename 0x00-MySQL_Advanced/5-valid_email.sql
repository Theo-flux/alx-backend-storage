-- Trigger that resets valid_email attribute when
-- the email has been changed
DELIMITER $$
CREATE TRIGGER `reset_valid_email`
BEFORE UPDATE
ON `users`
FOR EACH ROW
BEGIN
	IF NEW.EMAIL != OLD.EMAIL THEN
		SET NEW.VALID_EMAIL = 0;
	END IF;
END;
$$

