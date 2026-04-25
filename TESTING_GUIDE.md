# 🧪 TESTING GUIDE – SIRIUS LOCAL AI ALFA

This document defines the testing strategy, procedures, and safety validation rules for the SIRIUS LOCAL AI ALFA project.  
All tests are fully local and must be executed manually by the user.

---

## ⚠️ ALPHA WARNING

The system interacts with Windows 11 APIs, filesystem operations, and application control.  
Unexpected behavior may occur during ALPHA development.

Users must test features independently.  
The author does not provide individual troubleshooting for basic operations.

---

# 1. Testing Philosophy

- all tests must be reproducible  
- no automated tests that modify the system without confirmation  
- every test must validate safety, predictability, and reversibility  
- tests must not rely on network access  
- tests must not require external dependencies  

---

# 2. Test Categories

## A) Filesystem Tests
Validate:
- move, copy, delete  
- path validation  
- safety prompts  
- rollback behavior  

Checklist:
- invalid paths must be rejected  
- protected locations must be blocked  
- delete must require double confirmation  

---

## B) Command Interpreter Tests
Validate:
- command recognition  
- parameter extraction  
- ambiguity detection  
- confirmation prompts  

Checklist:
- unclear commands must trigger clarification  
- missing parameters must trigger questions  
- no command executes automatically  

---

## C) Workflow Tests
Validate:
- multi‑step sequences  
- state transitions  
- context memory behavior  

Checklist:
- workflows must not skip steps  
- invalid transitions must be blocked  
- context must reset after completion  

---

## D) UI Tests
Validate:
- confirmation dialogs  
- folder selection  
- safety warnings  
- correct routing of actions  

Checklist:
- UI must never auto‑confirm  
- UI must show correct target paths  
- UI must block unsafe operations  

---

## E) WIN‑CAP Tests
Validate:
- window snapping  
- app launching  
- audio device switching  
- system context detection  

Checklist:
- actions must require confirmation  
- invalid operations must be rejected  
- system state must remain stable  

---

# 3. Test Execution Rules

- run tests in a clean environment  
- close unnecessary applications  
- avoid testing on system‑critical directories  
- verify each step manually  
- log results in plain text  

---

# 4. Logging Format

```
[MODULE] action – status – notes
```

Example:
```
[FS-AGENT] delete_file – blocked – protected directory
```

---

# 5. Document Status

Current version: **ALPHA**
