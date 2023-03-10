class Tracks():
    def __init__(self):
        self.track_list = []
    def add_track(self, track):
        if track == "":
            raise Exception("No track provided")
        self.track_list.append(track)
    def see_tracks(self):
        if self.track_list == []:
            return "No tracks currently in list!"
        else:
            return self.track_list