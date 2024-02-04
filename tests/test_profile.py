from data_test.user_data import UserData


class TestProfile:

    def test_user_name_eql(self, profile_page):
        profile_page.auth(user=UserData.user1).open_page()
