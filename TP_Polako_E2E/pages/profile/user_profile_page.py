from TP_Polako_E2E.base.base_page import BasePage


class UserProfilePage(BasePage):
    EXIT_BTN = "//button[@type='button' and @data-slot='button']"

    def verify_logout_button_visible(self):
        self.verify_element_is_visible(
            selector=self.EXIT_BTN, element_name="Logout Button"
        )
