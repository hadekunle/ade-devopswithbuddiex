import pytest
from find_valid_ips_obi_solution import find_valid_ips

def test_valid_ips():
    lines = ['192.87.30.143', '143.24.163', '159.146.287.89']
    assert find_valid_ips(lines) == ['192.87.30.143']

def test_invalid_ips():
    lines = ['999.999.999.999', '256.256.256.256', '192.168.1.256']
    assert find_valid_ips(lines) == []

def test_mixed_ips():
    lines = ['192.168.1.1', '10.10.10.10', '300.300.300.300', '256.100.100.100']
    assert find_valid_ips(lines) == ['192.168.1.1', '10.10.10.10']

def test_ips_with_leading_zeros():
    lines = ['192.168.01.01', '010.010.010.010', '192.168.1.1']
    assert find_valid_ips(lines) == ['192.168.1.1']

def test_ips_with_valid_and_invalid_characters():
    lines = ['192.168.1.1a', 'b192.168.1.1', '192.168.1.1']
    assert find_valid_ips(lines) == ['192.168.1.1']
