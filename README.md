# QA Assignment — Single Bet Placement

## Overview
This repository contains QA deliverables for a sports betting application, focusing on risk-based testing and defect analysis.

## Contents
- Test Plan (`test_plan.md`)
- Execution Results & Bug Reports (`execution_and_bugs.md`)
- Automation Strategy and Technical Decisions  

## Execution Summary
Execution was partially blocked due to an authentication issue (`invalid_user_id`) that prevented access to core system functionality.

Despite this, the investigation identified:
- A critical system-level defect affecting user access
- Gaps between specification and implementation
- Weak error handling in the UI

## Key Findings
- The system requires pre-existing user identifiers, which are not documented
- API consistently returns `401 Unauthorized`
- Application becomes unusable without valid user context

## Approach
The testing approach focused on:
- Risk-based prioritization
- Financial validation scenarios
- System behavior under failure conditions

## Notes
AI tools were used as a supporting aid to improve clarity and structure, without replacing reasoning, decision-making, hands-on experience, or empirical validation.

## Status
Submission complete. Further execution pending resolution of authentication issue.

