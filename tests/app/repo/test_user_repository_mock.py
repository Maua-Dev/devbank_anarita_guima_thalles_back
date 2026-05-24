from src.app.entities.user import User
from src.app.repo.user_repository_mock import UserRepositoryMock

#verifica se o usuário foi criado corretamente
def test_create_user():

    repository = UserRepositoryMock()

    user = User(
        name="Ana Rita",
        agency="0013",
        account="56789",
        current_balance=1000
    )

    repository.create_user(user)

    assert len(repository.users) == 1

#verifica se é possível puxar um usuário pelo número da conta
def test_get_user_by_account():

    repository = UserRepositoryMock()

    user = User(
        name="Ana Rita",
        agency="0013",
        account="56789",
        current_balance=1000
    )

    repository.create_user(user)

    found_user = repository.get_user_by_account("56789")

    assert found_user == user

#verifica se retorna none com usuário inexistente
def test_get_nonexistent_user():

    repository = UserRepositoryMock()

    found_user = repository.get_user_by_account("99999")

    assert found_user is None