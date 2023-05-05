import pytest

def test_findMin():
    sol = Solution()

    # Test case 1
    nums1 = [4,5,6,7,0,1,2]
    assert sol.findMin(nums1) == 0

    # Test case 2
    nums2 = [3,4,5,1,2]
    assert sol.findMin(nums2) == 1

    # Test case 3
    nums3 = [2,1]
    assert sol.findMin(nums3) == 1

    # Test case 4
    nums4 = [1]
    assert sol.findMin(nums4) == 1

    # Test case 5
    nums5 = [1,2,3,4,5]
    assert sol.findMin(nums5) == 1

    # Test case 6
    nums6 = [5,4,3,2,1]
    assert sol.findMin(nums6) == 1

    # Test case 7
    nums7 = [1,1,1,1,1]
    assert sol.findMin(nums7) == 1

    # Test case 8
    nums8 = []
    assert sol.findMin(nums8) == None

    # Test case 9
    nums9 = [2,2,2,0,1]
    assert sol.findMin(nums9) == 0

    # Test case 10
    nums10 = [3,1,3]
    assert sol.findMin(nums10) == 1

    # Test case 11
    nums11 = [1,1]
    assert sol.findMin(nums11) == 1

    # Test case 12
    nums12 = [10,1]
    assert sol.findMin(nums12) == 1

    # Test case 13
    nums13 = [1,10]
    assert sol.findMin(nums13) == 1

    # Test case 14
    nums14 = [1,3,3]
    assert sol.findMin(nums14) == 1

    # Test case 15
    nums15 = [-1,2,3,4,5,-1,-1,-1]
    assert sol.findMin(nums15) == -1

    # Test case 16
    nums16 = [1,3,5]
    assert sol.findMin(nums16) == 1

    # Test case 17
    nums17 = [3,5,1]
    assert sol.findMin(nums17) == 1

    # Test case 18
    nums18 = [5,1,3]
    assert sol.findMin(nums18) == 1

    # Test case 19
    nums19 = [3,1,5]
    assert sol.findMin(nums19) == 1

    # Test case 20
    nums20 = [1,5,3]
    assert sol.findMin(nums20) == 1

    # Test case 21
    nums21 = [3,3,3,3,3,0,3]
    assert sol.findMin(nums21) == 0

    # Test case 22
    nums22 = [3,3,3,0,3,3,3]
    assert sol.findMin(nums22) == 0

    # Test case 23
    nums23 = [3,0,3,3,3,3,3]
    assert sol.findMin(nums23) == 0

    # Test case 24
    nums24 = [3,3,3,3,3,3,0]
    assert sol.findMin(nums24) == 0

    # Test case 25
    nums25 = [0,3,3,3,3,3,3]
    assert sol.findMin(nums25) == 0

    # Test case 26
    nums26 = [3,3,3,3,0,3,3]
    assert sol.findMin(nums26) == 0

    # Test case 27
    nums27 = [3,3,0,3,3,3,3]
    assert sol.findMin(nums27) == 0

    # Test case 28
    nums28 = [2,2,2,0,1,1,1]
    assert sol.findMin(nums28) == 0

    # Test case 29
    nums29 = [1,1,1,2,2,2,0]
    assert sol.findMin(nums29) == 0

    # Test case 30
    nums30 = [2,0,1,1,1,2,2]
    assert sol.findMin(nums30) == 0

    # Test case 31
    nums31 = [1,2,2,2,1,1,1,1]
    assert sol.findMin(nums31) == 1

    # Test case 32
    nums32 = [3,1,1,2,2,2,2]
    assert sol.findMin(nums32) == 1

    # Test case 33
    nums33 = [2,2,2,2,1,1,3,1]
    assert sol.findMin(nums33) == 1

    # Test case 34
    nums34 = [1,1,3,1,2,2,2,2]
    assert sol.findMin(nums34) == 1

    # Test case 35
    nums35 = [2,2,2,2,3,1,1,2]
    assert sol.findMin(nums35) == 1

    # Test case 36
    nums36 = [2,1,2,2,2,2,2]
    assert sol.findMin(nums36) == 1

    # Test case 37
    nums37 = [1,2,2,2,2,2,1]
    assert sol.findMin(nums37) == 1

    # Test case 38
    nums38 = [1,2,2,2,1,2,2]
    assert sol.findMin(nums38) == 1

    # Test case 39
    nums39 = [2,2,1,2,2,2,2]
    assert sol.findMin(nums39) == 1

    # Test case 40
    nums40 = [2,2,2,2,2,1,2]
    assert sol.findMin(nums40) == 1

    # Test case 41
    nums41 = [2,2,2,1,2,2,2]
    assert sol.findMin(nums41) == 1

    # Test case 42
    nums42 = [2,2,2,2,2,2,1]
    assert sol.findMin(nums42) == 1

    # Test case 43
    nums43 = [1,2,2,2,2,2,2]
    assert sol.findMin(nums43) == 1

    # Test case 44
    nums44 = [2,1,2,2,2,2,1]
    assert sol.findMin(nums44) == 1

    # Test case 45
    nums45 = [1,2,2,2,2,1,2]
    assert sol.findMin(nums45) == 1

    # Test case 46
    nums46 = [1,2,2,1,2,2,2]
    assert sol.findMin(nums46) == 1

    # Test case 47
    nums47 = [2,2,1,2,2,2,1]
    assert sol.findMin(nums47) == 1

    # Test case 48
    nums48 = [2,2,2,1,2,2,1]
    assert sol.findMin(nums48) == 1

    # Test case 49
    nums49 = [2,1,2,2,2,1,2]
    assert sol.findMin(nums49) == 1

    # Test case 50
    nums50 = [2,2,1,2,1,2,2]
    assert sol.findMin(nums50) == 1

    # Test case 51
    nums51 = [2,1,2,1,2,2,2]
    assert sol.findMin(nums51) == 1

    # Test case 52
    nums52 = [1,2]
    assert sol.findMin(nums52) == 1

    # Test case 53
    nums53 = [2,1]
    assert sol.findMin(nums53) == 1

    # Test case 54
    nums54 = [1,2,3]
    assert sol.findMin(nums54) == 1

    # Test case 55
    nums55 = [3,2,1]
    assert sol.findMin(nums55) == 1

    # Test case 56
    nums56 = [1,2,3,4]
    assert sol.findMin(nums56) == 1

    # Test case 57
    nums57 = [4,3,2,1]
    assert sol.findMin(nums57) == 1

    # Test case 58
    nums58 = [1,1,1,0,1,1,1,1,1,1]
    assert sol.findMin(nums58) == 0

    # Test case 59
    nums59 = [1,1,1,1,1,1,0,1,1,1]
    assert sol.findMin(nums59) == 0

    # Test case 60
    nums60 = [1,1,1,1,0,1,1,1,1,1]
    assert sol.findMin(nums60) == 0

    # Test case 61
    nums61 = [1,1,1,1,1,1,1,1,0,1]
    assert sol.findMin(nums61) == 0

    # Test case 62
    nums62 = [1,1,1,1,1,1,1,0,1,1]
    assert sol.findMin(nums62) == 0

    # Test case 63
    nums63 = [1,1,1,1,0,1,1,1,0,1]
    assert sol.findMin(nums63) == 0

    # Test case 64
    nums64 = [1,1,0,1,1,1,1,1,0,1]
    assert sol.findMin(nums64) == 0

    # Test case 65
    nums65 = [1,1,1,0,1,1,0,1,1,1]
    assert sol.findMin(nums65) == 0

    # Test case 66
    nums66 = [1,1,0,1,1,0,1,1,1,1]
    assert sol.findMin(nums66) == 0

    # Test case 67
    nums67 = [1,0,1,1,1,0,1,1,1,1]
    assert sol.findMin(nums67) == 0

    # Test case 68
    nums68 = [0,1,1,1,1,1,1,1,1,1]
    assert sol.findMin(nums68) == 0

    # Test case 69
    nums69 = [1,1,1,1,1,1,1,1,1,0]
    assert sol.findMin(nums69) == 0

    # Test case 70
    nums70 = [1,1,1,1,1,1,1,0,1,1]
    assert sol.findMin(nums70) == 0

    # Test case 71
    nums71 = [1,1,0,1,1,1,1,1,1,1]
    assert sol.findMin(nums71) == 0

    # Test case 72
    nums72 = [1,0,1,1,1,1,1,1,1,1]
    assert sol.findMin(nums72) == 0

    # Test case 73
    nums73 = [1,1,1,1,0,1,1,1,1,0]
    assert sol.findMin(nums73) == 0

    # Test case 74
    nums74 = [1,0,1,1,1,1,0,1,1,1]
    assert sol.findMin(nums74) == 0

    # Test case 75
    nums75 = [1,1,1,0,1,1,1,1,0,1]
    assert sol.findMin(nums75) == 0

    # Test case 76
    nums76 = [4,5,6,7,8,9,1,2,3]
    assert sol.findMin(nums76) == 1

    # Test case 77
    nums77 = [3,4,5,1,2]
    assert sol.findMin(nums77) == 1

    # Test case 78
    nums78 = [5,6,0,1,2,3,4]
    assert sol.findMin(nums78) == 0

    # Test case 79
    nums79 = [2,2,2,2,2,2,2,2,2,1]
    assert sol.findMin(nums79) == 1

    # Test case 80
    nums80 = [2,2,2,2,2,2,2,1,2,2]
    assert sol.findMin(nums80) == 1

    # Test case 81
    nums81 = [2,2,2,2,2,2,1,2,2,2]
    assert sol.findMin(nums81) == 1

    # Test case 82
    nums82 = [2,2,2,2,2,1,2,2,2,2]
    assert sol.findMin(nums82) == 1

    # Test case 83
    nums83 = [2,2,2,2,1,2,2,2,2,2]
    assert sol.findMin(nums83) == 1

    # Test case 84
    nums84 = [2,2,2,1,2,2,2,2,2,2]
    assert sol.findMin(nums84) == 1

    # Test case 85
    nums85 = [2,2,1,2,2,2,2,2,2,2]
    assert sol.findMin(nums85) == 1

    # Test case 86
    nums86 = [2,1,2,2,2,2,2,2,2,2]
    assert sol.findMin(nums86) == 1

    # Test case 87
    nums87 = [1,2,2,2,2,2,2,2,2,2]
    assert sol.findMin(nums87) == 1

    # Test case 88
    nums88 = [2,2,2,2,2,2,2,2,1,2]
    assert sol.findMin(nums88) == 1

    # Test case 89
    nums89 = [2,2,2,2,2,2,2,1,2,2]
    assert sol.findMin(nums89) == 1

    # Test case 90
    nums90 = [2,2,2,2,2,2,1,2,2,2]
    assert sol.findMin(nums90) == 1

    # Test case 91
    nums91 = [2,2,2,2,2,1,2,2,2,2]
    assert sol.findMin(nums91) == 1

    # Test case 92
    nums92 = [2,2,2,2,1,2,2,2,2,2]
    assert sol.findMin(nums92) == 1

    # Test case 93
    nums93 = [2,2,2,1,2,2,2,2,2,2]
    assert sol.findMin(nums93) == 1

    # Test case 94
    nums94 = [2,2,1,2,2,2,2,2,2,2]
   