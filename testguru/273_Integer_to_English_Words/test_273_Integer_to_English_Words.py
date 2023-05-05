
def test_numberToWords():
    s = Solution()

    assert s.numberToWords(0) == "Zero"
    assert s.numberToWords(123) == "One Hundred Twenty Three"
    assert s.numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    assert s.numberToWords(1234567891) == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
