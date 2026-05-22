from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BetPage:

    def __init__(self, driver):
        self.driver = driver

    def select_first_match_home(self):
        self.driver.find_elements(By.CSS_SELECTOR, ".odds-button")[0].click()

    def enter_stake(self, amount):
        stake_input = self.driver.find_element(By.CSS_SELECTOR, "input[data-testid='stake-input']")
        stake_input.clear()
        stake_input.send_keys(str(amount))

    def place_bet(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='place-bet']").click()

    def get_receipt(self):
        modal = self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='receipt-modal']")
        return modal.text

