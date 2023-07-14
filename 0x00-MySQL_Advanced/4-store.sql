-- SQL script that creates a trigger that decreases
-- the quantity of an item after adding a new order
DELIMITER $$
CREATE TRIGGER `decrease_qty_of_an_item`
AFTER INSERT
ON `orders`
FOR EACH ROW
BEGIN
	UPDATE `items` SET `quantity` = `quantity` - NEW.number
	WHERE `name` = NEW.item_name;
END;
$$

