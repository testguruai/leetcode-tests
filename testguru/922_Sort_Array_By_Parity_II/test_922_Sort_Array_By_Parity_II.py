
def test_sortArrayByParityII():
    s = Solution()

    # test empty input array
    assert s.sortArrayByParityII([]) == []

    # test array with odd and even numbers
    assert s.sortArrayByParityII([4,2,5,7]) == [4,5,2,7]

    # test array with only even numbers
    assert s.sortArrayByParityII([2,8,4,6]) == [2,8,4,6]

    # test array with only odd numbers
    assert s.sortArrayByParityII([3,9,5,7]) == [3,9,5,7]

    # test array with repeated numbers
    assert s.sortArrayByParityII([1,2,2,3,4,4]) == [2,1,4,3,2,4]

    # test array with negative even and odd numbers
    assert s.sortArrayByParityII([-4,-2,-5,-7]) == [-4,-5,-2,-7]
