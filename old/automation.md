# Automation Approach

## Test 1 — E2E UI: Bet Placement Flow

**Objective:** Validate complete betting flow from UI to confirmation.

**Steps:**
1. Open application with valid user-id  
2. Select a match outcome  
3. Enter a valid stake  
4. Click "Place Bet"  
5. Verify receipt  

**Expected Result:**
- Bet is successfully placed  
- Receipt shows correct stake, odds and payout  
- Balance is updated  

**Example (Playwright):**

    import { test, expect } from '@playwright/test';

    test('should place a bet successfully', async ({ page }) => {
      await page.goto('/?user-id=VALID_USER');

      await page.locator('[data-testid="odds-button"]').first().click();
      await page.fill('[data-testid="stake-input"]', '10');
      await page.click('[data-testid="place-bet-btn"]');

      await expect(page.locator('[data-testid="receipt-modal"]')).toBeVisible();
    });

---

## Test 2 — API: Stake Validation

**Objective:** Validate backend stake rules.

**Steps:**
1. Send POST request to `/api/place-bet`  
2. Use invalid stake (e.g. 0.5)  
3. Check response  

**Expected Result:**
- API rejects invalid stake  
- Returns HTTP 422  

**Example (Playwright API):**

    import { test, expect } from '@playwright/test';

    test('should reject invalid stake', async ({ request }) => {
      const response = await request.post('/api/place-bet', {
        headers: { 'x-user-id': 'VALID_USER' },
        data: {
          matchId: '123',
          selection: 'HOME',
          stake: 0.5
        }
      });

      expect(response.status()).toBe(422);
    });
