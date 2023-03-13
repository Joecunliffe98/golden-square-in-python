from lib.track import *

def test_returns_true_if_keyword_matches_title_or_artist():
    track1 = Track("Artist 1", "Track 1")
    assert track1.matches("1") == True

def test_returns_false_if_keyword__does_not_match_title_or_artist():
    track1 = Track("Artist 1", "Track 1")
    assert track1.matches("3") == False

def test_add_multiple_tracks_and_returns_true_if_keyword_matches():
    track1 = Track("Artist 1", "Track 1")
    track2 = Track("Artist 2", "Track 2")
    assert track1.matches("Artist") == True

def test_add_multiple_tracks_and_returns_false_if_keyword_does_not_match():
    track1 = Track("Artist 1", "Track 1")
    track2 = Track("Artist 2", "Track 2")
    assert track1.matches("Track 3") == False