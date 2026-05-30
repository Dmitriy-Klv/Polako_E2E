from TP_Polako_E2E.base.base_page import BasePage

FOOTER_LOGO = 'footer img[alt="logo"]'

APP_STORE_BTN = 'footer img[alt="App Store"]'
GOOGLE_PLAY_BTN = 'footer img[alt="Google Play"]'

FOOTER_NAV_COLUMN = 'footer > div.grid > div:nth-child(2)'
FOOTER_NAV_LINKS = {
    "events": f'{FOOTER_NAV_COLUMN} > a:nth-of-type(1)',
    "vouchers": f'{FOOTER_NAV_COLUMN} > a:nth-of-type(2)',
    "organizers": f'{FOOTER_NAV_COLUMN} > a:nth-of-type(3)',
    "news": f'{FOOTER_NAV_COLUMN} > a:nth-of-type(4)',
    "documents": f'{FOOTER_NAV_COLUMN} > a:nth-of-type(5)',
    "terms": f'{FOOTER_NAV_COLUMN} > a:nth-of-type(6)',
    "return_policy": f'{FOOTER_NAV_COLUMN} > a:nth-of-type(7)',
    "mobile_ticket_scanner": f'{FOOTER_NAV_COLUMN} > a:nth-of-type(8)',
    "help": f'{FOOTER_NAV_COLUMN} > a:nth-of-type(9)',
    "ticket_scanner": f'{FOOTER_NAV_COLUMN} > a:nth-of-type(10)',
    "tickets": f'{FOOTER_NAV_COLUMN} > a:nth-of-type(11)',
    "sitemap": f'{FOOTER_NAV_COLUMN} > a:nth-of-type(12)',
}

FOOTER_CONTACTS_COLUMN = 'footer > div.grid > div:nth-child(3)'
FOOTER_CONTACT_LINKS = {
    "telegram": f'{FOOTER_CONTACTS_COLUMN} > a:nth-of-type(1)',
    "instagram_ru": f'{FOOTER_CONTACTS_COLUMN} > a:nth-of-type(2)',
    "instagram_sr": f'{FOOTER_CONTACTS_COLUMN} > a:nth-of-type(3)',
    "email": f'{FOOTER_CONTACTS_COLUMN} > a:nth-of-type(4)',
    "viber": f'{FOOTER_CONTACTS_COLUMN} > a:nth-of-type(5)',
    "whatsapp": f'{FOOTER_CONTACTS_COLUMN} > a:nth-of-type(6)',
}

WORKING_HOURS_TEXT = 'footer > div.grid > div:nth-child(4)'
LEGAL_INFO_TEXT = 'footer > div.grid > div:nth-child(5)'


class FooterPage(BasePage):

    # LOGO
    def click_logo(self):
        self.page.locator(FOOTER_LOGO).click()

    def verify_logo_visible(self):
        self.page.locator(FOOTER_LOGO).wait_for(state="visible", timeout=5000)

    # Mobile Apps
    def click_app_store(self):
        self.page.locator(APP_STORE_BTN).click()

    def verify_app_store_visible(self):
        self.page.locator(APP_STORE_BTN).wait_for(state="visible", timeout=4000)

    def click_google_play(self):
        self.page.locator(GOOGLE_PLAY_BTN).click()

    def verify_google_play_visible(self):
        self.page.locator(GOOGLE_PLAY_BTN).wait_for(state="visible", timeout=4000)

    # Navigation Links
    def click_nav_link(self, key_name: str):
        selector = FOOTER_NAV_LINKS[key_name.lower()]
        self.page.locator(selector).click()

    def verify_nav_link_visible(self, key_name: str):
        selector = FOOTER_NAV_LINKS[key_name.lower()]
        self.page.locator(selector).wait_for(state="visible", timeout=3000)

    # Contacts Links
    def get_contact_href(self, platform_name: str) -> str:
        selector = FOOTER_CONTACT_LINKS[platform_name.lower()]
        return self.page.locator(selector).get_attribute("href")

    def click_contact_link(self, platform_name: str):
        selector = FOOTER_CONTACT_LINKS[platform_name.lower()]
        self.page.locator(selector).click()

    # Working Hours
    def verify_working_hours_visible(self):
        self.page.locator(WORKING_HOURS_TEXT).wait_for(state="visible", timeout=4000)

    def get_working_hours_text(self) -> str:
        return self.page.locator(WORKING_HOURS_TEXT).inner_text()

    # Legal Info
    def verify_legal_info_visible(self):
        self.page.locator(LEGAL_INFO_TEXT).wait_for(state="visible", timeout=4000)

    def get_legal_info_text(self) -> str:
        return self.page.locator(LEGAL_INFO_TEXT).inner_text()
