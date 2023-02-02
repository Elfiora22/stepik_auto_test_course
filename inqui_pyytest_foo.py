import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup_module(module):
    #init_something()
    pass

def teardown_module(module):
    #teardown_something()
    pass

def test_upper():
    assert 'foo'.upper() == 'FOO'

def test_isupper():
    assert 'FOO'.isupper()

def test_failed_upper():
    assert 'foo'.upper() == 'FOO'
