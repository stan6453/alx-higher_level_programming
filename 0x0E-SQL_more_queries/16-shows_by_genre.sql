-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT DISTINCT tv_shows.title, tv_genres.name FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_genres.name;
