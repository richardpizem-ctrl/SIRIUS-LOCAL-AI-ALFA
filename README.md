# 🚀 SIRIUS LOCAL AI ALFA  
### Modular Local AI Runtime for Windows 11

SIRIUS LOCAL AI ALFA is a fully modular, local‑only AI runtime designed to safely execute user commands on a single PC.  
It understands natural language, interprets tasks, manages workflows, and interacts with the Windows 11 environment through a secure capability layer.

This project focuses on **safety**, **predictability**, **modularity**, and **full local control**.

---

# 🧩 Core Philosophy

- **Local‑only AI** — no cloud, no external dependencies  
- **Modular architecture** — every capability is isolated  
- **Predictable behavior** — no hidden actions, no automation without confirmation  
- **Human‑controlled** — SIRIUS never performs destructive actions without explicit approval  
- **Extensible** — new modules can be added without breaking the system  

---

# 🏗 Architecture Overview

SIRIUS LOCAL AI ALFA is composed of independent modules that communicate through defined interfaces.  
Each module has a single responsibility and is replaceable.

---

## 1. Runtime Core
Central system layer.

**Responsibilities:**
- module initialization  
- lifecycle management  
- task scheduling  
- security restrictions  

---

## 2. Filesystem Agent (FS‑AGENT)
Safe file operations.

**Responsibilities:**
- moving, copying, deleting  
- path validation  
- action confirmations  
- user feedback  

FS‑AGENT never performs an action without explicit confirmation.

---

## 3. Command Interpreter (CME)
Understands user commands and converts them into internal actions.

**Responsibilities:**
- command type recognition  
- parameter extraction  
- routing to correct module  
- generating “Where to?” and “Confirm?” questions  

---

## 4. Context Memory Engine (CME‑MEM)
Maintains workflow and system context.

**Responsibilities:**
- tracking recent actions  
- storing paths and states  
- providing contextual suggestions  

---

## 5. Workflow Tracker
Controls multi‑step logic.

**Responsibilities:**
- tracking workflow  
- predicting next steps  
- generating automatic suggestions  

---

## 6. UI Confirm Module
Interactive confirmation layer.

**Responsibilities:**
- selecting target folders  
- confirming actions  
- safety dialogs  
- automatic window opening  

---

## 7. Email Composer
Generates structured email text (never sends).

**Responsibilities:**
- email drafts  
- professional responses  
- structured text generation  

---

## 8. Automatic Input Triage Engine (AITE)
Automatically classifies user inputs.

**Recognized Types:**
- text → text storage  
- image/photo → media storage  
- application/installer → applications section  

**Responsibilities:**
- input type detection  
- routing  
- metadata generation  
- integration with FS‑AGENT and CME‑MEM  

---

## 9. Windows System Capabilities Layer (WIN‑CAP)
The module that transforms SIRIUS into a **true local OS‑level AI agent**.

**Purpose:** Provide safe, abstracted access to Windows 11 system functions.

**Responsibilities:**
- exposing high‑level system capabilities  
- enforcing permissions and allowed scopes  
- safe wrappers around OS operations  
- enabling multi‑step system actions  

**Submodules:**
- `file_ops` — find projects, open folders, create structured directories  
- `app_ops` — launch apps, detect running apps, focus windows  
- `window_ops` — snap windows, arrange layouts, position SIRIUS next to VS Code  
- `audio_ops` — detect audio output device, switch to preferred device  

**Examples of enabled commands:**
- “Find all SIRIUS projects on disk and open the latest.”  
- “Launch Real-Time MIDI Notation and place its window next to VS Code.”  
- “Check if audio is going to the correct device and switch if not.”  
- “Create a new folder for v1.3.0 and prepare the structure.”  

WIN‑CAP allows SIRIUS to understand natural language, decompose tasks, and execute them safely.

---

# 🔌 Module Interconnections

- **CME → FS‑AGENT:** decides what action should be executed  
- **CME → UI Confirm:** generates questions  
- **CME‑MEM → Workflow Tracker:** provides context  
- **AITE → FS‑AGENT:** routes inputs based on type  
- **AITE → CME‑MEM:** stores metadata  
- **WIN‑CAP → CME:** provides available system capabilities  
- **WIN‑CAP → Runtime Core:** registered as a privileged capability layer  
- **Runtime Core → all modules:** initialization and security  

---

# 🗺 Roadmap (High‑Level)

### **ALPHA (current)**  
Architecture definition, module design, documentation.

### **BETA**  
Core implementation (Runtime, CME, FS‑AGENT, CME‑MEM).

### **BETA 2**  
Feature expansion, workflow logic, Email Composer.

### **RELEASE CANDIDATE**  
Stabilization, testing, API documentation.

### **VERSION 1.0**  
First stable release.

### **Post‑release**  
- UI Automation Layer  
- Voice Command Layer  
- Plugin API  
- System Monitoring  
- WIN‑CAP expansion  

---

# 📄 License
MIT License.

---

# 👤 Author
**Richard Pizem**  
Independent Researcher

---

# ⭐ Vision
SIRIUS LOCAL AI ALFA aims to become the **first fully local, modular AI agent** capable of safely controlling a Windows 11 PC through natural language.

A personal AI that works *with you*, not instead of you.

