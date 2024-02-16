-- A script that lists all the cities of California from the database hbtn_0d_usa
SELECT cities.id,
	cities.name
WHERE cities.state_id = (
		SELECT id
		FROM states
		WHERE name = 'California'
	);