-- A script that lists all shows contained in the database `hbtn_0d_tvshows` that have at least one genre linked
SELECT `tv_shows`.`title`,
	`tv_show_genres`.`genre_id`
FROM `tv_shows`
	JOIN `tv_show_genres` ON `tv_shows`.`id` = `tv_show_genres`.`tv_show_id`
	AND `tv_show_genres`.`genre_id` IS NOT NULL
ORDER BY `tv_shows`.`id`;