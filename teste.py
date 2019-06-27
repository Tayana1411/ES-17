import pytest
from principal import somar
from principal import sub

""" test of function somar"""
def test_somar():
    assert somar(2,4) == 6

""" test of function sub"""
def test_sub():
    assert sub(5,3) == 2