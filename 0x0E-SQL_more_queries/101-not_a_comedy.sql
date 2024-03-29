-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT DISTINCT tv_shows.title FROM tv_shows LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.show_id NOT IN (SELECT tv_shows.id FROM tv_shows
	JOIN  tv_show_genres ON tv_show_genres.show_id = tv_shows.id
	JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_genres.name="Comedy") 
OR tv_show_genres.genre_id IS NULL 
ORDER BY tv_shows.title;
