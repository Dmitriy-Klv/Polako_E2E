from TP_Polako_E2E.base.base_page import BasePage

EVENT_CARD = '[data-testid="event-card"]'
EVENT_TITLE = ".event-card__title"
FILTER_BUTTON = "button.filters-trigger"
SEARCH_INPUT = 'input[placeholder*="search"]'


class EventsListPage(BasePage):
    def search_event(self, query: str):
        self.fill(SEARCH_INPUT, query)
        self.page.keyboard.press("Enter")

    def open_event_by_index(self, index: int = 0):
        self.page.locator(EVENT_CARD).nth(index).click()

    def get_all_event_titles(self):
        return self.page.locator(EVENT_TITLE).all_inner_texts()
