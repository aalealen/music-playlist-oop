class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
    def __str__(self):
        return f"{self.title} — {self.artist} ({self.duration} сек)"
class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []
    def add_track(self, track): 
        self.tracks.append(track)
    def total_duration(self): 
        total = 0
        for track in self.tracks:
            total += track.duration
        return total
    def total_duration_formatted(self): 
        total = self.total_duration()
        m =  total // 60
        s = total % 60
        return f'{m} мин {s} сек'
    def show(self):
        print(f"{self.name}:")
        for i, track in enumerate(self.tracks, 1):
            print(f"{i}. {track}")
    def find_by_artist(self,artist):
        result = []
        for track in self.tracks:
            if track.artist == artist:
                result.append(track)
        return result
class Player:
    def __init__(self):
        self.playlists = []
        self.current_playlist = None
        self.current_track_index = 0
    def add_playlist(self, playlist): 
        self.playlists.append(playlist)
    def select_playlist(self, name): 
        for playlist in self.playlists:
            if playlist.name == name:
                self.current_playlist = playlist
                self.current_track_index = 0
                return
        print("Плейлист не найден")
    def play(self):
        if self.current_playlist is None:
            print("Плейлист не выбран")
        elif len(self.current_playlist.tracks) == 0:
            print("Плейлист пуст")
        else:
            print(self.current_playlist.tracks[self.current_track_index])

    def next_track(self):
        if self.current_playlist is None or len(self.current_playlist.tracks) == 0:
            print("Нет активного плейлиста")
            return
        
        self.current_track_index += 1
        if self.current_track_index >= len(self.current_playlist.tracks):
            self.current_track_index = 0
    def prev_track(self):
        if self.current_playlist is None or len(self.current_playlist.tracks) == 0:
            print("Нет активного плейлиста")
            return
        
        self.current_track_index -= 1
        if self.current_track_index < 0:
            self.current_track_index = len(self.current_playlist.tracks) - 1
