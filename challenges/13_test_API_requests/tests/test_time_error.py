from lib.time_error import *
from unittest.mock import Mock

def test_time_error():
    requester_mock = Mock()
    response_mock = Mock()
    time_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime": 1678709372}
    time_mock.time.return_value = 1678709372.5
    time_error = TimeError(requester_mock, time_mock)
    assert time_error.error() == -0.5
    