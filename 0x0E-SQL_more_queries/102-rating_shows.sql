-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT
	s.title,
	SUM(rate) AS rating
FROM tv_shows s
JOIN tv_show_ratings r
	ON s.id = r.show_id
GROUP BY r.show_id
ORDER BY rating DESC
