import pytest
from solution import Solution
import random

# create test cases
test_case_1 = ([1, 2, 3, 4, 5], 2, 4)
test_case_2 = ([10, 8, 6, 4, 2], 3, 6)
test_case_3 = ([7, 3, 5, 2, 9, 1], 1, 9)
test_case_4 = ([4, 6, 1, 3, 8, 9, 2], 5, 4)

# create class instance
s = Solution()

def test_findKthLargest():
    # test using sorted method
    assert s.findKthLargest(test_case_1[0], test_case_1[1]) == test_case_1[2]
    assert s.findKthLargest(test_case_2[0], test_case_2[1]) == test_case_2[2]
    assert s.findKthLargest(test_case_3[0], test_case_3[1]) == test_case_3[2]
    
    # test using min heap method
    assert s.findKthLargest(test_case_1[0], test_case_1[1]) == test_case_1[2]
    assert s.findKthLargest(test_case_2[0], test_case_2[1]) == test_case_2[2]
    assert s.findKthLargest(test_case_3[0], test_case_3[1]) == test_case_3[2]

    # test using quick selection method
    assert s.findKthLargest(test_case_1[0], test_case_1[1]) == test_case_1[2]
    assert s.findKthLargest(test_case_2[0], test_case_2[1]) == test_case_2[2]
    assert s.findKthLargest(test_case_3[0], test_case_3[1]) == test_case_3[2]
    
    
    # additional test case for random input
    random_list = [random.randint(0, 1000000) for i in range(10000)]
    k = random.randint(1, 10000)
    assert s.findKthLargest(random_list, k) == sorted(random_list, reverse=True)[k-1]