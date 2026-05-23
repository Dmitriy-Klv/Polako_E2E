from TP_Polako_E2E.base.base_page import BasePage

USER_SIDEBAR_LINKS = {
    "profile": 'aside a:has-text("Профиль")',
    "purchase_history": 'aside a:has-text("История покупок")',
    "balance": 'aside a:has-text("Баланс")'
}

USER_ROLE_BADGE = 'span:has-text("Пользователь")'
LOGOUT_BTN = 'button:has-text("Выйти")'
EXIT_BTN = "//button[@type='button' and @data-slot='button']"

INFO_CONTAINER = 'div:has-text("Основная информация")'
FIRST_NAME_INPUT = 'div:has-text("Основная информация") ~ div div:nth-child(1) input'
LAST_NAME_INPUT = 'div:has-text("Основная информация") ~ div div:nth-child(2) input'

EMAIL_INPUT = 'input[type="email"]'
PHONE_INPUT = 'input[type="tel"]'
INSTAGRAM_INPUT = 'div:has-text("Контактная информация") ~ div div:nth-child(3) input'
TELEGRAM_INPUT = 'div:has-text("Контактная информация") ~ div div:nth-child(4) input'

SAVE_PROFILE_BTN = 'button:has-text("Сохранить")'

NEW_PASSWORD_INPUT = 'input[placeholder="Введите новый пароль"]'
CONFIRM_PASSWORD_INPUT = 'input[placeholder="Подтвердите пароль"]'
CHANGE_PASSWORD_BTN = 'button:has-text("Изменить пароль")'

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
    def fill_all_profile_fields(self, const_first_name: str, const_last_name: str, const_phone: str,
                                const_instagram: str, const_telegram: str):
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
