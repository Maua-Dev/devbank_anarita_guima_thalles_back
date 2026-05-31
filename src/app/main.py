from fastapi import FastAPI, HTTPException
from mangum import Mangum

from src.app.entities.user import User
from src.app.repo.user_repository_mock import UserRepositoryMock

app = FastAPI()

repo = UserRepositoryMock()


@app.get("/")
def home():
    return {"message": "DevBank API"}


@app.get("/users")
def get_all_users():

    return {
        "users": [user.to_dict() for user in repo.get_all_users()]
    }


@app.get("/users/{account}")
def get_user(account: str):

    user = repo.get_user_by_account(account)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user.to_dict()


@app.post("/users/create", status_code=201)
def create_user(request: dict):

    account = request.get("account")

    user_exists = repo.get_user_by_account(account)

    if user_exists is not None:
        raise HTTPException(
            status_code=409,
            detail="User already exists"
        )

    try:

        user = User(
            name=request.get("name"),
            agency=request.get("agency"),
            account=account,
            current_balance=request.get("current_balance", 0)
        )

    except ValueError as err:

        raise HTTPException(
            status_code=400,
            detail=str(err)
        )

    repo.create_user(user)

    return user.to_dict()


@app.post("/users/deposit")
def deposit(request: dict):

    account = request.get("account")
    value = request.get("value")

    user = repo.get_user_by_account(account)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    try:

        user.deposit(value)

    except ValueError as err:

        raise HTTPException(
            status_code=400,
            detail=str(err)
        )

    return user.to_dict()


@app.post("/users/withdraw")
def withdraw(request: dict):

    account = request.get("account")
    value = request.get("value")

    user = repo.get_user_by_account(account)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    try:

        user.withdraw(value)

    except ValueError as err:

        raise HTTPException(
            status_code=400,
            detail=str(err)
        )

    return user.to_dict()

@app.get("/users/{account}/transactions")
def get_transactions(account: str):

    user = repo.get_user_by_account(account)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "all_transactions": [
            transaction.to_dict()
            for transaction in user.transactions
        ]
    }

handler = Mangum(app, lifespan="off")
