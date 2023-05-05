
def test_read_empty_buf():
    solution = Solution()
    buf = [''] * 10
    assert solution.read(buf, 0) == 0
    assert buf == [''] * 10

def test_read_zero_characters():
    solution = Solution()
    buf = [''] * 10
    assert solution.read(buf, 0) == 0
    assert buf == [''] * 10

def test_read_less_than_4_characters():
    solution = Solution()
    buf = [''] * 10
    assert solution.read(buf, 3) == 3
    assert buf[:3] == ['a', 'b', 'c']
    assert buf[3:] == [''] * 7

def test_read_multiple_times():
    solution = Solution()
    buf = [''] * 10
    assert solution.read(buf, 2) == 2
    assert buf[:2] == ['a', 'b']
    assert buf[2:] == [''] * 8
    assert solution.read(buf, 3) == 3
    assert buf[:5] == ['a', 'b', 'c', 'd', 'e']
    assert buf[5:] == [''] * 5

def test_read_more_than_available():
    solution = Solution()
    buf = [''] * 10
    assert solution.read(buf, 6) == 6
    assert buf[:6] == ['a', 'b', 'c', 'd', 'e', 'f']
    assert buf[6:] == [''] * 4
    assert solution.read(buf, 6) == 4
    assert buf[:10] == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    assert buf[10:] == [''] * 0
