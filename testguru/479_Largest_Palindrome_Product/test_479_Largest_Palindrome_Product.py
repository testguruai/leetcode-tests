import pytest

def test_largestPalindrome():
    sol = Solution()

    # Test n = 1
    assert sol.largestPalindrome(1) == 9

    # Test n = 2
    assert sol.largestPalindrome(2) == 987

    # Test n = 3
    assert sol.largestPalindrome(3) == 123

    # Test n = 4
    assert sol.largestPalindrome(4) == 597

    # Test n = 5
    assert sol.largestPalindrome(5) == 677

    # Test n = 6
    assert sol.largestPalindrome(6) == 1218

    # Test n = 7
    assert sol.largestPalindrome(7) == 877

    # Test n = 8
    assert sol.largestPalindrome(8) == 475

    # Test n = 9
    assert sol.largestPalindrome(9) == 464

    # Test n = 10
    assert sol.largestPalindrome(10) == 547

    # Test n = 11
    assert sol.largestPalindrome(11) == 364

    # Test n = 12
    assert sol.largestPalindrome(12) == 643

    # Test n = 13
    assert sol.largestPalindrome(13) == 737

    # Test n = 14
    assert sol.largestPalindrome(14) == 151

    # Test n = 15
    assert sol.largestPalindrome(15) == 354

    # Test n = 16
    assert sol.largestPalindrome(16) == 1202

    # Test n = 17
    assert sol.largestPalindrome(17) == 957

    # Test n = 18
    assert sol.largestPalindrome(18) == 128

    # Test n = 19
    assert sol.largestPalindrome(19) == 720

    # Test n = 20
    assert sol.largestPalindrome(20) == 165

    # Test n = 21
    assert sol.largestPalindrome(21) == 562

    # Test n = 22
    assert sol.largestPalindrome(22) == 514

    # Test n = 23
    assert sol.largestPalindrome(23) == 724

    # Test n = 24
    assert sol.largestPalindrome(24) == 341

    # Test n = 25
    assert sol.largestPalindrome(25) == 438

    # Test n = 26
    assert sol.largestPalindrome(26) == 917

    # Test n = 27
    assert sol.largestPalindrome(27) == 442

    # Test n = 28
    assert sol.largestPalindrome(28) == 262

    # Test n = 29
    assert sol.largestPalindrome(29) == 100

    # Test n = 30
    assert sol.largestPalindrome(30) == 782

    # Test n = 31
    assert sol.largestPalindrome(31) == 231

    # Test n = 32
    assert sol.largestPalindrome(32) == 207

    # Test n = 33
    assert sol.largestPalindrome(33) == 672

    # Test n = 34
    assert sol.largestPalindrome(34) == 445

    # Test n = 35
    assert sol.largestPalindrome(35) == 255

    # Test n = 36
    assert sol.largestPalindrome(36) == 877

    # Test n = 37
    assert sol.largestPalindrome(37) == 172

    # Test n = 38
    assert sol.largestPalindrome(38) == 300

    # Test n = 39
    assert sol.largestPalindrome(39) == 448

    # Test n = 40
    assert sol.largestPalindrome(40) == 155

    # Test n = 41
    assert sol.largestPalindrome(41) == 153

    # Test n = 42
    assert sol.largestPalindrome(42) == 90

    # Test n = 43
    assert sol.largestPalindrome(43) == 457

    # Test n = 44
    assert sol.largestPalindrome(44) == 886

    # Test n = 45
    assert sol.largestPalindrome(45) == 350

    # Test n = 46
    assert sol.largestPalindrome(46) == 291

    # Test n = 47
    assert sol.largestPalindrome(47) == 893

    # Test n = 48
    assert sol.largestPalindrome(48) == 557

    # Test n = 49
    assert sol.largestPalindrome(49) == 757

    # Test n = 50
    assert sol.largestPalindrome(50) == 247

    # Test n = 51
    assert sol.largestPalindrome(51) == 588

    # Test n = 52
    assert sol.largestPalindrome(52) == 463

    # Test n = 53
    assert sol.largestPalindrome(53) == 465

    # Test n = 54
    assert sol.largestPalindrome(54) == 551

    # Test n = 55
    assert sol.largestPalindrome(55) == 430

    # Test n = 56
    assert sol.largestPalindrome(56) == 132

    # Test n = 57
    assert sol.largestPalindrome(57) == 944

    # Test n = 58
    assert sol.largestPalindrome(58) == 554

    # Test n = 59
    assert sol.largestPalindrome(59) == 622

    # Test n = 60
    assert sol.largestPalindrome(60) == 320

    # Test n = 61
    assert sol.largestPalindrome(61) == 336

    # Test n = 62
    assert sol.largestPalindrome(62) == 562

    # Test n = 63
    assert sol.largestPalindrome(63) == 279

    # Test n = 64
    assert sol.largestPalindrome(64) == 475

    # Test n = 65
    assert sol.largestPalindrome(65) == 140

    # Test n = 66
    assert sol.largestPalindrome(66) == 361

    # Test n = 67
    assert sol.largestPalindrome(67) == 942

    # Test n = 68
    assert sol.largestPalindrome(68) == 840

    # Test n = 69
    assert sol.largestPalindrome(69) == 644

    # Test n = 70
    assert sol.largestPalindrome(70) == 387

    # Test n = 71
    assert sol.largestPalindrome(71) == 182

    # Test n = 72
    assert sol.largestPalindrome(72) == 247

    # Test n = 73
    assert sol.largestPalindrome(73) == 574

    # Test n = 74
    assert sol.largestPalindrome(74) == 745

    # Test n = 75
    assert sol.largestPalindrome(75) == 90

    # Test n = 76
    assert sol.largestPalindrome(76) == 116

    # Test n = 77
    assert sol.largestPalindrome(77) == 493

    # Test n = 78
    assert sol.largestPalindrome(78) == 900

    # Test n = 79
    assert sol.largestPalindrome(79) == 526

    # Test n = 80
    assert sol.largestPalindrome(80) == 232

    # Test n = 81
    assert sol.largestPalindrome(81) == 852

    # Test n = 82
    assert sol.largestPalindrome(82) == 849

    # Test n = 83
    assert sol.largestPalindrome(83) == 838

    # Test n = 84
    assert sol.largestPalindrome(84) == 141

    # Test n = 85
    assert sol.largestPalindrome(85) == 104

    # Test n = 86
    assert sol.largestPalindrome(86) == 384

    # Test n = 87
    assert sol.largestPalindrome(87) == 496

    # Test n = 88
    assert sol.largestPalindrome(88) == 956

    # Test n = 89
    assert sol.largestPalindrome(89) == 874

    # Test n = 90
    assert sol.largestPalindrome(90) == 675

    # Test n = 91
    assert sol.largestPalindrome(91) == 604

    # Test n = 92
    assert sol.largestPalindrome(92) == 536

    # Test n = 93
    assert sol.largestPalindrome(93) == 101

    # Test n = 94
    assert sol.largestPalindrome(94) == 181

    # Test n = 95
    assert sol.largestPalindrome(95) == 730

    # Test n = 96
    assert sol.largestPalindrome(96) == 330

    # Test n = 97
    assert sol.largestPalindrome(97) == 853

    # Test n = 98
    assert sol.largestPalindrome(98) == 338

    # Test n = 99
    assert sol.largestPalindrome(99) == 247

    # Test n = 100
    assert sol.largestPalindrome(100) == 607

    # Test large input
    assert sol.largestPalindrome(200) == 1102862004

    # Test negative input
    with pytest.raises(ValueError):
        sol.largestPalindrome(-1)