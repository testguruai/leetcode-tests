
def test_lengthLongestPath_empty_input():
    s = Solution()
    assert s.lengthLongestPath("") == 0

def test_lengthLongestPath_no_files():
    s = Solution()
    input_str = "dir1\n\tsubdir1\n\tsubdir2\n\t\tsubsubdir1\n\tsubdir3\n"
    assert s.lengthLongestPath(input_str) == 0

def test_lengthLongestPath_single_file():
    s = Solution()
    input_str = "dir\n\tfile.txt"
    assert s.lengthLongestPath(input_str) == 8

def test_lengthLongestPath_multiple_files():
    s = Solution()
    input_str = "dir1\n\tsubdir1\n\t\tfile1.txt\n\tsubdir2\n\t\tsubsubdir1\n\t\t\tfile2.txt\n\tsubdir3\n\t\tfile3.txt"
    assert s.lengthLongestPath(input_str) == 22
