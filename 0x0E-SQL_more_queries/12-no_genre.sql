-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT s.title, g.genre_id
FROM tv_show_genres g
RIGHT JOIN tv_shows s
	ON g.show_id = s.id
WHERE g.genre_id IS NULL
ORDER BY s.title, g.genre_id;
