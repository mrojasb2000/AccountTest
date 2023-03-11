from account.account import Account

import pytest


def test_when_create_account_then_return_account_instance():
    account = Account("Mavro", 1000)
    expected = 1000
    
    actual = account.balance
    
    assert actual == expected

def test_should_throw_exception_when_debit_insufficient_balance():
     account = Account("Mavro", 1000)
     expected = "Error: Raised when the balance less or equal than zero"

     actual = account.debit(1500)

     assert actual == expected

def test_should_return_balance_when_debit_greater_than_zero():
     account = Account("Mavro", 1000)
     expected = 500

     actual = account.debit(500)
     
     assert actual == expected     