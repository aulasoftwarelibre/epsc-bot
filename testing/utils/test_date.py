import pytest
from datetime import datetime
from freezegun import freeze_time
from utils.date import is_friday


@freeze_time("2021-05-07")
def test_is_friday():
    assert is_friday() == True


@freeze_time("2021-06-07")
def test_is_not_friday():
    assert is_friday() == False


since_data = [
    (datetime(2021, 1, 1, 0, 4, 0, 0), 1, True),
    (datetime(2021, 1, 1, 0, 4, 0, 0), 2, False),
]