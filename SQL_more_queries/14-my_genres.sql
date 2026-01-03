-- TASK
SELECT tv_genres.name
FROM tv_genres
JOIN tv_shows ON tv_show.id = tv_genres.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name ASC
