import random
import string

from faker import Faker


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
            random.choice(string.punctuation),  # Специальный символ
            random.choice(string.digits),  # Цифра
            random.choice(string.ascii_uppercase),  # Заглавная буква
            random.choice(string.ascii_lowercase)  # Строчная буква
        ]

        # Гарантируем, что все требования выполнены
        remaining_length = length - len(password)

        # Перемешиваем все доступные символы для оставшихся позиций
        remaining_characters = list(string.ascii_letters + string.digits + string.punctuation)
        random.shuffle(remaining_characters)

        # Добавляем оставшиеся символы
        password.extend(remaining_characters[:remaining_length])

        # Перемешиваем итоговый пароль
        random.shuffle(password)

        return ''.join(password)


