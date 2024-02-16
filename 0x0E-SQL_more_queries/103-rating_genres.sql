-- A script that lists all genres from the database `hbtn_0d_tvshows_rate` and their rating
SELECT `genres`.`name`,
	`ratings`.`rating`
FROM `genres`
	JOIN `ratings` ON `genres`.`id` = `ratings`.`genre_id`
ORDER BY `genres`.`name`;