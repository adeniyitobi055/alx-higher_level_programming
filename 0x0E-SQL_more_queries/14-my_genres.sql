-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- lists
SELECT name FROM tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_show.id WHERE tv_show.title = 'Dexter' GROUP BY name ORDER BY name ASC;
