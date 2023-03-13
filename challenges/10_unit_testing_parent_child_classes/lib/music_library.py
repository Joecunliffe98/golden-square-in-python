class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        self.track_list = []

    def add(self, track):
        self.track_list.append(track)

    def search(self, keyword):
        search_list = []
        for tracks in self.track_list:
            if tracks.matches(keyword):
                search_list.append(tracks)
            else:
                return "No tracks contain " + keyword
        return search_list

