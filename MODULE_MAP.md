# 🗺️ Module Map – SIRIUS LOCAL AI (v5.8 UNIFIED)

This document defines all modules of the project, their purpose, responsibilities, and interconnections.  
It serves as an architectural orientation map for the **Unified Orchestration, PanelAPI, TimeCore/Guard & Enhanced COLNIK‑AUTONOMY Architecture 5.8**.

Version **5.8 UNIFIED** expands and stabilizes the module map with:

- **Unified Orchestrator (`sirius_orchestrator.py`)**  
- **PanelAPI & Interactive [ÁNO/NIE] Confirmation Loops**  
- **TimeCore Temporal Tracking & Guard Security Supervision**  
- **AITE 5.8 (Semantic + Deep Explainability Multimodal Triage)**  
- **Workflow Engine 5.8 (Deep Explainability + COLNIK‑validated + AUTONOMY‑aware Routing)**  
- **Reasoning Engine 5.8 (multi‑hop, inheritance, transitivity, rule chaining)**  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP (Explainability Engines)**  
- **Unified Knowledge Graph 5.8 + KG‑LIGHT (stabilized autosave `autosave_kg.json`)**  
- **Expanded KG Comfort Commands**  
- **ENVOY Execution + Permission Layers 5 (Deep Explainability Traces)**  
- **System Agent 5**  
- **Security Family 5.x (Identity Engine 3.1)**  
- **Self‑Repair Layer 5.8**  
- **Unified PC/Mobile deterministic routing**  
- **Deterministic UI Automation Engine 5.1**  
- **COLNIK‑6.x Enterprise Validation Layer (Standard & IPC Mode)**  
- **AUTONOMY 6.x Autonomous Proposal/Confirmation & Triage Mode**  

All processing is fully local; no data leaves the user's device.

---

# 1. Runtime Core & Orchestrator 5.8 (Unified)
**Purpose:** Central execution orchestrator driven by `sirius_orchestrator.py`.  
**Responsibilities:**
- module initialization and lifecycle management via `sirius_orchestrator.py`  
- interactive `PanelAPI` confirmation loops (`[ÁNO/NIE]`)  
- temporal tracking (`TimeCore`) and security/anomaly monitoring (`Guard`)  
- plugin loading  
- workflow + deep explainability dispatch  
- enforcing capability boundaries  
- event routing  
- global system stability  
- integration with Security Family 5.x and Self‑Repair Layer 5.8  
- deterministic execution and System Agent 5 routing  
- KG_EXPLAIN & KG_EXPLAIN_DEEP routing  
- UI Automation Engine 5.1 integration  
- unified PC/Mobile behavior  
- ENVOY permission enforcement  
- **COLNIK‑6.x validation of workflow + KG operations (Standard & IPC Mode)**  
- **AUTONOMY 6.x proposal/confirmation & Triage Mode routing**

---

# 2. Filesystem Agent (FS‑AGENT 5.8)
**Purpose:** Safe, deterministic file operations.  
**Responsibilities:**
- moving, copying, deleting  
- path validation  
- rollback‑safe operations  
- semantic routing (documents, code, schoolwork)  
- integration with Schoolwork Engine 5.8  
- integration with UI Automation Engine 5.1  
- unified PC/Mobile filesystem logic  
- COLNIK‑validated file operations  

---

# 3. Natural Language Router (NL Router 5.8)
**Purpose:** Semantic interpretation and routing of user commands.  
**Responsibilities:**
- command classification  
- semantic extraction  
- explain intent detection (“why … ?”)  
- routing to modules or plugins  
- plugin NL command detection  
- fallback interpretation  
- preventing ambiguous or unsafe actions  
- identity‑aware filtering (OWNER / FAMILY / STRANGER)  
- UI automation command routing  
- System Agent 5 validation for system‑level intents  
- COLNIK‑validated NL routing  
- AUTONOMY‑aware intent detection  

---

# 4. Context Memory Engine (CME‑MEM 5.8)
**Purpose:** Semantic workflow context.  
**Responsibilities:**
- tracking recent actions  
- storing semantic tags  
- supporting multi‑step workflows  
- providing contextual hints  
- subject/difficulty metadata  
- explainability traces  
- integration with Schoolwork Engine 5.8  
- integration with UI Automation Engine 5.1  
- unified PC/Mobile context memory  
- COLNIK‑validated context transitions  

---

# 5. Workflow Engine 5.8
**Purpose:** Deterministic multi‑step logic with deep explainability.  
**Responsibilities:**
- workflow state machine managed by `sirius_orchestrator.py`  
- plugin workflow execution  
- semantic transitions  
- preventing invalid sequences  
- SCHOOLWORK workflow prioritization  
- integration with Reasoning Engine 5.8  
- integration with KG_EXPLAIN & KG_EXPLAIN_DEEP  
- integration with UIWorkflow 5.1  
- deterministic fallback behavior  
- unified PC/Mobile workflows  
- ENVOY workflow integration  
- **COLNIK‑validated workflow steps (Standard & IPC Mode)**  
- **AUTONOMY‑aware transitions (Control & Triage Mode)**

---

# 6. GUI Layer 5.8
**Purpose:** Modular user interface.  
**Responsibilities:**
- rendering plugin UI  
- executing GUI actions  
- identity indicators  
- SCHOOLWORK indicators  
- tray/voice integration  
- UI automation visual feedback  
- explainability visualizer  
- unified PC/Mobile UI  

---

# 7. Email Composer
**Purpose:** Generating email text (without sending).  
**Responsibilities:**
- email drafts  
- structured responses  
- professional text generation  

---

# 8. Automatic Input Triage Engine (AITE 5.8)
**Purpose:** Multimodal semantic + deep explainability detection and classification.  
**Responsibilities:**
- detecting input type (text, image, code, document, installer)  
- OCR extraction  
- semantic analysis  
- subject detection  
- difficulty scoring  
- explain intent detection  
- routing to correct modules  
- metadata generation  
- integration with FS‑AGENT, CME‑MEM  
- integration with Schoolwork Engine 5.8  
- integration with Reasoning Engine 5.8  
- ENVOY 5 support  
- UI automation intent detection  
- identity‑aware triage  
- unified PC/Mobile triage  
- **COLNIK‑validated triage decisions**  
- **AUTONOMY proposal/confirmation triggers**

---

# 9. Windows System Capabilities Layer (WIN‑CAP 5.x)
**Purpose:** Safe, abstracted access to Windows system functions.  
**Responsibilities:**
- exposing high‑level system capabilities  
- enforcing permissions and allowed scopes  
- safe wrappers around OS operations  
- multi‑step system actions  
- identity‑aware restrictions  
- UI automation OS‑level routing  
- System Agent 5 enforcement  
- COLNIK‑validated capability routing  
- AUTONOMY‑aware capability validation  

**Submodules:**
- `file_ops`  
- `app_ops`  
- `window_ops`  
- `audio_ops`  
- `system_context`  
- `automation_ops`  
- `ui_capabilities_5_x`  

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
- orchestrating multi‑step operations via `sirius_orchestrator.py`  
- validating transitions  
- predictable behavior  
- integrating CME, FS‑AGENT, GUI  
- SCHOOLWORK workflow routing  
- UI automation workflow integration  
- unified PC/Mobile workflow logic  
- COLNIK‑validated workflow transitions  
- AUTONOMY‑aware workflow logic  

---

# 12. Plugin System 5.x
**Purpose:** Extensible plugin ecosystem.  
**Responsibilities:**
- loading plugin manifests  
- registering NL commands  
- registering AI tasks  
- registering workflows  
- registering reasoning hooks  
- registering GUI elements  
- safe plugin isolation  
- SCHOOLWORK‑aware plugin behavior  
- UI automation plugin hooks  
- unified PC/Mobile plugin behavior  
- COLNIK‑validated plugin actions  
- AUTONOMY‑aware plugin routing  

Official plugins include:
- automation  
- clipboard  
- file_manager  
- notes  
- system_tools  
- translator  
- developer_tools  

---

# 13. AI Loop 5.x
**Purpose:** Autonomous interval‑based logic.  
**Responsibilities:**
- executing plugin heartbeat rules  
- safe periodic tasks  
- deterministic scheduling  
- error protection  
- SCHOOLWORK‑aware timing  
- unified PC/Mobile loop behavior  
- AUTONOMY‑aware autonomous continuation  

---

# 14. Self‑Repair & Health‑Check Layer (5.8)
**Purpose:** Diagnostics and safe automatic recovery.  
**Responsibilities:**  
- checking integrity of core modules  
- detecting corrupted states, missing files, invalid configs  
- performing safe automatic repairs  
- generating patch suggestions  
- preventing uncontrolled modifications  
- reporting system health to Runtime Core  
- validating UI automation modules  
- integration with System Agent 5  
- unified PC/Mobile diagnostics  

**Submodules:**  
- `health_check_engine.py`  
- `self_repair_safe.py`  
- `repair_suggestions.py`  

---

# 15. Security Family 5.x (Identity Engine 3.1)
**Purpose:** Behavior‑based identity and family safety layer.  
**Responsibilities:**
- OWNER / FAMILY / STRANGER identity  
- behavior‑based recognition  
- safe‑mode for unknown users  
- restricted mode for children  
- time‑limits v3  
- Schoolwork Engine integration  
- identity‑aware routing  
- STRANGER‑mode restrictions  
- UI automation identity gating  
- System Agent 5 enforcement  
- AUTONOMY‑aware identity validation  

**Submodules:**
- `identity_engine_3_1.py`  
- `behavior_audit_3_1.py`  
- `access_control_3_1.py`  
- `family_mode_v3.py`  
- `stranger_mode_v3.py`  
- `time_limits_v3.py`  
- `schoolwork_engine_5_x.py`  
- `profile_store_v3.json`  

---

# 16. Intelligent Runtime Modules (v5.8)

## 16.1 HOME_ASSISTANT 5.8  
## 16.2 COOKING_ADVISOR 5.8  
## 16.3 DEVICE_DIAGNOSTICS 5.8  
## 16.4 SCHOOL_HELPER 5.8  
## 16.5 IMAGE_ANALYZER 5.8  
## 16.6 CONTEXT_ROUTER 5.8  
## 16.7 KNOWLEDGE_PACKS 5.x  

---

# 17. PASSWORD_VAULT 5.0
**Purpose:** Secure offline credential storage.  
**Responsibilities:**
- AES‑256‑GCM encrypted vault  
- PBKDF2‑HMAC‑SHA256 master key derivation  
- OWNER‑only write access  
- FAMILY read‑only access  
- STRANGER blocked  
- deterministic API for workflows  
- NL Router integration  
- Runtime Core integration  

---

# 18. UI Automation Engine 5.1
**Purpose:** Semantic, deterministic UI automation.  
**Responsibilities:**
- improved fuzzy UI parsing  
- semantic alias mapping  
- multi‑stage resolution pipeline  
- deterministic fallback logic  
- OS‑level routing  
- safe sandboxed execution  
- WIN‑CAP 5.x integration  
- System Agent 5 validation  
- unified PC/Mobile automation  

**Submodules:**
- `ui_parser_5_1.py`  
- `ui_workflow_5_1.py`  
- `ui_actions_5_1.py`  
- `win_capabilities_5_x.py`  

---

# 19. System Agent 5
**Purpose:** Final gatekeeper for all system‑level actions.  
**Responsibilities:**
- validating every system action  
- enforcing identity rules  
- blocking unsafe operations  
- deterministic safety enforcement  
- logging system actions  
- protecting OS‑level automation  
- unified PC/Mobile execution  
- AUTONOMY‑aware system validation  

**Submodules:**
- `agent_core_5.py`  
- `agent_rules_5.py`  
- `agent_validation_5.py`  

---

# 20. SIRIUS ENVOY 5 (Execution + Permission Layers)
**Purpose:** Safe, outbound‑only external retrieval.  
**Responsibilities:**  
- permission layer (identity‑aware)  
- scraper layer  
- quarantine sandbox  
- validator & policy filter  
- deep explainability traces  
- safe payload delivery  
- Knowledge Pack updates  
- unified PC/Mobile behavior  
- COLNIK‑validated payload delivery (Standard & IPC Mode)  
- AUTONOMY‑aware validation traces  

---

# 21. System Intelligence Layer 5.8
**Purpose:** Cross‑platform diagnostics and safe optimization.  
**Responsibilities:**
- hardware analysis  
- driver checks  
- service health  
- process analysis  
- optimization suggestions  
- deterministic system workflows  
- System Agent 5 enforcement  
- unified PC/Mobile diagnostics  
- explainability‑aware diagnostics  
- COLNIK‑validated system actions  
- AUTONOMY‑aware system intelligence  

---

# 22. Mobile Runtime 5.8
**Purpose:** Unified mobile execution layer.  
**Responsibilities:**
- mobile‑optimized workflows  
- mobile filesystem logic  
- mobile UI automation  
- mobile AITE integration  
- mobile reasoning integration  
- mobile KG_EXPLAIN & KG_EXPLAIN_DEEP integration  
- COLNIK‑validated mobile workflows  
- AUTONOMY‑aware mobile routing  

---

# 23. Module Interconnections
All modules communicate through:

- Unified Orchestrator (`sirius_orchestrator.py`)  
- PanelAPI interactive loops (`[ÁNO/NIE]`)  
- TimeCore & Guard supervision  
- Runtime Core 5.8  
- NL Router 5.8  
- Workflow Engine 5.8  
- CME‑MEM 5.8  
- Security Family 5.x  
- WIN‑CAP 5.x  
- UI Automation Engine 5.1  
- System Agent 5  
- ENVOY 5  
- KG_EXPLAIN & KG_EXPLAIN_DEEP  
- Self‑Repair Layer 5.8  
- Mobile Runtime 5.8  
- **COLNIK‑6.x Validation Layer (Standard & IPC Mode)**  
- **AUTONOMY 6.x Control & Triage Mode**

---

# Document Status
**Version:** 5.8 UNIFIED  
Updated to reflect the **5.7.0 → 5.8 transition**, orchestrator routing via `sirius_orchestrator.py`, interactive `PanelAPI` confirmation loops, `TimeCore`/`Guard` supervision, expanded **COLNIK‑6.x (Standard & IPC Mode)**, and **AUTONOMY 6.x (Control & Triage Mode)**.
