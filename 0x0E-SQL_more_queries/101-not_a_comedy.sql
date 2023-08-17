-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT s.title
FROM tv_shows s
LEFT JOIN tv_show_genres sg
	ON s.id = sg.show_id
LEFT JOIN tv_genres g
	ON g.id = sg.genre_id
WHERE s.id NOT IN (
	SELECT sg.show_id
	FROM tv_show_genres sg
	JOIN tv_genres g
		ON sg.genre_id = g.id
	WHERE g.name = 'Comedy')
ORDER BY s.title
