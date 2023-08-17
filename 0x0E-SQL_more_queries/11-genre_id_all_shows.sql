-- lists all shows contained in the database hbtn_0d_tvshows.
SELECT s.title, g.genre_id
FROM tv_show_genres g
RIGHT JOIN tv_shows s
	ON g.show_id = s.id
ORDER BY s.title, g.genre_id;
