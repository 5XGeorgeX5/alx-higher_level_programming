-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT s.title, g.genre_id
FROM tv_show_genres g
JOIN tv_shows s
	ON g.show_id = s.id
ORDER BY s.title, g.genre_id;
