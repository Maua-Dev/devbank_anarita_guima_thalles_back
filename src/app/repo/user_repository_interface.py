from abc import ABC, abstractmethod
from src.app.entities.user import User


class UserRepositoryInterface(ABC):

#todo usuário precisa dos métodos: criação de usuário e busca de usuário por conta
    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def get_user_by_account(self, account: str):
        pass