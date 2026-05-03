# 🎨 STYLEGUIDE – SIRIUS LOCAL AI (v2.0.0)

This document defines the unified code style, naming conventions, module structure, and cleanliness rules for the SIRIUS LOCAL AI project.  
The goal is to maintain consistency, readability, and a professional standard across the entire Runtime 2.0 architecture.

All processing is fully local; no data leaves the user’s PC.

---

# 1. Core Principles

- code must be clean, readable, and modular  
- no monolithic functions or modules  
- no magic constants — everything must be named  
- no hidden side effects  
- every module must follow SRP (Single Responsibility Principle)  
- security always has priority over convenience  
- predictable, transparent behavior  
- consistent structure across all modules  
- minimal cognitive load for future maintainers  
- plugin code must follow Plugin API 2.0  
- **safety‑critical modules (SECURITY FAMILY) must follow strict isolation rules**  
- **no code may weaken time‑limits or Schoolwork Priority Mode**  

---

# 2. Naming Conventions

## Variables
- `lower_snake_case`
- short but descriptive
- no meaningless abbreviations

**Examples:**  
`target_path`, `pending_action`, `user_confirmation_required`

## Functions
- `lower_snake_case`
- name must express an action
- verbs first, nouns second

**Examples:**  
`resolve_target_folder()`, `validate_path()`, `generate_confirmation_dialog()`, `load_context_state()`

## Classes / Modules
- `PascalCase`
- name = responsibility of the module

**Examples:**  
`FilesystemAgent`, `NaturalLanguageRouter`, `ContextMemoryEngine`, `WorkflowEngine`,  
`SecurityFamily`, `TimeLimitsEngine`, `SchoolworkDetector`

## Constants
- `UPPER_SNAKE_CASE`
- must be descriptive

**Examples:**  
`MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT_MS`, `CHILD_TIME_LIMIT_MINUTES`

---

# 3. File & Folder Structure

Each module has its own folder:
/runtime  
/filesystem  
/commands  
/context  
/workflow  
/ui  
/email  
/ui_components  
/ui_components/animations  
/plugins  
/security_family   ← **NEW (v3.0.0)**

Each folder contains:

- `__init__.py`
- main module file
- helper utilities (if needed)

**Rules:**
- no cross‑module imports except through public interfaces  
- Runtime Core is the only module allowed to initialize others  
- no circular imports  
- no global mutable state  
- **SECURITY FAMILY must remain isolated from all other modules except Runtime Core**  

---

# 4. Function Length

- ideal length: **5–25 lines**  
- maximum: **50 lines**  
- if a function grows too large, split it  
- avoid deeply nested logic  
- prefer early returns over complex branching  

---

# 5. Comments

- comments only where necessary  
- comments explain **why**, not **what**  
- avoid redundant comments  
- document non‑obvious decisions  
- document all SECURITY FAMILY logic clearly  

---

# 6. Error Messages

- clear, concise, informative  
- never aggressive or vague  
- must include a reason + recommendation  
- avoid unnecessary technical jargon  

**Example:**  
`"Invalid path: target directory does not exist. Please choose a valid location."`

---

# 7. Security Rules in Code

- no operation may bypass user confirmation  
- all file operations must be validated  
- no direct deletion without double confirmation  
- no network operations in any module  
- no hidden background tasks  
- no automatic actions without explicit approval  
- no implicit state sharing  
- all privileged operations must go through WIN‑CAP 2.0  
- plugins must follow capability boundaries  
- **SECURITY FAMILY rules must never be bypassed**  
- **time‑limits must be enforced deterministically**  
- **Schoolwork Priority Mode must always override restrictions**  

---

# 8. Testing Requirements

Every module must include:

- basic tests  
- error‑state tests  
- security‑constraint tests  
- input‑validation tests  
- predictable behavior tests  
- no reliance on external network or cloud  
- **SECURITY FAMILY tests (identity, time‑limits, schoolwork detection)**  

---

# 9. Logging Rules

- concise and technical  
- no sensitive data  
- format: `[MODULE] action – status`

**Example:**  
`[FS-AGENT] move_file – confirmed`

**SECURITY FAMILY logging rules:**
- never log identity profiles  
- never log behavior patterns  
- never log child usage data  
- only log high‑level events (e.g., “family_mode_enabled”)  

---

# 10. Formatting Rules

- indentation: **4 spaces**  
- max line width: **100 characters**  
- blank line between logical blocks  
- no trailing spaces  
- consistent import ordering:

standard library  
import os
import json 
third‑party  
import win32api 
internal  
from filesystem.agent import FilesystemAgent
from security_family.time_limits import TimeLimitsEngine 
---

# 11. Module Boundaries

- modules may not access each other's internals  
- communication must go through public interfaces  
- Runtime Core is the only module allowed to orchestrate all others  
- no circular imports  
- no global mutable state  
- plugins must remain isolated and follow Plugin API 2.0  
- **SECURITY FAMILY may only communicate with Runtime Core, AITE, and WIN‑CAP**  
- **SchoolworkDetector may not access filesystem or OS directly**  

---

# Document Status

Current version: **2.0.0 (Stable)**  
This styleguide will evolve as new modules and capabilities are introduced.
