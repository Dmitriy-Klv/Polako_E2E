import pytest

from TP_Polako_E2E.utils.constants import (
    EXPECTED_ERROR_TEXT_COMPANY_NAME,
    LONG_COMPANY_NAME,
    TEST_EMAIL,
    TEST_NAME,
    VALID_COMPANY_NAME,
    VALID_TEST_PASSWORD,
    VALID_RANDOM_USERS_DATA,
    INVALID_PASSWORD,
)

from TP_Polako_E2E.base.base_test import BaseTest
from TP_Polako_E2E.pages.auth.registration_page import REGISTER_BTN


class TestRegistration(BaseTest):

    @pytest.mark.xfail(reason="Blocked by CAPTCHA limitation")
    def test_positive_manager_registration(self):

        self.login_page.open_login_modal()
        self.registration_page.for_organization_to_click()
        self.registration_page.fill_first_step_form(
            VALID_RANDOM_USERS_DATA[0],
            VALID_RANDOM_USERS_DATA[3],
            VALID_RANDOM_USERS_DATA[1],
        )
        self.registration_page.fill_company_name(VALID_RANDOM_USERS_DATA[2])
        self.registration_page.click_register()
        self.registration_page.verify_success_registration()

    def test_invalid_company_name_registration(self):
        self.login_page.open_login_modal()
        self.registration_page.for_organization_to_click()
        self.registration_page.fill_first_step_form(
            VALID_RANDOM_USERS_DATA[0],
            VALID_RANDOM_USERS_DATA[3],
            VALID_RANDOM_USERS_DATA[1],
        )
        self.registration_page.fill_company_name(LONG_COMPANY_NAME)
        self.registration_page.verify_company_name_error_visible(
            EXPECTED_ERROR_TEXT_COMPANY_NAME
        )

        assert self.page.locator(REGISTER_BTN).is_disabled()

    @pytest.mark.xfail(reason="Blocked by CAPTCHA limitation")
    def test_email_has_already_been_registered(self):
        self.login_page.open_login_modal()
        self.registration_page.for_organization_to_click()
        self.registration_page.fill_first_step_form(
            TEST_EMAIL, VALID_TEST_PASSWORD, TEST_NAME
        )
        self.registration_page.fill_company_name(VALID_COMPANY_NAME)
        self.registration_page.click_register()
        self.registration_page.verify_failure_inform_message_company_registration()

    def test_company_registration_with_empty_fields(self):
        self.login_page.open_login_modal()
        self.registration_page.for_organization_to_click()
        self.registration_page.verify_next_button_is_disabled()
        self.page.pause()

    def test_company_registration_with_password_error_not_displayed(self):
        self.login_page.open_login_modal()
        self.registration_page.for_organization_to_click()
        self.registration_page.fill_first_step_form(
            VALID_RANDOM_USERS_DATA[0],
            INVALID_PASSWORD[5],
            VALID_RANDOM_USERS_DATA[1],
            submit_form=False,
        )
        self.registration_page.verify_password_error_is_not_visible()
