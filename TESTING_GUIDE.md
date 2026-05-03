# 🧪 TESTING GUIDE – SIRIUS LOCAL AI (v2.0.0)

This document defines the testing strategy, procedures, and safety validation rules for the SIRIUS LOCAL AI project.  
All tests are fully local and must be executed manually by the user.

The system interacts with Windows 11 APIs, filesystem operations, window management, and application control.  
All behavior must remain deterministic, safe, and reversible.

---

# 1. Testing Philosophy

- all tests must be reproducible  
- no automated tests that modify the system without confirmation  
- every test must validate safety, predictability, and reversibility  
- tests must not rely on network access  
- tests must not require external dependencies  
- plugin tests must follow Plugin System 2.0 rules  
- WIN‑CAP tests must validate permission boundaries  
- workflows must behave deterministically  
- **SECURITY FAMILY tests must validate identity, time‑limits, and schoolwork bypass logic**  

---

# 2. Test Categories

## A) Filesystem Tests (FS‑AGENT 2.0)
Validate:
- move, copy, delete  
- path validation  
- safety prompts  
- rollback behavior  
- protected directory blocking  

Checklist:
- invalid paths must be rejected  
- protected locations must be blocked  
- delete must require double confirmation  
- rollback must succeed on failure  
- no destructive action may run without explicit approval  

---

## B) Natural Language Router Tests (NL Router 2.0)
Validate:
- command recognition  
- parameter extraction  
- plugin NL command routing  
- ambiguity detection  
- confirmation prompts  

Checklist:
- unclear commands must trigger clarification  
- missing parameters must trigger questions  
- no command executes automatically  
- plugin commands must route correctly  
- invalid commands must be rejected  

---

## C) Workflow Engine Tests (Workflow Engine 2.0)
Validate:
- multi‑step sequences  
- state transitions  
- context memory behavior  
- plugin workflow execution  

Checklist:
- workflows must not skip steps  
- invalid transitions must be blocked  
- context must reset after completion  
- plugin workflows must follow deterministic rules  

---

## D) GUI Tests (GUI Layer 2.0)
Validate:
- confirmation dialogs  
- folder selection  
- safety warnings  
- plugin UI elements  
- correct routing of actions  

Checklist:
- UI must never auto‑confirm  
- UI must show correct target paths  
- UI must block unsafe operations  
- plugin buttons must execute correct actions  

---

## E) WIN‑CAP Tests (WIN‑CAP 2.0)
Validate:
- window snapping  
- app launching  
- audio device switching  
- system context detection  
- capability boundaries  

Checklist:
- actions must require confirmation  
- invalid operations must be rejected  
- system state must remain stable  
- no privileged action may bypass WIN‑CAP  
- capability wrappers must behave predictably  

---

## F) Plugin System Tests (Plugin System 2.0)
Validate:
- plugin loading  
- manifest parsing  
- NL command registration  
- workflow registration  
- AI loop rule execution  
- GUI element rendering  

Checklist:
- plugins must load without errors  
- invalid plugins must be rejected  
- plugin isolation must be preserved  
- no plugin may access restricted capabilities  
- plugin workflows must follow Workflow Engine 2.0 rules  

---

## G) AI Loop Tests (AI Loop 2.0)
Validate:
- interval execution  
- plugin heartbeat rules  
- deterministic scheduling  
- safe error handling  

Checklist:
- no blocking operations  
- no long‑running tasks  
- no infinite loops  
- plugin rules must not break runtime stability  

---

## H) SECURITY FAMILY Tests (v3.0.0)
Validate:
- identity classification (OWNER / FAMILY / STRANGER)  
- behavior‑based recognition  
- restricted mode for children  
- safe‑mode for unknown users  
- time‑limit enforcement  
- Schoolwork Priority Mode (schoolwork always allowed)  
- integration with NL Router, AITE, and WIN‑CAP  

Checklist:
- identity must be deterministic  
- time‑limits must trigger correctly  
- schoolwork must bypass restrictions instantly  
- stranger mode must block sensitive operations  
- no module may override SECURITY FAMILY decisions  

---

# 3. Test Execution Rules

- run tests in a clean environment  
- close unnecessary applications  
- avoid testing on system‑critical directories  
- verify each step manually  
- log results in plain text  
- repeat tests after major module changes  
- plugin tests must be isolated  
- SECURITY FAMILY tests must be performed with multiple user profiles  

---

# 4. Logging Format
[MODULE] action – status – notes

Examples:
[FS-AGENT] delete_file – blocked – protected directory
[WIN-CAP] snap_window – confirmed – window positioned left
[PLUGIN:notes] create_note – success – workflow completed
[SECURITY_FAMILY] time_limit_check – enforced – child profile exceeded limit
[SECURITY_FAMILY] schoolwork_detected – bypass – restrictions lifted 
---

# 5. Document Status

Current version: **2.0.0 (Stable)**  
This guide will expand as new modules and capabilities are introduced in v3.0.0 and v4.0.0.
