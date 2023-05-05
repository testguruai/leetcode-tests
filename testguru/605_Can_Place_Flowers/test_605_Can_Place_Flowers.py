import pytest

from solution import Solution

def test_Solution_canPlaceFlowers():
    sol = Solution()
    
    # Test Case 1
    flowerbed = [1,0,0,0,1]
    n = 1
    assert sol.canPlaceFlowers(flowerbed, n) == True
    
    # Test Case 2
    flowerbed = [1,0,0,0,1]
    n = 2
    assert sol.canPlaceFlowers(flowerbed, n) == False
    
    # Test Case 3
    flowerbed = [0,0,1,0,0]
    n = 2
    assert sol.canPlaceFlowers(flowerbed, n) == True
    
    # Test Case 4
    flowerbed = [0,0,1,0,0]
    n = 3
    assert sol.canPlaceFlowers(flowerbed, n) == False
    
    # Test Case 5
    flowerbed = [1,0,0,0,0,0,1]
    n = 2
    assert sol.canPlaceFlowers(flowerbed, n) == True
    
    # Test Case 6
    flowerbed = [1,0,0,0,0,0,1]
    n = 3
    assert sol.canPlaceFlowers(flowerbed, n) == False
    
    # Test Case 7
    flowerbed = [0,0,0,0,0,0,0]
    n = 4
    assert sol.canPlaceFlowers(flowerbed, n) == True
    
    # Test Case 8
    flowerbed = [1,1,1,1,1,1,1]
    n = 2
    assert sol.canPlaceFlowers(flowerbed, n) == False
    
    # Test Case 9
    flowerbed = [1,0,1,0,1,0,1]
    n = 0
    assert sol.canPlaceFlowers(flowerbed, n) == True
    
    # Test Case 10
    flowerbed = [1,0,1,0,1,0,1]
    n = -1
    assert sol.canPlaceFlowers(flowerbed, n) == False
