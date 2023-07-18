-- create stored procedure to compute the average weighted score
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
	IN user_id INTEGER
)
BEGIN
	DECLARE weight_score INTEGER;
	DECLARE total_weight INTEGER;

	CREATE VIEW UCP AS
	SELECT users.id AS id, corrections.score AS score,
	projects.weight AS weight FROM corrections
	INNER JOIN users ON corrections.user_id = users.id
	INNER JOIN projects ON corrections.project_id = projects.id;

	SELECT SUM(score * weight) INTO weight_score
	FROM UCP WHERE UCP.id = user_id;

	SELECT SUM(weight) INTO total_weight
	FROM UCP WHERE UCP.id = user_id;

	UPDATE users SET average_score = weight_score / total_weight
	WHERE users.id = user_id;

	DROP VIEW UCP;
END$$
DELIMITER ;

