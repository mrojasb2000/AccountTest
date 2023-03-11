from account.account import Account
import pytest

def test_whenCreateAccountThenReturnAccountInstance():
    account = Account("Mavro", 1000)
    expected = 1000
    actual = account.balance
    assert actual == expected