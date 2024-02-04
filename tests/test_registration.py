
from models.user import User


class TestRegistration:

    def test_valid_data_reg(self, registration_page):
        # Act
        registration_page.open_page()
        registration_page.registration_user(user=User())

        # Assert



