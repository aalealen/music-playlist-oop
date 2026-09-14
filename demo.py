from music_playlist import Track, Playlist, Player

# Создаём треки
p = Playlist("Мой плейлист")
p.add_track(Track("Bohemian Rhapsody", "Queen", 354))
p.add_track(Track("Imagine", "John Lennon", 183))
p.add_track(Track("We Will Rock You", "Queen", 122))

# Показываем плейлист
p.show()
print(f"Общая длительность: {p.total_duration_formatted()}")
print("Треки Queen:")
for track in p.find_by_artist("Queen"):
    print(f"  {track}")

# Управляем плеером
player = Player()
player.add_playlist(p)
player.select_playlist("Мой плейлист")

print("Управление плеером")
player.play()
player.next_track()
player.play()
player.next_track()
player.play()
player.next_track()
player.play()
player.prev_track()
player.play()