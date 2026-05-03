<!--
SEO META BLOCK – improves GitHub search visibility
Keywords: local AI, offline AI, Windows automation, AI runtime, workflow automation, modular AI, secure AI, natural language automation, Windows 11 tools, local assistant, AI agent, filesystem automation, command interpreter, context engine, workflow engine, plugin system, runtime core, family safety, behavior-based identity, schoolwork priority
Description: SIRIUS LOCAL AI is a fully local, modular AI runtime for Windows 11. It executes natural‑language commands, manages workflows, automates filesystem operations, and interacts with the OS through a secure capability layer — all without cloud dependencies.
-->

# 🚀 SIRIUS LOCAL AI  
### Modular Local AI Runtime for Windows 11  
### Modular local AI runtime for file management, workflows, and safe command execution on a single PC.

<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-blue">
  <img src="https://img.shields.io/badge/license-MIT-green">
  <img src="https://img.shields.io/badge/platform-Windows%2011-blue">
  <img src="https://img.shields.io/badge/architecture-modular-lightgrey">
  <img src="https://img.shields.io/badge/local%20AI-100%25-blueviolet">
</p>

SIRIUS LOCAL AI is a fully modular, local‑only AI runtime designed to safely execute user commands on a single PC.  
It understands natural language, interprets tasks, manages workflows, loads plugins, and interacts with Windows 11 through a secure capability layer.

This project focuses on **safety**, **predictability**, **modularity**, and **full local control**.

All processing is fully offline — no cloud, no telemetry, no external dependencies.

---

# ℹ️ About SIRIUS LOCAL AI

SIRIUS LOCAL AI is a fully local, modular AI runtime for Windows 11 designed for developers, testers, and power‑users who need safe, deterministic automation on a single PC.  
It provides a complete runtime architecture (Runtime 2.0) with a plugin system, workflow engine, natural‑language routing, Windows capability layer, and advanced safety modules — all running fully offline.

Unlike cloud‑based AI agents, SIRIUS LOCAL AI executes every operation locally, ensuring privacy, predictability, and full user control.  
The system is distributed as clean Python source code and is built as a long‑term, extensible platform for local AI automation.

**Key characteristics:**
- 100% offline, no telemetry  
- modular architecture with replaceable components  
- deterministic behavior and strict safety boundaries  
- plugin ecosystem for extending capabilities  
- workflow automation and NL command routing  
- Windows 11 integration through a secure capability layer  
- upcoming intelligent features (identity, time‑limits, schoolwork priority) in v3.0.0  

SIRIUS LOCAL AI aims to become a new category of software:  
a **local AI runtime** that safely controls a Windows PC through natural language.

---

# 🧩 Core Philosophy

- **Local‑only AI** — no cloud, no external services  
- **Modular architecture** — every capability is isolated  
- **Predictable behavior** — no hidden actions, no automation without confirmation  
- **Human‑controlled** — SIRIUS never performs destructive actions without explicit approval  
- **Extensible** — Plugin System 2.0 allows new features without modifying the core  
- **Deterministic** — Runtime 2.0 ensures stable, repeatable behavior  
- **Family‑safe** — SECURITY FAMILY (v3.0.0) introduces identity, time‑limits, and schoolwork priority  

---

# 🏗 Architecture Overview (v2.0.0)

SIRIUS LOCAL AI is composed of independent modules that communicate through defined interfaces.  
Each module has a single responsibility and is replaceable.

---

## 🖼 Architecture Diagram (Placeholder)

> A high‑level architecture diagram will be added here in a future update.

<p align="center">
  <img src="docs/architecture_diagram_placeholder.png" width="600">
</p>

---

# 🔧 Core Modules (v2.0.0)

## 1. Runtime Core 2.0
Central orchestrator of the entire system.

**Responsibilities:**
- module initialization  
- lifecycle management  
- plugin loading  
- event routing  
- workflow dispatch  
- security boundaries  

---

## 2. Filesystem Agent (FS‑AGENT 2.0)
Safe, validated filesystem operations.

**Responsibilities:**
- moving, copying, deleting  
- path validation  
- safety checks  
- conflict detection  
- rollback‑safe operations  

---

## 3. Natural Language Router (NL Router 2.0)
Understands user commands and routes them to modules or plugins.

**Responsibilities:**
- command type recognition  
- parameter extraction  
- plugin NL command detection  
- fallback interpretation  
- preventing unsafe or ambiguous actions  

---

## 4. Context Memory Engine (CME‑MEM 2.0)
Maintains workflow and system context.

**Responsibilities:**
- tracking recent actions  
- storing paths and states  
- providing contextual suggestions  
- supporting multi‑step workflows  

---

## 5. Workflow Engine 2.0
Controls multi‑step logic and plugin workflows.

**Responsibilities:**
- workflow state machine  
- next‑step prediction  
- validating transitions  
- deterministic behavior  

---

## 6. GUI Layer 2.0
Modular user interface.

**Responsibilities:**
- rendering plugin buttons  
- executing GUI actions  
- integrating with Runtime Core  
- providing visual feedback  

---

## 7. Email Composer
Generates structured email text (never sends).

**Responsibilities:**
- email drafts  
- professional responses  
- structured text generation  

---

## 8. Automatic Input Triage Engine (AITE 2.0)
Automatically classifies user inputs.

**Recognized Types:**
- text  
- image/photo  
- application/installer  
- documents  
- **(v3.0.0) schoolwork — triggers Schoolwork Priority Mode**

**Responsibilities:**
- input type detection  
- routing  
- metadata generation  
- integration with FS‑AGENT and CME‑MEM  
- **schoolwork bypass for FAMILY restrictions**  

---

## 9. Windows System Capabilities Layer (WIN‑CAP 2.0)
Transforms SIRIUS into a **true local OS‑level AI agent**.

**Responsibilities:**
- exposing high‑level system capabilities  
- enforcing permissions  
- safe wrappers around OS operations  
- enabling multi‑step system actions  

**Submodules:**
- `file_ops`  
- `app_ops`  
- `window_ops`  
- `audio_ops`  
- `system_context`  

---

## 10. Plugin System 2.0
Extensible plugin ecosystem.

**Capabilities:**
- NL commands  
- AI tasks  
- workflows  
- AI loop rules  
- GUI elements  

Official plugins include:
- automation  
- clipboard  
- example  
- file_manager  
- notes  
- system_tools  
- translator  

---

# 🔐 SECURITY FAMILY (planned for v3.0.0)

A new core module introducing:

- behavior‑based identity (OWNER / FAMILY / STRANGER)  
- time‑limits for children  
- restricted mode for unknown users  
- Schoolwork Priority Mode — schoolwork always allowed  
- offline identity learning  
- safe‑mode for sensitive operations  

This module becomes a core part of the intelligent runtime in v3.0.0.

---

# 🔌 Module Interconnections

- **NL Router → FS‑AGENT:** determines file operations  
- **NL Router → Plugins:** routes NL commands  
- **CME‑MEM → Workflow Engine:** provides context  
- **AITE → FS‑AGENT:** routes inputs based on type  
- **AITE → CME‑MEM:** stores metadata  
- **AITE → SECURITY FAMILY:** schoolwork detection → bypass time limits  
- **WIN‑CAP → Runtime Core:** privileged capability layer  
- **Runtime Core → all modules:** initialization and security  
- **Plugins → Runtime Core:** register capabilities  

All communication is explicit and controlled.

---

# 🗺 Roadmap (High‑Level)

### **v2.0.0 – Current Stable Release**
- Runtime 2.0  
- Plugin System 2.0  
- Workflow Engine 2.0  
- AI Loop 2.0  
- GUI 2.0  
- AITE 2.0  
- WIN‑CAP 2.0  
- Full documentation refresh  

### **v3.0.0 – Intelligent Runtime**
- AI‑assisted triage  
- semantic workflows  
- advanced GUI/tray/voice integration  
- contextual automation  
- **SECURITY FAMILY (identity, time‑limits, schoolwork priority)**  

### **v4.0.0 – Self‑Repair & Health‑Check Layer**
- integrity checks  
- safe automatic repairs  
- patch suggestions  
- system‑wide health reporting  

---

# 📄 License
MIT License.

---

# 👤 Author
**Richard Pizem**  
Independent Researcher

---

# ⭐ Vision
SIRIUS LOCAL AI aims to become the **first fully local, modular AI agent** capable of safely controlling a Windows 11 PC through natural language.

A personal AI that works *with you*, not instead of you.
