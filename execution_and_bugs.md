
# Execution Results & Bug Reports

## Execution Summary

Execution of selected test scenarios was blocked due to a critical authentication issue.

Attempts to access:
- /api/matches
- /api/balance

Resulted in:
- 401 Unauthorized
- error: invalid_user_id

---

## BUG-01 — Invalid User ID Handling Blocks Application Usage

**Severity:** Critical  

### Reproduction Steps:
1. Open application with any user-id (e.g., ?user-id=test123)
2. Open DevTools → Network tab
3. Observe API calls

### Expected Result:
- System should accept user-id
- Matches and balance should load

### Actual Result:
- API returns 401 Unauthorized
- Response: invalid_user_id
- UI shows no matches and €0 balance
- Header X-User-Id is correctly sent but still rejected

### Business Impact:
- User cannot access the platform
- Core functionality completely blocked


### Evidence:
- Network requests return 401 Unauthorized despite valid X-User-Id

Captura de pantalla 2026-05-17 225528.png


---

## BUG-02 — Poor Handling of Unauthorized State in UI

**Severity:** High  

### Reproduction Steps:
1. Access application with invalid user-id
2. Observe UI state

### Expected Result:
- Clear error message explaining issue
- Guidance on how to recover

### Actual Result:
- UI displays "Unauthorized"
- No explanation or recovery option
- Balance incorrectly displayed as €0.00

### Business Impact:
- Poor user experience
- User unable to understand or resolve issue


### Evidence:
- UI shows unauthorized state with no matches and incorrect balance display

Captura de pantalla 2026-05-17 225528.png


## BUG-02 — Poor unauthorized handling

Severity: High

UI shows unclear error and no recovery actions.
