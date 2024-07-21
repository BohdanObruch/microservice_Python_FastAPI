from model_data.register_user_model import RegisterUser
from utils.random_data import fake_user_data

data = fake_user_data()

UNSUCCESSFUL_REGISTER = RegisterUser(email='', first_name=data['name'])

SUCCESSFUL_REGISTER = RegisterUser(email=data['email'], first_name=data['name'])
