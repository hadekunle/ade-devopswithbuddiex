import pytest
from list_manipulation_solution_ade import and_lists, left_lists, xor_lists


def test_xor_lists():
    a,b = [], []
    assert xor_lists(a,b) ==[]
    a,b = [1, 2, 3], [2, 4, 6]
    assert xor_lists(a,b) == [1, 3, 4, 6]
    a,b = [1,2], [3,4]
    assert xor_lists(a,b) ==[1,2,3,4]


def test_and_lists():
    a,b = [], []
    assert and_lists(a,b) ==[]
    a,b = [1, 2, 3], [2, 4, 6]
    assert and_lists(a,b) == [2]
    a,b = [1,2], [3,4]
    assert and_lists(a,b) ==[]


def test_left_lists():
    a,b = [], []
    assert left_lists(a,b) ==[]
    a,b = [1, 2, 3], [2, 4, 6]
    assert left_lists(a,b) == [1,3]
    a,b = [1,2], [3,4]
    assert left_lists(a,b) ==[1,2]


