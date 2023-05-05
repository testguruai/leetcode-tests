import pytest

def test_restoreIpAddresses():
    s = Solution()
    assert s.restoreIpAddresses('25525511135') == ["255.255.11.135", "255.255.111.35"]
    assert s.restoreIpAddresses('0000') == ['0.0.0.0']
    assert s.restoreIpAddresses('1111') == ['1.1.1.1']
    assert s.restoreIpAddresses('010010') == ['0.10.0.10', '0.100.1.0']
    assert s.restoreIpAddresses('172162541') == ['17.216.25.41']

def test_isValid():
    s = Solution()
    assert s.isValid('12') == True
    assert s.isValid('123') == True
    assert s.isValid('01') == False
    assert s.isValid('256') == False
    assert s.isValid('0') == True

def test_getremainIP():
    s = Solution()
    assert s.getremainIP('172162541', 0, 3) == ['172.16.25.41']
    assert s.getremainIP('25525511135', 0, 4) == ["255.255.11.135", "255.255.111.35"]
    assert s.getremainIP('010010', 0, 4) == ['0.10.0.10', '0.100.1.0']
    assert s.getremainIP('010012', 0, 4) == []

def test_edge_cases():
    s = Solution()
    assert s.restoreIpAddresses('') == []
    assert s.restoreIpAddresses('999999999999') == []
    assert s.restoreIpAddresses('000000000000') == ['0.0.0.0']
    assert s.restoreIpAddresses('192512231') == ['19.251.22.31', '192.51.22.31', '192.5.22.31', '19.25.22.31', '19.2.22.31']