# 🏗 Architecture – SIRIUS LOCAL AI ALFA

SIRIUS LOCAL AI ALFA is a modular, local‑only AI runtime designed to safely interpret user commands and interact with the Windows 11 environment through isolated capability modules.

The architecture emphasizes **safety**, **predictability**, **modularity**, and **full local control**.

---

# ⚠️ ALPHA WARNING

SIRIUS LOCAL AI ALFA interacts with Windows 11 system APIs, including filesystem operations, window management, application control, and accessibility interfaces.  
The project is currently in **ALPHA**, and module behavior may change as the system evolves.

- Some operations may require elevated permissions (UAC).  
- Windows Defender or SmartScreen may classify the runtime as an “Unknown App”.  
- Antivirus tools may generate false positives during development.  
- Modules must run with the same privilege level as the applications they control.  
- All processing is fully local; no data leaves the user's PC.

**Users are encouraged to test features independently.**  
The author does not provide individual guidance for basic operations.

---

# 🧩 Architectural Principles

- strict modular separation  
- no hidden automation  
- no background tasks  
- no network communication  
- predictable, reversible actions  
- explicit user confirmations for all operations  
- capability‑based access to Windows functions  

---

# 🧱 Core Layers

## 1. Runtime Core
Central orchestrator responsible for:

- module initialization  
- lifecycle management  
- task scheduling  
- enforcing security boundaries  
- capability registration  

---

## 2. Command Interpreter (CME)
Natural‑language command processor.

Responsibilities:

- command classification  
- parameter extraction  
- routing to modules  
- generating confirmation prompts  
- validating intent  

---

## 3. Filesystem Agent (FS‑AGENT)
Safe, confirmation‑based filesystem operations.

Responsibilities:

- move, copy, delete  
- path validation  
- safety checks  
- user confirmation dialogs  

FS‑AGENT never performs an action without explicit approval.

---

## 4. Context Memory Engine (CME‑MEM)
Maintains short‑term workflow context.

Responsibilities:

- storing recent paths  
- tracking last actions  
- providing contextual suggestions  
- supporting multi‑step workflows  

---

## 5. Workflow Tracker
Controls multi‑step logic.

Responsibilities:

- workflow state machine  
- predicting next steps  
- validating transitions  
- ensuring predictable behavior  

---

## 6. UI Confirm Module
Interactive confirmation layer.

Responsibilities:

- folder selection  
- action confirmation  
- safety dialogs  
- automatic window opening  

---

## 7. Automatic Input Triage Engine (AITE)
Classifies incoming user inputs.

Recognized types:

- text  
- images/photos  
- installers/applications  

Responsibilities:

- type detection  
- routing  
- metadata generation  
- integration with FS‑AGENT and CME‑MEM  

---

## 8. Windows System Capabilities Layer (WIN‑CAP)
Abstracted access to Windows 11 system functions.

Submodules:

- `file_ops` — structured directories, project discovery  
- `app_ops` — launching, focusing, detecting running apps  
- `window_ops` — snapping, arranging, positioning windows  
- `audio_ops` — detecting and switching audio devices  

WIN‑CAP enables safe, high‑level system actions through controlled APIs.

---

# 🔌 Module Interconnections

- CME → FS‑AGENT  
- CME → UI Confirm  
- CME‑MEM → Workflow Tracker  
- AITE → FS‑AGENT  
- AITE → CME‑MEM  
- WIN‑CAP → CME  
- WIN‑CAP → Runtime Core  
- Runtime Core → all modules  

---

# 📌 Document Status
Current version: **ALPHA**
