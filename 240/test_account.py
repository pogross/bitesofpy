import pytest

from account import Account


@pytest.fixture()
def empty_account():
    return Account(owner="Empty")


@pytest.fixture
def filled_account():
    return Account(owner="Filled", amount=42)


@pytest.fixture
def faulty_account():
    return Account(owner="Faulty", amount="ABC")


@pytest.fixture
def transaction_account():
    acc = Account(owner="Transactions", amount=10)
    acc.add_transaction(3)
    acc.add_transaction(10)
    return acc


def test_non_int_transaction(filled_account):
    with pytest.raises(ValueError) as excinfo:
        filled_account.add_transaction("42")

    assert "please use int for amount" in str(excinfo.value)


def test_transaction(filled_account, empty_account):
    filled_account.add_transaction(42)
    assert filled_account.balance == 84

    empty_account.add_transaction(42)
    assert empty_account.balance == 42


def test_add_accounts(transaction_account, filled_account):
    combined = filled_account + transaction_account

    assert "Filled&Transactions" in str(combined)
    assert combined.balance == (23 + 42)


def test_comparisons(filled_account, empty_account):
    assert empty_account < filled_account
    assert filled_account > empty_account

    assert not empty_account < empty_account
    assert not empty_account > empty_account

    assert filled_account != empty_account
    assert empty_account == empty_account


def test_len(empty_account, transaction_account):
    assert len(empty_account) == 0
    assert len(transaction_account) == 2


def test_representations(empty_account, filled_account):
    assert repr(empty_account) == "Account('Empty', 0)"
    assert repr(filled_account) == "Account('Filled', 42)"

    assert str(empty_account) == "Account of Empty with starting amount: 0"
    assert str(filled_account) == "Account of Filled with starting amount: 42"


def test_get_transaction(transaction_account):
    assert transaction_account[0] == 3
    assert transaction_account[1] == 10
