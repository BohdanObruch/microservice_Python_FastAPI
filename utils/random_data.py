from faker import Faker
import random


def generate_random_data(existing_ids):

    new_id = random.randint(1, 1000)
    while new_id in existing_ids:
        new_id = random.randint(1, 1000)
    fake = Faker()
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    avatar = fake.image_url()

    return new_id, email, first_name, last_name, avatar


def get_existing_user_id():
    from api.user_api import UserApi
    users = UserApi().read_users()
    return random.choice(users)["id"]


def get_non_existing_user_id():
    from api.user_api import UserApi
    users = UserApi().read_users()
    existing_ids = [user["id"] for user in users]
    while True:
        id = Faker().random_int(min=1, max=1000)
        if id not in existing_ids:
            break
    return id


def fake_user_data():
    fake = Faker()
    token = fake.sha256()
    email_user = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    avatar = fake.image_url()
    data = {
        "token": token,
        "email": email_user,
        "name": first_name,
        "surname": last_name,
        "avatar": avatar
    }
    return data
