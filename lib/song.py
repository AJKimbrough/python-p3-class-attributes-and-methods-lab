import ipdb
class Song:

    count = 0
    genres = []
    artists = []
    add_song_to_count = 0
    genre_count = {}
    genre = []
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count += 1
        Song.count +=1
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        
    @classmethod
    def add_to_genres(cls, genre):
        if genre in cls.genre_count:
            #print(cls.genre_count)
            cls.genre_count[genre.genre] += 1 
        else:
            cls.genres.append(genre.genre)
            cls.genre_count[genre.genre] = 1
        return (cls.genre_count)

    @classmethod
    def add_to_artists(cls, artist):
        if artist in cls.genre:
            print(cls.artist_count)
            cls.artist_count[artist.artist] += 1 
        else:
            cls.artists.append(artist.artist)
            cls.artist_count[artist.artist] = 1
        return (cls.artist_count)
    
    @classmethod
    def add_to_genre_count(cls):
        return cls.genre_count

    @classmethod
    def add_to_artist_count(cls):
        pass


        

song1 = Song("99 Problems", "Jay Z", "Rap")
song2 = Song("Halo", "Beyonce", "Pop")
song3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
song4 = Song("Encore", "Jay Z", "Rap")

print(Song.genre_count)
print(Song.artist_count)
#print(Song.add_to_genre_count())