class Playlist:
    def __init__(self, tracks):
        self._tracks = list(tracks)

    def __iter__(self):
        return iter(self._tracks)


if __name__ == "__main__":
    playlist = Playlist([7, 12, 18])
    for track in playlist:
        print("Track", track)
    first = iter(playlist)
    second = iter(playlist)
    print("Independent:", next(first), next(second))
    print("Empty:", list(Playlist([])))
