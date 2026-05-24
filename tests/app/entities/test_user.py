import pytest
#framework pytest: realizará os testes no que condiz ao usuário e sua conta
from src.app.entities.user import User


def test_user():

    user = User(
        name="Ana Rita",
        agency="0013",
        account="56789",
        current_balance=1000
    )

#assert verifica se o valor do nome e o saldo do suário são verdadeiros
    assert user.name == "Ana Rita"
    assert user.current_balance == 1000

#teste de saldo inválido - negativo
def test_invalid_balance():

    with pytest.raises(ValueError):

        User(
            name="Ana Rita",
            agency="0013",
            account="56789",
            current_balance=-1000
        )

#teste de nome inválido - vazio
def test_invalid_name():

    with pytest.raises(ValueError):

        User(
            name="",
            agency="0013",
            account="56789",
            current_balance=1000
        )

#teste do método de depósito
def test_deposit():

    user = User(
        name="Ana Rita",
        agency="0013",
        account="56789",
        current_balance=1000
    )

    user.deposit(50)
#verifica se o valor do depósito foi adicionado corretamente ao saldo
    assert user.current_balance == 1050

#testando método de depósito com valor inválido - negativo
def test_invalid_deposit():

    user = User(
        name="Ana Rita",
        agency="0013",
        account="56789",
        current_balance=1000
    )

    with pytest.raises(ValueError):

        user.deposit(-100)

#teste do método de saque
def test_withdraw():

    user = User(
        name="Ana Rita",
        agency="0013",
        account="56789",
        current_balance=1000
    )

    user.withdraw(300)

    assert user.current_balance == 700

#teste do método de saque com valor inválido - negativo
def test_insufficient_funds():

    user = User(
        name="Ana Rita",
        agency="0013",
        account="56789",
        current_balance=1000
    )

    with pytest.raises(ValueError):

        user.withdraw(2000)