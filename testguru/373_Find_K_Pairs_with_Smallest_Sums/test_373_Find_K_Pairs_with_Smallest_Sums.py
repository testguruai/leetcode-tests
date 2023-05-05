import heapq
from typing import List
from solution import Solution

def test_kSmallestPairs():
    s = Solution()
    
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    result = s.kSmallestPairs(nums1, nums2, k)
    assert result == [[1,2],[1,4],[1,6]], f"Error: {result}"
    
    nums1 = [1,1,2]
    nums2 = [1,2,3]
    k = 2
    result = s.kSmallestPairs(nums1, nums2, k)
    assert result == [[1,1],[1,1]], f"Error: {result}"
    
    nums1 = [1,2]
    nums2 = [3]
    k = 3
    result = s.kSmallestPairs(nums1, nums2, k)
    assert result == [[1,3],[2,3]], f"Error: {result}"
    
    nums1 = []
    nums2 = []
    k = 5
    result = s.kSmallestPairs(nums1, nums2, k)
    assert result == [], f"Error: {result}"
