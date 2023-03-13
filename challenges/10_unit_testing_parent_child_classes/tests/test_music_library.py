from lib.music_library import *
from unittest.mock import Mock

def test_add_track():
    library = MusicLibrary()
    mock_track = Mock()
    mock_track.title.return_value = "Track 1"
    mock_track.artist.return_value = "Artist 1"
    library.add(mock_track)
    assert library.track_list == [mock_track]

def test_search_for_track_that_is_in_list():
    library = MusicLibrary()
    mock_track = Mock()
    mock_track.matches.return_value = True
    library.add(mock_track)
    assert library.search("1") == [mock_track]

def test_search_for_track_that_is_not_in_list():
    library = MusicLibrary()
    mock_track = Mock()
    mock_track.matches.return_value = False
    library.add(mock_track)
    assert library.search("1") == "No tracks contain 1"