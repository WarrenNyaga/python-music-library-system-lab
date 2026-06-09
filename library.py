class Song:
    # --- Class Attributes (Global State) ---
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    # --- Constructor ---
    def __init__(self, name, artist, genre):
        # Assign instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Automatically trigger the trackers every time a song is made
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    # --- Class Methods ---
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Ensure only unique genres are added
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Ensure only unique artists are added
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # If genre exists, increment. If not, initialize at 1.
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # If artist exists, increment. If not, initialize at 1.
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1