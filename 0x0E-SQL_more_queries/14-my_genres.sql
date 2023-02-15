-- lists all genres of the show Dexter
SELECT DISTINCT tv_genres.name FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter"
GROUP BY tv_genres.name;
