
from data_test.user_data import UserData


class TestProfile:

    def test_nickname_user(self, profile_page):
        # Act
        profile_page.auth(user=UserData.user1).open_page()

        # Assert
        profile_page.username.assert_text_eql(expected=UserData.user1.userName)

    def test_logout_user(self, profile_page):
        # Act
        profile_page.auth(user=UserData.user1).open_page()
        profile_page.log_out.click()

        # Assert

    def test_login(self):
        pass
    # @pytest.mark.parametrize('value', [Books.js, Boks])
    # def test_search_books(self, profile_page, value):
    #     #Act
    #     profile_page.auth(user=UserData.user1).open_page()
    #     profile_page.input_search_book.fill(text=value)

