from models.user import UserAccount
from utils.generator import GeneralGenerator


class UserData:

    user1 = UserAccount()
    user2 = UserAccount()
    user_changes = UserAccount(userName=f'TestDelete+{GeneralGenerator.generate_random_string(4)}', password='SomePassword!2021')

    all_users = (user1, user2)