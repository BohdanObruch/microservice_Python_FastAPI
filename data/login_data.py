from model_data.login_user_model import LoginUser
from utils.random_data import fake_user_data

data = fake_user_data()

UNSUCCESSFUL_LOGIN = LoginUser(email='')
SUCCESSFUL_LOGIN = LoginUser(email=data['email'])
