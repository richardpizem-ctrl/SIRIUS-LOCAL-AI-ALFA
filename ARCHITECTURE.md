# 🏗 Architecture – SIRIUS LOCAL AI (v2.0.0)

<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-blue">
  <img src="https://img.shields.io/badge/license-MIT-green">
  <img src="https://img.shields.io/badge/platform-Windows%2011-blue">
  <img src="https://img.shields.io/badge/architecture-modular-lightgrey">
  <img src="https://img.shields.io/badge/local%20AI-100%25-blueviolet">
</p>

SIRIUS LOCAL AI is a fully modular, local‑only AI runtime designed to safely interpret user commands and interact with the Windows 11 environment through isolated capability modules.

Version **2.0.0** introduces a complete architectural stabilization, a new plugin ecosystem, and a unified Runtime 2.0 core.

The architecture emphasizes **safety**, **predictability**, **modularity**, and **full local control**.

---

# 🛡 Stability Notice (v2.0.0)

SIRIUS LOCAL AI now operates on the **stable Runtime 2.0 architecture**.

- All modules are isolated and deterministic  
- No background automation without explicit rules  
- No network communication  
- All processing is fully local  
- All plugin interfaces are stable  
- All core modules (runtime, context, filesystem, commands) are validated for v2.0.0  

This version is stable and production‑ready, with future expansions planned for v3.0.0 and v4.0.0.

---

# 🧩 Architectural Principles

- strict modular separation  
- deterministic behavior  
- no hidden automation  
- no background tasks unless defined by AI Loop rules  
- no network communication  
- predictable, reversible actions  
- capability‑based access to Windows functions  
- explicit user intent for all operations  
- no implicit state sharing  
- plugin‑driven extensibility  

---

# 🖼 Architecture Diagram (Placeholder)

> A high‑level architecture diagram will be added in a future update.

<p align="center">
  <img src="docs/architecture_diagram_placeholder.png" width="600">
</p>

---

# 🧱 Core Layers (v2.0.0)

## 1. Runtime Core 2.0
Central orchestrator responsible for:

- module initialization  
- lifecycle management  
- plugin loading  
- task and workflow dispatch  
- enforcing security boundaries  
- capability registration  
- event routing  
- maintaining global system stability  

Runtime Core 2.0 is the **heart of the system**.

---

## 2. Natural Language Router (NL Router 2.0)
Processes natural‑language commands.

Responsibilities:

- command classification  
- plugin NL command detection  
- routing to modules  
- fallback interpretation  
- preventing ambiguous or unsafe actions  

NL Router 2.0 ensures **clear intent and safe execution**.

---

## 3. Filesystem Agent (FS‑AGENT 2.0)
Safe filesystem operations.

Responsibilities:

- move, copy, delete  
- path validation  
- safety checks  
- conflict detection  
- rollback‑safe operations  

FS‑AGENT 2.0 performs only **safe, validated actions**.

---

## 4. Context Memory Engine (CME‑MEM 2.0)
Maintains short‑term workflow context.

Responsibilities:

- storing recent paths  
- tracking last actions  
- providing contextual hints  
- supporting multi‑step workflows  

CME‑MEM stores **only workflow‑related context**, never personal data.

---

## 5. Workflow Engine 2.0
Controls multi‑step logic.

Responsibilities:

- workflow state machine  
- executing plugin workflows  
- validating transitions  
- predictable behavior  
- preventing invalid sequences  

Workflow Engine 2.0 ensures **transparent, deterministic workflows**.

---

## 6. GUI Layer 2.0
Plugin‑driven user interface.

Responsibilities:

- rendering plugin buttons  
- executing GUI actions  
- integrating with RuntimeManager  
- future expansion to tray/voice layers  

GUI 2.0 is fully modular and extensible.

---

## 7. Automatic Input Triage Engine (AITE 2.0)
Classifies incoming user inputs.

Recognized types:

- text  
- images/photos  
- installers/applications  
- documents  
- **(v3.0.0) schoolwork** — academic content with priority bypass

Responsibilities:

- type detection  
- routing  
- metadata generation  
- integration with FS‑AGENT and CME‑MEM  
- **bypassing FAMILY time limits for schoolwork (NEW)**  

AITE ensures the system always knows **what kind of input it is handling** and gives **schoolwork absolute priority**.

---

## 8. Windows System Capabilities Layer (WIN‑CAP 2.0)
Abstracted access to Windows 11 system functions.

Submodules:

- `file_ops`  
- `app_ops`  
- `window_ops`  
- `audio_ops`  
- `system_context`  

WIN‑CAP provides **safe, high‑level system actions**.

---

## 9. Plugin System 2.0
A fully modular plugin ecosystem.

Features:

- manifest‑based plugin definitions  
- NL commands  
- AI tasks  
- workflows  
- AI loop rules  
- GUI elements  

All official plugins are **v2‑ready**.

---

# 🔐 Future Core Module – SECURITY FAMILY (planned for v3.0.0)

Although not active in **v2.0.0**, the architecture already reserves space for a new core module:

## SECURITY FAMILY (Behavior‑Based Identity & Family Safety Layer)

Purpose:
- behavior‑based recognition of **OWNER**, **FAMILY**, and **STRANGER**  
- offline identity learning (no biometrics, no cloud)  
- safe‑mode for unknown users  
- restricted mode for children (games, multimedia, safe operations only)  
- protection of sensitive operations and system‑level commands  
- **time‑based limits for children (NEW)**  
- **schoolwork bypass mode (NEW)**  

Submodules:

- `identity_engine.py`  
- `behavior_audit.py`  
- `access_control.py`  
- `family_mode.py`  
- `stranger_mode.py`  
- `time_limits.py`  
- `profile_store.json`  

This module becomes a **core security layer** in version **3.0.0**.

---

# 🌟 Future Architecture Extensions (v3.0.0 – v4.0.0)

These modules expand SIRIUS from a system automation runtime into a **full offline household assistant**, while staying safe, predictable, and local‑only.

---

## 🏠 HOME_ASSISTANT (v3.0.0)
General household assistant.

Responsibilities:
- safe household recommendations  
- cleaning tips  
- organization workflows  
- safety‑first guidance  
- integration with IMAGE_ANALYZER  

---

## 🍳 COOKING_ADVISOR (v3.0.0)
Offline cooking and recipe assistant.

Responsibilities:
- recipe generation  
- suggestions based on available ingredients  
- step‑by‑step cooking workflows  
- dietary filters  
- integration with Knowledge Packs  

---

## 🔧 DEVICE_DIAGNOSTICS (v3.0.0)
Safe troubleshooting for household devices.

Responsibilities:
- identifying common device issues  
- providing safe repair suggestions  
- detecting dangerous situations  
- routing to OWNER‑only actions  
- integration with SECURITY FAMILY  

---

## 🎓 SCHOOL_HELPER (v3.0.0)
Offline schoolwork assistant.

Responsibilities:
- math, language, science explanations  
- step‑by‑step reasoning  
- safe educational help  
- image‑based homework recognition  
- integration with SCHOOLWORK PRIORITY MODE  

---

## 🖼 IMAGE_ANALYZER (v3.0.0)
Local image understanding engine.

Responsibilities:
- reading homework from photos  
- identifying household objects  
- detecting device issues visually  
- routing results to correct modules  

---

## 🧭 CONTEXT_ROUTER v3 (v3.0.0)
Smarter intent routing.

Responsibilities:
- detecting household tasks  
- detecting cooking tasks  
- detecting device issues  
- detecting schoolwork  
- routing to new v3 modules  

---

## 📚 KNOWLEDGE_PACKS (v3.0.0+)
Modular offline knowledge expansions.

Responsibilities:
- domain‑specific knowledge (kitchen, repairs, school subjects)  
- safe curated datasets  
- plug‑and‑play expansions  
- no internet required  

---

# 🔌 Module Interconnections

User Input  
↓  
NL Router → AITE → FS‑AGENT  
↓  
CME‑MEM → Workflow Engine  
↓  
Runtime Core → WIN‑CAP → Windows 11 APIs  

### Key relationships:

- NL Router → Plugins  
- Plugins → Runtime Core  
- AITE → FS‑AGENT  
- AITE → CME‑MEM  
- Workflow Engine → Runtime Core  
- WIN‑CAP → Runtime Core  
- **AITE → SECURITY FAMILY (schoolwork bypass)**  
- **IMAGE_ANALYZER → SCHOOL_HELPER / DEVICE_DIAGNOSTICS / HOME_ASSISTANT**  
- **CONTEXT_ROUTER v3 → all v3 modules**  

All communication is **explicit and controlled**.

---

# 📌 Document Status

Current version: **2.0.0 (Stable)**  
Architecture is fully defined and ready for future expansions in v3.0.0 and v4.0.0.
