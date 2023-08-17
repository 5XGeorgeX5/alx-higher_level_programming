-- lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT c.id, c.name
FROM cities c, states s
WHERE c.state_id = s.id AND s.name = 'California'
