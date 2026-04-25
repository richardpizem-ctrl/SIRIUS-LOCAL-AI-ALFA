# 🏗 Architecture – SIRIUS LOCAL AI ALFA

<p align="center">
  <img src="https://img.shields.io/badge/version-ALPHA-orange">
  <img src="https://img.shields.io/badge/license-MIT-green">
  <img src="https://img.shields.io/badge/platform-Windows%2011-blue">
  <img src="https://img.shields.io/badge/architecture-modular-lightgrey">
  <img src="https://img.shields.io/badge/local%20AI-100%25-blueviolet">
</p>

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
- deterministic behavior across all modules  
- no implicit state sharing  

---

# 🖼 Architecture Diagram (Placeholder)

> A high‑level architecture diagram will be added here in the next update.

<p align="center">
  <img src="docs/architecture_diagram_placeholder.png" width="600">
</p>

---

# 🧱 Core Layers

## 1. Runtime Core
Central orchestrator responsible for:

- module initialization  
- lifecycle management  
- task scheduling  
- enforcing security boundaries  
- capability registration  
- dispatching events to modules  
- maintaining global system stability  

The Runtime Core is the **heart of the system** and ensures that all modules operate within safe, isolated boundaries.

---

## 2. Command Interpreter (CME)
Natural‑language command processor.

Responsibilities:

- command classification  
- parameter extraction  
- routing to modules  
- generating confirmation prompts  
- validating intent  
- preventing ambiguous or unsafe actions  

CME ensures that **no command is executed without clear user intent**.

---

## 3. Filesystem Agent (FS‑AGENT)
Safe, confirmation‑based filesystem operations.

Responsibilities:

- move, copy, delete  
- path validation  
- safety checks  
- user confirmation dialogs  
- conflict detection  
- rollback‑safe operations  

FS‑AGENT never performs an action without explicit approval.

---

## 4. Context Memory Engine (CME‑MEM)
Maintains short‑term workflow context.

Responsibilities:

- storing recent paths  
- tracking last actions  
- providing contextual suggestions  
- supporting multi‑step workflows  
- enabling reversible logic  

CME‑MEM **never stores long‑term personal data** — only workflow‑related context.

---

## 5. Workflow Tracker
Controls multi‑step logic.

Responsibilities:

- workflow state machine  
- predicting next steps  
- validating transitions  
- ensuring predictable behavior  
- preventing invalid or unsafe sequences  

The Workflow Tracker ensures that multi‑step operations behave consistently and transparently.

---

## 6. UI Confirm Module
Interactive confirmation layer.

Responsibilities:

- folder selection  
- action confirmation  
- safety dialogs  
- automatic window opening  
- presenting workflow steps  
- preventing accidental actions  

UI Confirm is the **user‑facing safety barrier**.

---

## 7. Automatic Input Triage Engine (AITE)
Classifies incoming user inputs.

Recognized types:

- text  
- images/photos  
- installers/applications  
- unknown/ambiguous inputs  

Responsibilities:

- type detection  
- routing  
- metadata generation  
- integration with FS‑AGENT and CME‑MEM  
- rejecting unsupported or unsafe inputs  

AITE ensures that the system always knows **what kind of input it is dealing with**.

---

## 8. Windows System Capabilities Layer (WIN‑CAP)
Abstracted access to Windows 11 system functions.

Submodules:

- `file_ops` — structured directories, project discovery  
- `app_ops` — launching, focusing, detecting running apps  
- `window_ops` — snapping, arranging, positioning windows  
- `audio_ops` — detecting and switching audio devices  
- `system_context` — active window, mounted drives, available devices  

WIN‑CAP enables safe, high‑level system actions through controlled APIs.

---

# 🔌 Module Interconnections

```
User Input
   ↓
AITE → CME → UI Confirm → FS‑AGENT
   ↓        ↓
CME‑MEM → Workflow Tracker
   ↓
Runtime Core → WIN‑CAP → Windows 11 APIs
```

### Key relationships:

- CME → FS‑AGENT  
- CME → UI Confirm  
- CME‑MEM → Workflow Tracker  
- AITE → FS‑AGENT  
- AITE → CME‑MEM  
- WIN‑CAP → CME  
- WIN‑CAP → Runtime Core  
- Runtime Core → all modules  

All communication is **explicit**, never implicit.

---

# 🧱 Module Isolation Model

Each module:

- runs independently  
- exposes only documented interfaces  
- cannot access other modules’ internals  
- communicates through the Runtime Core  
- cannot perform actions without confirmation  
- cannot bypass safety layers  

This ensures **predictable, auditable behavior**.

---

# 🧪 Deterministic Execution Model

SIRIUS LOCAL AI ALFA guarantees:

- no race conditions  
- no background threads modifying state  
- no hidden automation  
- no unpredictable behavior  

Every action is:

1. Interpreted  
2. Confirmed  
3. Executed  
4. Logged  
5. Reversible (when possible)  

---

# 📌 Document Status

Current version: **ALPHA**  
Architecture is subject to refinement as modules reach Phase 4 stability.
