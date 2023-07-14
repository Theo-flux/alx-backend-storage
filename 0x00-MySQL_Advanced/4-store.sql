-- SQL script that creates a trigger that decreases
-- the quantity of an item after adding a new order
DELIMITER $$
CREATE TRIGGER `holberton`.`decrease_qty_of_an_item`
AFTER INSERT
ON `holberton`.`orders`
FOR EACH ROW
BEGIN
	UPDATE `holberton`.`items` SET `items`.`quantity` = `items`.`quantity` -	NEW.NUMBER
	WHERE `items`.`name` = NEW.ITEM_NAME;
END;
$$

