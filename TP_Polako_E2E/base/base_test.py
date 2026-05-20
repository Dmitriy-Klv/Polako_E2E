import pytest

from TP_Polako_E2E.pages.auth.login_page import LoginPage
from TP_Polako_E2E.pages.events.events_list_page import EventsListPage
from TP_Polako_E2E.pages.profile.user_profile_page import UserProfilePage


class BaseTest:
    login_page: LoginPage
    user_profile: UserProfilePage
    events_list: EventsListPage

    @pytest.fixture(autouse=True)
    def setup_pages(self, app_page):
        self.page = app_page
        self.login_page = LoginPage(app_page)
        self.user_profile = UserProfilePage(app_page)
        self.events_list = EventsListPage(app_page)
