1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


2. Design the Class Interface

class Tasks():

    def __init__(self):
        List: To store all of the music listened to
              self.track_list = []

    def add_track(self, task)
        String: Details of the track
        Adds track to self.track_list

    def see_tracks(self):
        Returns self.track_list


1. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

# EXAMPLE

"""
Given a track
#adds track to list and shows the list
"""
new_track = Tracks()
new_track.add_track("I Would - Lower Than Atlantis")
assert new_track.see_tracks() = ["I Would - Lower Than Atlantis"]

"""
Given multiple tracks
#adds tracks to list and shows the list
"""
new_track = Tracks()
new_track.add_track("I Would - Lower Than Atlantis")
new_track.add_track("Had Enough - Lower Than Atlantis")
assert new_track.see_tracks() = ["I Would - Lower Than Atlantis", "Had Enough - Lower Than Atlantis"]

"""
Given no track
#adds raises an exception
"""
new_track = Tracks()
new_track.add_track("") # raises an error with the message "No track provided."

"""
Given an empty track list
#returns a message saying no tracks in list
"""
new_track = Tracks()
new_track.see_tracks() = "No tracks currently in list!"


1. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.