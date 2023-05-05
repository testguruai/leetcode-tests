import pytest
from solution import Solution


def test_convert():
    s = Solution()

    assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert s.convert("A", 1) == "A"
    assert s.convert("AB", 1) == "AB"
    assert s.convert("ABCDEF", 2) == "ACEBDF"
    assert s.convert("ABCDE", 4) == "ABCED"


if __name__ == "__main__":
    pytest.main()