

class TestProfile:

    def test_nickname_user(self, profile_page):
        # Act
        profile_page.auth(user=UserData.user1).open_page()

        # Assert
        profile_page.username.assert_text_eql(expected=UserData.user1.userName)