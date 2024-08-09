from wallet import Wallet, InsufficientBalance
import pytest


@pytest.fixture
def empty_wallet():
    """Return a wallet instance of initial balance 0."""
    return Wallet()


@pytest.fixture
def wallet():
    """Return a wallet instance with an initial balance of 100."""
    return Wallet(100)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.getBalance() == 0


def test_wallet_initial_add_cash(empty_wallet):
    empty_wallet.addCash(50)
    assert empty_wallet.getBalance() == 50


def test_wallet_add_cash(wallet):
    wallet.addCash(50)
    assert wallet.getBalance() == 150


def test_wallet_spend(wallet):
    wallet.spend(20)
    assert wallet.getBalance() == 80


def test_insufficient_wallet_balance(wallet):
    with pytest.raises(InsufficientBalance):
        wallet.spend(120)


@pytest.mark.parametrize("earned,spend,expected",
                         [(10,5,5),(50,30,20)])
def test_transaction(earned,spend,expected,empty_wallet):
    empty_wallet.addCash(earned)
    empty_wallet.spend(spend)
    assert empty_wallet.getBalance()==expected


