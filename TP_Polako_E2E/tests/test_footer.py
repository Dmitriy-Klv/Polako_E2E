import re
from playwright.sync_api import expect
from TP_Polako_E2E.base.base_test import BaseTest
from TP_Polako_E2E.pages.common.footer import FOOTER_NAV_LINKS


class TestFooter(BaseTest):

    def test_footer_logo_navigation(self):
        self.footer_page.verify_logo_navigation()

    def test_mobile_apps_buttons_visibility(self):
        self.footer_page.verify_app_store_visible()
        self.footer_page.verify_google_play_visible()

    def test_app_store_redirection(self):
        self.footer_page.verify_app_store_redirection()

    def test_google_play_redirection(self):
        self.footer_page.verify_google_play_redirection()

    def test_all_navigation_links_are_visible(self):
        for link_key in FOOTER_NAV_LINKS.keys():
            self.footer_page.verify_nav_link_visible(link_key)

    def test_contacts_social_links_integrity(self):
        tg_url = self.footer_page.get_contact_href("telegram")
        assert "t.me" in tg_url, f"Invalid address Telegram: {tg_url}"

        insta_ru = self.footer_page.get_contact_href("instagram_ru")
        assert "instagram.com" in insta_ru, f"Invalid domain Instagram: {insta_ru}"

        email = self.footer_page.get_contact_href("email")
        assert email.startswith("mailto:"), f"Expected mailto: protocol, received: {email}"

    def test_working_hours_content_integrity(self):
        self.footer_page.verify_working_hours_visible()
        hours_text = self.footer_page.get_working_hours_text()
        assert "11:00" in hours_text, f"Opening time not found: {hours_text}"
        assert "21:00" in hours_text, f"Closing time not found: {hours_text}"

    def test_legal_info_content_integrity(self):
        self.footer_page.verify_legal_info_visible()
        legal_text = self.footer_page.get_legal_info_text()
        assert "114165836" in legal_text, f"PIB not found: {legal_text}"
        assert "67370481" in legal_text, f"MB not found: {legal_text}"
