class Song:
    # --- Class Attributes ---
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    # --- Constructor ---
    # Make sure this has TWO underscores on both sides: __init__
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Call the tracking methods
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)