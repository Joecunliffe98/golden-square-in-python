from lib.challenge import *
import pytest

def test_track_can_be_added():
    new_track = Tracks()
    new_track.add_track("I Would - Lower Than Atlantis")
    assert new_track.see_tracks() == ["I Would - Lower Than Atlantis"]

def test_multiple_tracks_added():
    new_track = Tracks()
    new_track.add_track("I Would - Lower Than Atlantis")
    new_track.add_track("Had Enough - Lower Than Atlantis")
    assert new_track.see_tracks() == ["I Would - Lower Than Atlantis", "Had Enough - Lower Than Atlantis"]  

def test_no_track_given():
    new_track = Tracks()
    with pytest.raises(Exception) as e:
        new_track.add_track("")
    error_message = str(e.value)
    assert error_message == "No track provided"

def test_empty_track_list():
    new_track = Tracks()
    assert new_track.see_tracks() == "No tracks currently in list!"