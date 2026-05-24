from src.app.entities.user import User
from src.app.repo.user_repository_interface import UserRepositoryInterface


class UserRepositoryMock(UserRepositoryInterface):

    def __init__(self):
#lista de usuários para armazenamento dos dados
        self.users = []
#adiciona novo usuário à lista
    def create_user(self, user: User):

        self.users.append(user)
#verfica se o usuário está presente na lista de usuários
    def get_user_by_account(self, account: str):

        for user in self.users:
#cas esteja presente, retorna o usuário
            if user.account == account:
                return user
#caso contrário, retorna None
        return None