from TP_Polako_E2E.pages.profile.user_profile_page import UserProfilePage

# WARNING BANNER
TOP_WARNING_BANNER = "main > div.bg-yellow-50, div:has-text('Завершите настройку')"  # Корректируй под точный класс
FILL_DATA_BTN = "button:has-text('Заполнить данные')"
CREATE_CONTRACT_BTN = "button:has-text('Создать договор')"

# BADGES
ORGANIZER_ROLE_BADGE = "main div.gap-1 span:nth-of-type(1)"  # Бейдж "Менеджер"
COMMISSION_BADGE = "main div.gap-1 span:nth-of-type(2)"      # Бейдж "Комиссия платформы..."

# SIDEBAR
COMPANY_BTN = 'nav a[href*="company"]'
MANAGE_EVENTS_BTN = 'nav a[href*="events"]'
CONTRACT_DATA_BTN = 'nav a[href*="contract-data"]'  # Данные для договоров
CONTRACTS_BTN = 'nav a[href*="contracts"]'          # Договоры
REPORTS_BTN = 'nav a[href*="reports"]'              # Отчеты
QR_CODE_BTN = 'nav a[href*="qr-code"]'              # Создать QR-код
WITHDRAW_BTN = 'nav a[href*="withdraw"]'            # Вывод средств
PUBLICATIONS_BTN = 'nav a[href*="publications"]'    # Публикации
MANAGE_BTN = 'nav a[href*="manage"]'                # Управление


class ManagerProfilePage(UserProfilePage):
    # Badges
    def verify_user_role_badge(self):
        self.page.locator(ORGANIZER_ROLE_BADGE).wait_for(state="visible", timeout=4000)

    def verify_commission_badge_visible(self, timeout: int = 3000):
        self.page.locator(COMMISSION_BADGE).wait_for(state="visible", timeout=timeout)

    def get_commission_text(self) -> str:
        return self.page.locator(COMMISSION_BADGE).text_content().strip()

    # Warning Banner
    def verify_warning_banner_visible(self, timeout: int = 3000):
        self.page.locator(TOP_WARNING_BANNER).wait_for(state="visible", timeout=timeout)

    def click_banner_fill_data(self):
        self.page.locator(FILL_DATA_BTN).click()

    def click_banner_create_contract(self):
        self.page.locator(CREATE_CONTRACT_BTN).click()

    # SIDEBAR
    def click_company_btn(self):
        self.page.locator(COMPANY_BTN).click()

    def verify_company_btn_visible(self):
        self.page.locator(COMPANY_BTN).wait_for(state="visible")

    def click_event_management_link(self):
        self.page.locator(MANAGE_EVENTS_BTN).click()

    def verify_event_management_link_visible(self):
        self.page.locator(MANAGE_EVENTS_BTN).wait_for(state="visible")

    def click_contract_data_btn(self):
        self.page.locator(CONTRACT_DATA_BTN).click()

    def verify_contract_data_btn_visible(self):
        self.page.locator(CONTRACT_DATA_BTN).wait_for(state="visible")

    def click_contracts_btn(self):
        self.page.locator(CONTRACTS_BTN).click()

    def verify_contracts_btn_visible(self):
        self.page.locator(CONTRACTS_BTN).wait_for(state="visible")

    def click_reports_btn(self):
        self.page.locator(REPORTS_BTN).click()

    def verify_reports_btn_visible(self):
        self.page.locator(REPORTS_BTN).wait_for(state="visible")

    def click_qr_code_btn(self):
        self.page.locator(QR_CODE_BTN).click()

    def verify_qr_code_btn_visible(self):
        self.page.locator(QR_CODE_BTN).wait_for(state="visible")

    def click_withdraw_btn(self):
        self.page.locator(WITHDRAW_BTN).click()

    def verify_withdraw_btn_visible(self):
        self.page.locator(WITHDRAW_BTN).wait_for(state="visible")

    def click_publications_btn(self):
        self.page.locator(PUBLICATIONS_BTN).click()

    def verify_publications_btn_visible(self):
        self.page.locator(PUBLICATIONS_BTN).wait_for(state="visible")

    def click_manage_btn(self):
        self.page.locator(MANAGE_BTN).click()

    def verify_manage_btn_visible(self):
        self.page.locator(MANAGE_BTN).wait_for(state="visible")
