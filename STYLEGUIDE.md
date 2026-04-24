# 🎨 STYLEGUIDE – SIRIUS LOCAL AI ALFA

This document defines the unified code style, naming conventions, module structure, and cleanliness rules for the project.  
The goal is to maintain consistency, readability, and a professional standard across the entire system.

---

## ⚠️ ALPHA WARNING

SIRIUS LOCAL AI ALFA interacts with Windows 11 system APIs, filesystem operations, window management, and application control.  
The project is currently in **ALPHA**, and module behavior may evolve as development continues.

- Some operations may require elevated permissions (UAC).  
- Windows Defender or SmartScreen may classify the runtime as an “Unknown App”.  
- Antivirus tools may generate false positives during development.  
- Modules must run with the same privilege level as the applications they control.  
- All processing is fully local; no data leaves the user's PC.

**Users are encouraged to test features independently.**  
This is an ALPHA‑stage developer tool — the author does not provide individual guidance for basic operations.

---

# 1. Core Principles

- code must be clean, readable, and modular  
- no monolithic functions or modules  
- no magic constants — everything must be named  
- no hidden side effects  
- every module must follow SRP (Single Responsibility Principle)  
- security always has priority over convenience  
- predictable, transparent behavior  

---

# 2. Naming Conventions

## Variables
- lower_snake_case  
- short but descriptive  
- no meaningless abbreviations  

Examples:  
target_path  
pending_action  
user_confirmation_required  

## Functions
- lower_snake_case  
- name must express an action  

Examples:  
resolve_target_folder()  
validate_path()  
generate_confirmation_dialog()  

## Classes / Modules
- PascalCase  
- name = responsibility of the module  

Examples:  
FilesystemAgent  
CommandInterpreter  
ContextMemoryEngine  

---

# 3. File Structure

Each module has its own folder:

/runtime  
/filesystem  
/commands  
/context  
/workflow  
/ui  
/email  

Each folder contains:

- __init__.py  
- main module  
- helper utilities (if needed)

---

# 4. Function Length

- ideal length: 5–25 lines  
- maximum: 50 lines  
- if a function grows too large, split it  

---

# 5. Comments

- comments only where necessary  
- comments explain **why**, not **what**  

Bad:  
i = 0  # set i to zero  

Good:  
# reset index for a new workflow step  
i = 0  

---

# 6. Error Messages

- clear, concise, informative  
- never aggressive or vague  
- must include a reason + recommendation  

Example:  
Invalid path: C:/root  
This operation is blocked for safety reasons.

---

# 7. Security Rules in Code

- no operation may bypass user confirmation  
- all file operations must be validated  
- no direct deletion without double confirmation  
- no network operations in any module  
- no hidden background tasks  
- no automatic actions without explicit approval  

---

# 8. Testing

Every module must include:

- basic tests  
- error‑state tests  
- security‑constraint tests  
- input‑validation tests  

---

# 9. Logging

- concise and technical  
- no sensitive data  
- format: [MODULE] action – status  

Example:  
[FS-AGENT] move_file – confirmed  

---

# 10. Formatting

- indentation: 4 spaces  
- max line width: 100 characters  
- blank line between logical blocks  
- no trailing spaces  
- consistent structure across all modules  

---

# 11. Document Status

Current version: ALPHA
