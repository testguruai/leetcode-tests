
import pytest

class TestSolution:
    def test_searchRange_emptyList(self):
        s = Solution()
        assert s.searchRange([], 3) == [-1, -1]

    def test_searchRange_notInList(self):
        s = Solution()
        assert s.searchRange([1,4,7,9], 5) == [-1, -1]

    def test_searchRange_oneOccurrence(self):
        s = Solution()
        assert s.searchRange([1,3,5,7,9], 5) == [2, 2]

    def test_searchRange_multipleOccurrences(self):
        s = Solution()
        assert s.searchRange([1,3,5,5,5,7,9], 5) == [2, 4]

    def test_searchRange_firstElement(self):
        s = Solution()
        assert s.searchRange([3,5,7,9], 3) == [0, 0]

    def test_searchRange_lastElement(self):
        s = Solution()
        assert s.searchRange([1,4,7,9], 9) == [3, 3]

    def test_searchRange_singleElement(self):
        s = Solution()
        assert s.searchRange([5], 5) == [0, 0]

    def test_searchRange_negativeNumbers(self):
        s = Solution()
        assert s.searchRange([-5,-2,1,3,5,5,5,7], 5) == [4, 6]
