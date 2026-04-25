# Module Map – SIRIUS LOCAL AI ALFA

This document defines all modules of the project, their purpose, responsibilities, and interconnections.  
It serves as an architectural orientation map.

---

## ⚠️ ALPHA WARNING

SIRIUS LOCAL AI ALFA interacts with Windows 11 system APIs, filesystem operations, window management, and application control.  
The project is currently in **ALPHA**, and module behavior may change as development progresses.

- Some operations may require elevated permissions (UAC).  
- Windows Defender or SmartScreen may classify the runtime as an “Unknown App”.  
- Antivirus tools may generate false positives during development.  
- Modules must run with the same privilege level as the applications they control.  
- All processing is fully local; no data leaves the user's PC.

**Users are encouraged to test features independently.**  
This is an ALPHA‑stage developer tool — the author does not provide individual guidance for basic operations.

---

# 1. Runtime Core
**Purpose:** Central system layer.  
**Responsibilities:**
- module initialization  
- lifecycle management  
- task scheduling  
- enforcing security boundaries  
- capability registration  
- dispatching events to modules  

---

# 2. Filesystem Agent (FS‑AGENT)
**Purpose:** Safe file operations.  
**Responsibilities:**
- moving, copying, deleting  
- path validation  
- safety checks  
- action confirmations  
- user feedback  
- rollback‑safe operations  

---

# 3. Command Interpreter (CME)
**Purpose:** Translation of user commands.  
**Responsibilities:**
- recognizing command type  
- extracting parameters  
- routing to modules  
- generating “Where to?” and “Confirm?” questions  
- validating intent  
- preventing ambiguous or unsafe actions  

---

# 4. Context Memory Engine (CME‑MEM)
**Purpose:** Maintaining context and recent actions.  
**Responsibilities:**
- tracking recent user actions  
- storing paths and states  
- providing contextual suggestions  
- supporting multi‑step workflows  

---

# 5. Workflow Tracker
**Purpose:** Logic of step sequences.  
**Responsibilities:**
- workflow state machine  
- predicting the next step  
- validating transitions  
- generating automatic action suggestions  
- preventing invalid sequences  

---

# 6. UI Confirm Module
**Purpose:** Interactive confirmation tables.  
**Responsibilities:**
- selecting the target folder  
- confirming actions  
- safety dialogs  
- automatic window opening  
- presenting workflow steps  

---

# 7. Email Composer
**Purpose:** Generating email text (without sending).  
**Responsibilities:**
- email drafts  
- professional responses  
- structured text generation  

---

# 8. Automatic Input Triage Engine (AITE)
**Purpose:** Automatic detection and classification of input type.  
**Responsibilities:**
- detecting input type (text, image, application)  
- routing to the correct module  
- metadata generation  
- integration with FS‑AGENT and CME‑MEM  
- rejecting unsupported or unsafe inputs  

AITE ensures that SIRIUS immediately understands what the user inserted or downloaded and classifies it correctly without asking questions.

---

# 9. Windows System Capabilities Layer (WIN‑CAP)
**Purpose:** Provide safe, abstracted access to Windows 11 system functions.  
This module transforms SIRIUS into a true local OS‑level AI agent.

**Responsibilities:**
- exposing high‑level system capabilities  
- enforcing permissions and allowed scopes  
- providing safe wrappers around OS operations  
- enabling multi‑step system actions through AI reasoning  

**Submodules:**
- `file_ops` — project discovery, structured directories  
- `app_ops` — launching, focusing, detecting running apps  
- `window_ops` — snapping, arranging, positioning windows  
- `audio_ops` — detecting and switching audio devices  
- `system_context` — active window, drives, devices  

**Examples of enabled commands:**
- “Find all SIRIUS projects on disk and open the latest.”  
- “Launch Real-Time MIDI Notation and place its window next to VS Code.”  
- “Check if audio is going to the correct device and switch if not.”  
- “Create a new folder for v1.3.0 and prepare the structure.”  

---

# 10. UI Components
**Purpose:** Modular UI building blocks.  
**Responsibilities:**
- reusable UI elements  
- layout components  
- visual helpers  
- animation hooks  

**Subfolder: `animations/`**
- `animation_engine.py`  
- `animation_objects.py`  
- `animation_scenes.py`  
- `animation_manager.py`  

These files prepare the animation system for future versions (v2.0.0 and v3.0.0).

---

# 11. Workflow Module
**Purpose:** High‑level workflow logic.  
**Responsibilities:**
- orchestrating multi‑step operations  
- validating transitions  
- providing predictable behavior  
- integrating CME, FS‑AGENT, and UI Confirm  

---

# 12. Future Modules (Extensibility)

**Possible future modules:**
- UI Automation Layer  
- Voice Command Layer  
- System Monitoring Layer  
- Plugin API  

---

## **Self‑Repair & Health‑Check Layer (v4.0.0)**  
**Purpose:** Diagnostics and safe automatic recovery.  
**Responsibilities:**  
- checking integrity of core modules (runtime, context, commands, filesystem)  
- detecting corrupted states, missing files, invalid configs  
- performing safe automatic repairs (cache reset, index rebuild, default config restore)  
- generating patch suggestions for code-level fixes (manual approval required)  
- preventing uncontrolled modifications of source code  
- reporting system health to Runtime Core  

**Submodules:**  
- `health_check_engine.py` — diagnostics  
- `self_repair_safe.py` — safe automatic repairs  
- `repair_suggestions.py` — patch proposals (non‑executing)  

**Notes:**  
This module is planned for **version 4.0.0**, after the system reaches full stability.

---

# 13. Module Interconnections

- **CME → FS‑AGENT:** decides what action should be executed  
- **CME → UI Confirm:** generates questions  
- **CME‑MEM → Workflow Tracker:** provides context  
- **AITE → FS‑AGENT:** routes inputs based on type  
- **AITE → CME‑MEM:** stores metadata about the input  
- **WIN‑CAP → CME:** exposes system capabilities  
- **WIN‑CAP → Runtime Core:** privileged capability layer  
- **Runtime Core → all modules:** initialization and security  

---

# Document Status
Current version: **ALPHA**  
Module structure may evolve as the system approaches Phase 4 stability.
