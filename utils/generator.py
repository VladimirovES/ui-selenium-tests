import random
import string

from faker import Faker
class GeneralGenerator:

    @staticmethod
    def generate_random_string(length=10):
        return "".join(random.choice(string.ascii_lowercase) for _ in range(length))

class UserDataGenerator:
    fake = Faker()

    @staticmethod
    def generate_first_name():
        return UserDataGenerator.fake.first_name()

    @staticmethod
    def generate_last_name():
        return UserDataGenerator.fake.last_name()

    @staticmethod
    def generate_user_name():
        return UserDataGenerator.fake.user_name()

    @staticmethod
    def generate_password(length=10):
        password = [
            random.choice(string.punctuation),
            random.choice(string.digits),
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase)
        ]

        remaining_length = length - len(password)

        remaining_characters = list(string.ascii_letters + string.digits + string.punctuation)
        random.shuffle(remaining_characters)

        password.extend(remaining_characters[:remaining_length])

        random.shuffle(password)

        return ''.join(password)


