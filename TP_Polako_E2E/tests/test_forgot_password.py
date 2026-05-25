from TP_Polako_E2E.base.base_test import BaseTest
from TP_Polako_E2E.utils.constants import INVALID_EMAILS, EMAIL_ADDRESS


class TestForgotPassword(BaseTest):

    def test_forgot_password_success(self):
        """
        Positive Test: Successfully request password recovery.
        Expected Result: Appearance of a modal window displaying a success message.
        """
        self.login_page.open_login_modal()
        self.login_page.click_forgot_password()

        self.forgot_password_page.fill_recovery_email(EMAIL_ADDRESS)
        self.forgot_password_page.click_send_button()

        self.forgot_password_page.verify_recovery_success_message(EMAIL_ADDRESS)

    def test_forgot_password_invalid_email(self):
        """
        Negative Test: Attempting to Reset Password with an invalid email format.
        Expected Result: Appearance of an email format validation error message.
        """
        self.login_page.open_login_modal()
        self.login_page.click_forgot_password()

        # Используем первый невалидный email для примера
        invalid_email = INVALID_EMAILS[0]
        self.forgot_password_page.fill_recovery_email(invalid_email)
        self.forgot_password_page.click_send_button()

        self.forgot_password_page.verify_email_format_error_message()
