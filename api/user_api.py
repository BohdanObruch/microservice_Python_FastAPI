from datetime import datetime, timezone

from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
import json

from model_data.create_user_model import User
from model_data.register_user_model import RegisterUser
from model_data.login_user_model import LoginUser

from utils.paths import path_file
from utils.random_data import fake_user_data

data = fake_user_data()

router = APIRouter()


class UserApi:
    _URL = 'http://127.0.0.1:8000'

    @staticmethod
    def read_users():
        with open(path_file('users.txt'), 'r') as file:
            return json.load(file)

    @staticmethod
    def write_users(users):
        with open(path_file('users.txt'), 'w') as file:
            json.dump(users, file)

    def update_user(self, user_id: int, user: dict):
        users = self.read_users()
        for existing_user in users:
            if existing_user["id"] == user_id:
                existing_user.update(user)
                existing_user["updatedAt"] = datetime.now(timezone.utc).isoformat()
                self.write_users(users)
                return JSONResponse(content=existing_user, status_code=200)
        return JSONResponse(content={"detail": "User not found"}, status_code=404)

    @router.get("/users", response_model=list[User], summary="Get all users", description="Retrieve a list of all users.")
    def get_users(self):
        users = self.read_users()
        return Response(content=json.dumps(users), status_code=200, media_type="application/json")

    @router.get("/users/{user_id}", response_model=User, summary="Get user by ID", description="Retrieve a user by their ID.")
    def get_user(self, user_id: int):
        users = self.read_users()
        for user in users:
            if user["id"] == user_id:
                return JSONResponse(content=user, status_code=200)
        return JSONResponse(content={"detail": "User not found"}, status_code=404)

    @router.post("/users", response_model=User, summary="Create a new user", description="Create a new user with the provided details.")
    def create_user(self, user: dict):
        # Validate required fields
        required_fields = ["first_name", "email"]
        for field in required_fields:
            if field not in user:
                return Response(content=json.dumps({"detail": f"Missing {field}"}), status_code=400,
                                media_type="application/json")

        users = self.read_users()
        users.append(user)
        self.write_users(users)
        return Response(content=json.dumps(user), status_code=201, media_type="application/json")

    @router.delete("/users/{user_id}", response_model=dict, summary="Delete user by ID", description="Delete a user by their ID.")
    def delete_user(self, user_id: int):
        users = self.read_users()
        for user in users:
            if user["id"] == user_id:
                users.remove(user)
                self.write_users(users)
                return Response(content=json.dumps({"message": "User deleted"}), status_code=204,
                                media_type="application/json")
        return Response(content=json.dumps({"detail": "User not found"}), status_code=404,
                        media_type="application/json")

    @router.post("/register", response_model=dict, summary="Register a new user", description="Register a new user with the provided details.")
    def register(self, user: dict):
        user = RegisterUser(**user)
        if not user.email:
            return Response(content=json.dumps({"detail": "Missing email"}), status_code=400,
                            media_type="application/json")
        return Response(content=json.dumps({"message": "Successfully registered"}), status_code=200,
                        media_type="application/json")

    @router.post("/login", response_model=dict, summary="Login a user", description="Login a user with the provided credentials.")
    def login(self, user: dict):
        user = LoginUser(**user)
        if not user.email:
            return Response(content=json.dumps({"detail": "Missing email"}), status_code=400,
                            media_type="application/json")
        return Response(
            content=json.dumps({"message": "Successfully logged in", "token": data['token'],
                                "user": user.model_dump()}),
            status_code=200, media_type="application/json")

    @router.put("/users/{user_id}", response_model=User, summary="Update user by ID (PUT)", description="Update an existing user by their ID using PUT method.")
    def update_put_user(self, user_id: int, user: dict):
        return self.update_user(user_id, user)

    @router.patch("/users/{user_id}", response_model=dict, summary="Update user by ID (PATCH)", description="Update an existing user by their ID using PATCH method.")
    def update_patch_user(self, user_id: int, user: dict):
        return self.update_user(user_id, user)


user_api = UserApi()