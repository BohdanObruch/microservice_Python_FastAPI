from model_data.create_user_model import User
from utils.random_data import generate_random_data
from api.user_api import UserApi

existing_ids = [user["id"] for user in UserApi().read_users()]


def create_user_data():
    id, email, first_name, last_name, avatar = generate_random_data(existing_ids)
    return User(
        id=id,
        email=email,
        first_name=first_name,
        last_name=last_name,
        avatar=avatar
    )


USER_DATA = create_user_data()
