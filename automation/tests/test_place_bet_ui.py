from automation.pages.bet_page import BetPage

def test_place_valid_bet(driver):
    """
    Critical E2E: placing a valid bet verifies the core revenue flow.
    """
    page = BetPage(driver)

    page.select_first_match_home()
    page.enter_stake(10)
    page.place_bet()

    receipt = page.get_receipt()

    assert "Bet ID" in receipt
    assert "Stake: €10.00" in receipt

