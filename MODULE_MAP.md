# Module Map – SIRIUS LOCAL AI (v2.0.0)

This document defines all modules of the project, their purpose, responsibilities, and interconnections.  
It serves as an architectural orientation map for the stable Runtime 2.0 architecture.

All processing is fully local; no data leaves the user's PC.

---

# 1. Runtime Core 2.0
**Purpose:** Central system layer.  
**Responsibilities:**
- module initialization  
- lifecycle management  
- plugin loading  
- task and workflow dispatch  
- enforcing security boundaries  
- capability registration  
- event routing  
- maintaining global system stability  

---

# 2. Filesystem Agent (FS‑AGENT 2.0)
**Purpose:** Safe file operations.  
**Responsibilities:**
- moving, copying, deleting  
- path validation  
- safety checks  
- action confirmations  
- conflict detection  
- rollback‑safe operations  

---

# 3. Natural Language Router (NL Router 2.0)
**Purpose:** Translation and routing of user commands.  
**Responsibilities:**
- recognizing command type  
- extracting parameters  
- routing to modules or plugins  
- detecting plugin NL commands  
- fallback interpretation  
- preventing ambiguous or unsafe actions  

---

# 4. Context Memory Engine (CME‑MEM 2.0)
**Purpose:** Maintaining context and recent actions.  
**Responsibilities:**
- tracking recent user actions  
- storing paths and states  
- providing contextual suggestions  
- supporting multi‑step workflows  
- metadata for plugins and workflows  

---

# 5. Workflow Engine 2.0
**Purpose:** Logic of step sequences and plugin workflows.  
**Responsibilities:**
- workflow state machine  
- executing plugin workflows  
- validating transitions  
- generating next‑step predictions  
- preventing invalid sequences  

---

# 6. GUI Layer 2.0
**Purpose:** Modular user interface.  
**Responsibilities:**
- rendering plugin buttons  
- executing GUI actions  
- integrating with Runtime Core  
- providing visual feedback  
- preparing for tray/voice integration  

---

# 7. Email Composer
**Purpose:** Generating email text (without sending).  
**Responsibilities:**
- email drafts  
- structured responses  
- professional text generation  

---

# 8. Automatic Input Triage Engine (AITE 2.0)
**Purpose:** Automatic detection and classification of input type.  
**Responsibilities:**
- detecting input type (text, image, application, document)  
- routing to the correct module  
- metadata generation  
- integration with FS‑AGENT and CME‑MEM  
- rejecting unsupported or unsafe inputs  

---

# 9. Windows System Capabilities Layer (WIN‑CAP 2.0)
**Purpose:** Provide safe, abstracted access to Windows 11 system functions.  
This module transforms SIRIUS into a true local OS‑level AI agent.

**Responsibilities:**
- exposing high‑level system capabilities  
- enforcing permissions and allowed scopes  
- providing safe wrappers around OS operations  
- enabling multi‑step system actions through AI reasoning  

**Submodules:**
- `file_ops`  
- `app_ops`  
- `window_ops`  
- `audio_ops`  
- `system_context`  

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

---

# 11. Workflow Module
**Purpose:** High‑level workflow logic.  
**Responsibilities:**
- orchestrating multi‑step operations  
- validating transitions  
- predictable behavior  
- integrating CME, FS‑AGENT, and GUI  

---

# 12. Plugin System 2.0
**Purpose:** Extensible plugin ecosystem.  
**Responsibilities:**
- loading plugin manifests  
- registering NL commands  
- registering AI tasks  
- registering workflows  
- registering AI loop rules  
- registering GUI elements  
- safe plugin isolation  

Official plugins include:
- automation  
- clipboard  
- example  
- file_manager  
- notes  
- system_tools  
- translator  

---

# 13. AI Loop 2.0
**Purpose:** Autonomous interval‑based logic.  
**Responsibilities:**
- executing plugin heartbeat rules  
- safe periodic tasks  
- deterministic scheduling  
- error protection  

---

# 14. Future Modules (Extensibility)

Possible future modules:
- UI Automation Layer  
- Voice Command Layer  
- System Monitoring Layer  
- Advanced Semantic Triage  

---

# 15. Self‑Repair & Health‑Check Layer (v4.0.0)
**Purpose:** Diagnostics and safe automatic recovery.  
**Responsibilities:**  
- checking integrity of core modules  
- detecting corrupted states, missing files, invalid configs  
- performing safe automatic repairs  
- generating patch suggestions (manual approval required)  
- preventing uncontrolled modifications of source code  
- reporting system health to Runtime Core  

**Submodules:**  
- `health_check_engine.py`  
- `self_repair_safe.py`  
- `repair_suggestions.py`  

---

# 16. SECURITY FAMILY (planned for v3.0.0)
**Purpose:** Behavior‑based identity and family safety layer.  
This module introduces **OWNER / FAMILY / STRANGER** identity levels.

**Responsibilities:**
- behavior‑based identity recognition  
- offline learning of owner and family profiles  
- safe‑mode for unknown users  
- restricted mode for children  
- protection of sensitive operations  
- integration with NL Router and WIN‑CAP  

**Submodules (already scaffolded):**
- `identity_engine.py`  
- `behavior_audit.py`  
- `access_control.py`  
- `family_mode.py`  
- `stranger_mode.py`  
- `profile_store.json`  

This becomes a **core security module** in version **3.0.0**.

---

# 17. Module Interconnections

- **NL Router → FS‑AGENT:** determines file operations  
- **NL Router → Plugins:** routes NL commands  
- **CME‑MEM → Workflow Engine:** provides context  
- **AITE → FS‑AGENT:** routes inputs based on type  
- **AITE → CME‑MEM:** stores metadata  
- **WIN‑CAP → Runtime Core:** privileged capability layer  
- **Runtime Core → all modules:** initialization and security  
- **Plugins → Runtime Core:** register capabilities  
- **SECURITY FAMILY → Runtime Core (v3.0.0):** identity‑based access control  

All communication is explicit and controlled.

---

# Document Status
Current version: **2.0.0 (Stable)**  
Module structure is fully defined and ready for future expansions in v3.0.0 and v4.0.0.
