from src.app.entities.transaction import Transaction


def test_transaction():

    transaction = Transaction(
        transaction_type="deposit",
        value=100,
        current_balance=1000
    )

    assert transaction.transaction_type == "deposit"
    assert transaction.value == 100
    assert transaction.current_balance == 1000