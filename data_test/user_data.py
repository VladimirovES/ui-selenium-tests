from models.user import UserAccount
from utils.generator import GeneralGenerator, UserDataGenerator


class UserData:

    user1 = UserAccount()
    user2 = UserAccount()
    user_changes = UserAccount(userName=GeneralGenerator.generate_random_string(5), password='SomePassword!2021')

    all_users = (user1, user2)