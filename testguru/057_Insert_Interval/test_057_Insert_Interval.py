import pytest

class TestSolution:
    def setup_method(self, method):
        self.s = Solution()

    def test_insert_empty_intervals(self):
        assert self.s.insert([], Interval(1,3)) == [Interval(1,3)]

    def test_insert_non_overlap_intervals(self):
        assert self.s.insert([Interval(1,2), Interval(4,5)], Interval(3,6)) == [Interval(1,2), Interval(3,6), Interval(4,5)]

    def test_insert_overlap_intervals(self):
        assert self.s.insert([Interval(1,3), Interval(4,5)], Interval(2,4)) == [Interval(1,5)]

    def test_check_overlap_false(self):
        assert self.s.check_overlap(Interval(1,3), Interval(4,5)) == False

    def test_check_overlap_true(self):
        assert self.s.check_overlap(Interval(1,3), Interval(2,4)) == True

    def test_merge_intervals(self):
        assert self.s.merge_intervals(Interval(1,3), Interval(2,5)) == Interval(1,5)