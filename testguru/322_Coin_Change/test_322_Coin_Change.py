import pytest

from solution import Solution

def test_coinChange():
    sol = Solution()
    coins_1 = [1, 2, 5]
    amount_1 = 11
    assert sol.coinChange(coins_1, amount_1) == 3

    coins_2 = [2]
    amount_2 = 3
    assert sol.coinChange(coins_2, amount_2) == -1

    coins_3 = [1]
    amount_3 = 0
    assert sol.coinChange(coins_3, amount_3) == 0

    coins_4 = [1]
    amount_4 = 1
    assert sol.coinChange(coins_4, amount_4) == 1

    coins_5 = [1]
    amount_5 = 2
    assert sol.coinChange(coins_5, amount_5) == 2

    coins_6 = [186, 419, 83, 408]
    amount_6 = 6249
    assert sol.coinChange(coins_6, amount_6) == 20

    coins_7 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    amount_7 = 1100
    assert sol.coinChange(coins_7, amount_7) == 58

    coins_8 = [27, 40, 244, 168, 383]
    amount_8 = 7854
    assert sol.coinChange(coins_8, amount_8) == 26

    coins_9 = [1, 2, 5]
    amount_9 = 100
    assert sol.coinChange(coins_9, amount_9) == 20

    coins_10 = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    amount_10 = 9332
    assert sol.coinChange(coins_10, amount_10) == 22

    coins_11 = [2, 5, 10, 20, 50, 100, 200, 500, 1000]
    amount_11 = 102
    assert sol.coinChange(coins_11, amount_11) == 7

    coins_12 = [186, 419, 83, 408]
    amount_12 = 9999
    assert sol.coinChange(coins_12, amount_12) == 25

    coins_13 = [430, 474, 83, 931, 377, 351, 741, 448, 123, 966]
    amount_13 = 8790
    assert sol.coinChange(coins_13, amount_13) == 20

    coins_14 = [83, 186, 408, 419]
    amount_14 = 1016
    assert sol.coinChange(coins_14, amount_14) == 3

    coins_15 = [1, 2]
    amount_15 = 2
    assert sol.coinChange(coins_15, amount_15) == 1

    coins_16 = []
    amount_16 = 0
    assert sol.coinChange(coins_16, amount_16) == -1

    coins_17 = [6, 7, 8, 9]
    amount_17 = 50
    assert sol.coinChange(coins_17, amount_17) == 7

    coins_18 = [34, 12, 4, 56, 7, 8, 99, 102]
    amount_18 = 416
    assert sol.coinChange(coins_18, amount_18) == 9

    coins_19 = [413, 317, 35, 920, 336, 762, 505, 124, 323, 665]
    amount_19 = 7582
    assert sol.coinChange(coins_19, amount_19) == 10

    coins_20 = [112, 216, 286, 432, 226, 183, 114, 197, 25, 7, 210, 436, 431, 225, 5, 311]
    amount_20 = 4828
    assert sol.coinChange(coins_20, amount_20) == 12

    coins_21 = [2, 5, 10, 20, 50, 100, 200, 500, 1000]
    amount_21 = 30
    assert sol.coinChange(coins_21, amount_21) == 2

    coins_22 = [479, 371]
    amount_22 = 19416
    assert sol.coinChange(coins_22, amount_22) == 57

    coins_23 = [186, 83, 408]
    amount_23 = 6249
    assert sol.coinChange(coins_23, amount_23) == 26

    coins_24 = [186, 83, 408, 419]
    amount_24 = 6249
    assert sol.coinChange(coins_24, amount_24) == 15

    coins_25 = [1, 2, 3]
    amount_25 = 5
    assert sol.coinChange(coins_25, amount_25) == 2

    coins_26 = [1, 3, 4, 5, 7, 8, 10, 12, 15, 18, 20, 24, 27, 30, 33, 37, 40, 44, 48, 50]
    amount_26 = 1000
    assert sol.coinChange(coins_26, amount_26) == 24

    coins_27 = [1, 3, 4, 7, 10]
    amount_27 = 53
    assert sol.coinChange(coins_27, amount_27) == 8

    coins_28 = [1, 2, 5]
    amount_28 = 100
    assert sol.coinChange(coins_28, amount_28) == 20

    coins_29 = [1, 3, 4, 5, 7, 9, 10, 12, 15, 18, 20, 25, 27, 30, 33, 35, 37, 40, 44, 48, 50]
    amount_29 = 1000
    assert sol.coinChange(coins_29, amount_29) == 21

    coins_30 = [2]
    amount_30 = 1
    assert sol.coinChange(coins_30, amount_30) == -1

    coins_31 = [2]
    amount_31 = 10
    assert sol.coinChange(coins_31, amount_31) == -1

    coins_32 = [464, 9, 305, 72, 63, 73, 153, 60, 124]
    amount_32 = 7741
    assert sol.coinChange(coins_32, amount_32) == 17

    coins_33 = [1, 2, 5]
    amount_33 = 100
    assert sol.coinChange(coins_33, amount_33) == 20

    coins_34 = [2, 5, 7]
    amount_34 = 107
    assert sol.coinChange(coins_34, amount_34) == 17

    coins_35 = [3, 5, 7, 8, 9, 10, 11]
    amount_35 = 245
    assert sol.coinChange(coins_35, amount_35) == 28

    coins_36 = [2, 3, 4]
    amount_36 = 5
    assert sol.coinChange(coins_36, amount_36) == 2

    coins_37 = [83, 141, 486, 470, 95, 193, 246, 438, 364, 121, 414, 458]
    amount_37 = 8565
    assert sol.coinChange(coins_37, amount_37) == 19

    coins_38 = [2, 3, 4]
    amount_38 = 1
    assert sol.coinChange(coins_38, amount_38) == -1

    coins_39 = [186, 408]
    amount_39 = 9538
    assert sol.coinChange(coins_39, amount_39) == 25

    coins_40 = [8, 15]
    amount_40 = 129
    assert sol.coinChange(coins_40, amount_40) == 10