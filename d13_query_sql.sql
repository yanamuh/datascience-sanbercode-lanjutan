SELECT a.Title, b.Name as Name, c.Name as track
FROM albums a
INNER JOIN tracks b ON a.AlbumId = b.AlbumId AND (b.AlbumId = 4 OR b.AlbumId = 5)
INNER JOIN artists c ON a.ArtistId = c.ArtistId AND (c.ArtistId = 1 OR c.ArtistId = 3);
