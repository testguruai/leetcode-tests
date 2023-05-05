
import pytest
from solution import RecentCounter

def test_recent_counter():
    recent_counter = RecentCounter()

    # Test case 1
    assert recent_counter.ping(1) == 1

    # Test case 2
    assert recent_counter.ping(100) == 2

    # Test case 3
    assert recent_counter.ping(3001) == 1

    # Test case 4
    assert recent_counter.ping(3002) == 2

    # Test case 5
    assert recent_counter.ping(5000) == 1
