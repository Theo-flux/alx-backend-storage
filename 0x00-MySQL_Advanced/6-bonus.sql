-- script that creates a stored procedure AddBonus
-- that adds a new correction for a student.
DELIMITER $$
CREATE PROCEDURE AddBonus(
	IN user_id INTEGER,
	IN project_name VARCHAR(255),
	IN score INTEGER
)
BEGIN
	DECLARE pro_id INTEGER;
	SELECT `id` INTO pro_id FROM `projects`
	WHERE `name` = project_name;

	IF pro_id IS NULL THEN
		INSERT INTO `projects`(name) VALUES(project_name);
		SELECT `id` INTO pro_id FROM `projects`
		WHERE `name` = project_name;
	END IF;

	INSERT INTO `corrections` (user_id, project_id, score)
	VALUES(user_id, pro_id, score); 	
END$$
DELIMITER ;
