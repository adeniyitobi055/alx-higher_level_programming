-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title, tv_shows_genres.genre_id FROM tv_show INNER JOIN tv_show_genre ON tv_shows.id = tv_shows_genre.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
