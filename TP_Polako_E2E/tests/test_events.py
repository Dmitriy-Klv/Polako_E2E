from TP_Polako_E2E.base.base_test import BaseTest


class TestEvent(BaseTest):

    def test_create_event_button_is_clickable(self):
        self.login_page.login_as_valid_user()
        self.login_page.click_profile()

        self.user_profile.click_event_management_link()

        self.events_list.create_event_btn_is_visible()
        self.events_list.click_create_event_btn()
