from model_data.update_user_model import UpdateUser
from utils.random_data import fake_user_data


def unsuccessful_update():
    user_data = fake_user_data()
    return UpdateUser(email='', first_name=user_data['name'], last_name=user_data['surname'],
                      avatar=user_data['avatar'])


def successful_update():
    user_data = fake_user_data()
    return UpdateUser(email=user_data['email'], first_name=user_data['name'], last_name=user_data['surname'],
                      avatar=user_data['avatar'])
