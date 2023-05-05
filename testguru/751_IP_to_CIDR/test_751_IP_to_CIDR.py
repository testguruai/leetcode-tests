import pytest
from solution import Solution

def test_ipToInt():
    solution = Solution()
    assert solution.ipToInt("0.0.0.0") == 0
    assert solution.ipToInt("255.255.255.255") == 4294967295
    assert solution.ipToInt("192.168.1.1") == 3232235777

def test_intToIP():
    solution = Solution()
    assert solution.intToIP(0) == "0.0.0.0"
    assert solution.intToIP(3232235777) == "192.168.1.1"
    assert solution.intToIP(4294967295) == "255.255.255.255"

def test_ipToCIDR():
    solution = Solution()
    assert solution.ipToCIDR("0.0.0.0", 1) == ['0.0.0.0/32']
    assert solution.ipToCIDR("192.168.1.0", 4) == ['192.168.1.0/30', '192.168.1.4/31', '192.168.1.6/32']
    assert solution.ipToCIDR("172.19.26.2", 64) == ['172.19.26.2/26', '172.19.26.64/27', '172.19.26.96/28', 
                                                   '172.19.26.112/29', '172.19.26.120/30', '172.19.26.124/31', 
                                                   '172.19.26.126/32']