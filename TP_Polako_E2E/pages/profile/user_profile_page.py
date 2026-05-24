from TP_Polako_E2E.base.base_page import BasePage

USER_SIDEBAR_LINKS = {
    "profile": 'nav a[href*="personal-information"]',
    "purchase_history": 'nav a[href*="purchases"]',
    "balance": 'nav a[href*="balance"]',
}

USER_ROLE_BADGE = "nav ~ div div.gap-1 span"
LOGOUT_BTN = "main div.rounded-2xl button"
EXIT_BTN = "//button[@type='button' and @data-slot='button']"

BASIC_INFO = "form:has(#first_name) > p:nth-of-type(1)"
FIRST_NAME_INPUT = "#first_name"
LAST_NAME_INPUT = "#last_name"

CONTACT_INFO = "form:has(#first_name) > p:nth-of-type(2)"
EMAIL_INPUT = "#email"
PHONE_INPUT = "#phone"
INSTAGRAM_INPUT = "#instagram"
TELEGRAM_INPUT = "#telegram"

SAVE_PROFILE_BTN = 'form:has(#first_name) button[type="submit"]'

CHANGE_PASSWORD = "main form:nth-of-type(2) > p"
NEW_PASSWORD_INPUT = "#new_password"
CONFIRM_PASSWORD_INPUT = "#confirm_password"
CHANGE_PASSWORD_BTN = 'main form:nth-of-type(2) button[type="submit"]'

EVENT_MNG_BTN = 'a[href="/ru/user/events"]'


class UserProfilePage(BasePage):
    def verify_logout_button_visible(self):
        self.verify_element_is_visible(selector=EXIT_BTN, element_name="Logout Button")

    def click_event_management_link(self):
        self.page.click(EVENT_MNG_BTN)

    # SIDEBAR
    def click_sidebar_menu(self, menu_key: str):
        selector = USER_SIDEBAR_LINKS[menu_key.lower()]
        self.page.locator(selector).click()

    def verify_sidebar_link_visible(self, menu_key: str):
        selector = USER_SIDEBAR_LINKS[menu_key.lower()]
        self.page.locator(selector).wait_for(state="visible", timeout=3000)

    # PROFILE INFORMATION
    def verify_user_role_badge(self):
        self.page.locator(USER_ROLE_BADGE).wait_for(state="visible", timeout=4000)

    def click_logout(self):
        self.page.locator(LOGOUT_BTN).click()

    def verify_logout_button_visible2(self):
        self.page.locator(LOGOUT_BTN).wait_for(state="visible", timeout=4000)

    # MANAGE PROFILE
    def fill_all_profile_fields(
        self,
        const_first_name: str,
        const_last_name: str,
        const_phone: str,
        const_instagram: str,
        const_telegram: str,
    ):
        if const_first_name:
            self.page.locator(FIRST_NAME_INPUT).fill(const_first_name)
        if const_last_name:
            self.page.locator(LAST_NAME_INPUT).fill(const_last_name)
        if const_phone:
            self.page.locator(PHONE_INPUT).fill(const_phone)
        if const_instagram:
            self.page.locator(INSTAGRAM_INPUT).fill(const_instagram)
        if const_telegram:
            self.page.locator(TELEGRAM_INPUT).fill(const_telegram)

    def get_email_value(self) -> str:
        return self.page.locator(EMAIL_INPUT).input_value()

    def click_save_profile(self):
        self.page.locator(SAVE_PROFILE_BTN).click()

    # CHANGE PASSWORD
    def fill_and_submit_new_password(self, const_new_pass: str):
        self.page.locator(NEW_PASSWORD_INPUT).fill(const_new_pass)
        self.page.locator(CONFIRM_PASSWORD_INPUT).fill(const_new_pass)
        self.page.locator(CHANGE_PASSWORD_BTN).click()
