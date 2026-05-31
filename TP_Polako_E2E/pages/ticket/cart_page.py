from TP_Polako_E2E.base.base_page import BasePage

CART_BADGE = '(//button[@aria-label="Cart"])[1]'
REMOVE_TICKET_BUTTON = '//button[@aria-label="Remove"]'
EMPTY_CART_MESSAGE = ".text-sm.font-medium.text-gray-700"
CLEAR_CART_BUTTON = "(//button[contains(@class, 'text-gray-400')])[2]"

class CartPage(BasePage):

    def verify_cart_is_visible(self):
        self.expect(self.page.locator(CART_BADGE)).to_be_visible()

    def remove_ticket(self):
        self.page.locator(REMOVE_TICKET_BUTTON).wait_for(
            state="visible",
            timeout=10000
        )
        self.page.locator(REMOVE_TICKET_BUTTON).click()

    def verify_cart_is_empty(self):
        self.expect(self.page.locator(EMPTY_CART_MESSAGE)).to_be_visible(timeout=5000)

    def clear_all_tickets(self):
        clear_button = self.page.locator(CLEAR_CART_BUTTON)

        clear_button.wait_for(state="visible", timeout=10000)
        clear_button.click()