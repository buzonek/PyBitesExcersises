import pytest

from account import Account


@pytest.fixture(scope='module')
def account():
    return Account('Rob', 100)


@pytest.fixture(scope='module')
def second_account():
    return Account('Mike', 90)


def test_str(account):
    assert str(account) == 'Account of Rob with starting amount: 100'


def test_repr(account):
    assert repr(account) == "Account('Rob', 100)"


def test_add_trans(account):
    with pytest.raises(ValueError):
        account.add_transaction('123')
    account.add_transaction(200)
    assert account.balance == 300


def test_len(account):
    assert len(account) == 1


def test_comparison(account, second_account):
    assert account > second_account
    second_account.add_transaction(110)
    assert account >= second_account
