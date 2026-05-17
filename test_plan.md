# Test Plan — Single Bet Placement Feature

## TC-01 — Successful Bet Placement (Happy Path)

**Priority:** Critical  

**Risk Rationale:**  
Core business flow involving financial transactions. Any issue directly affects user trust and revenue.

**Steps:**
1. Open the application with a valid user-id
2. Select a match
3. Choose an outcome (1 / X / 2)
4. Enter a valid stake (e.g., €10)
5. Click "Place Bet"

**Expected Result:**
- Bet is successfully placed
- Receipt is displayed with correct:
  - Match
  - Selection mapping (1=Home, X=Draw, 2=Away)
  - Stake
  - Odds
  - Payout (stake × odds)
- Balance is deducted correctly
- Bet slip is cleared


---

## TC-02 — Stake Validation (Boundary & Invalid Inputs)

**Priority:** Critical  

**Risk Rationale:**  
Invalid stake values can lead to incorrect financial transactions.

**Steps:**
1. Select a match and outcome
2. Enter invalid stake values:
   - Below minimum (€0.50)
   - Above maximum (€150)
   - Non-numeric input ("abc")
   - More than 2 decimal places
3. Attempt to place bet

**Expected Result:**
- System blocks the action
- Proper validation messages are displayed
- No bet is placed


---

## TC-03 — Insufficient Balance Handling

**Priority:** High  

**Risk Rationale:**  
Prevents users from betting more than available balance.

**Steps:**
1. Note available balance
2. Select a match and outcome
3. Enter stake greater than balance
4. Attempt to place bet

**Expected Result:**
- Bet is blocked
- Error message "Insufficient balance"
- Balance remains unchanged


---

## TC-04 — Selection Replacement

**Priority:** High  

**Risk Rationale:**  
Ensures only one active bet is maintained.

**Steps:**
1. Select an outcome for a match
2. Select another outcome (same or different match)

**Expected Result:**
- Previous selection is replaced
- Only one selection shown in bet slip


---

## TC-05 — Error Handling on Bet Placement

**Priority:** High  

**Risk Rationale:**  
Ensures system stability when backend fails.

**Steps:**
1. Attempt to place a bet when API returns error
2. Observe error modal
3. Click "Rebet" and "Close"

**Expected Result:**
- Error modal appears
- Rebet retries request
- Close clears bet slip


---

## TC-06 — Event Suspension After Kickoff

**Priority:** Critical  

**Risk Rationale:**  
Prevents invalid bets on already started events (compliance risk).

**Steps:**
1. Select a match before kickoff
2. Attempt to place bet after kickoff time

**Expected Result:**
- Betting is blocked
- Event marked as unavailable
- Appropriate error shown
