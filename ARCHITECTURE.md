# SIRIUS LOCAL AI ALFA – Project Architecture

SIRIUS LOCAL AI ALFA is a modular local AI runtime designed to safely and accurately execute commands within a single PC.  
The architecture is divided into independent modules that communicate through defined interfaces and maintain a consistent user context.

---

## 1. Runtime Core
The foundational system layer responsible for:

- module initialization  
- lifecycle management  
- task scheduling  
- security restrictions (sandboxing, allowed operations)  

---

## 2. Filesystem Agent (FS‑AGENT)
Responsible for all file operations:

- moving, copying, deleting  
- path validation  
- safety confirmations  
- user feedback  

FS‑AGENT never performs an action without explicit confirmation.

---

## 3. Command Interpreter (CME)
The layer that translates user commands into internal actions:

- command type recognition  
- parameter extraction  
- deciding which module should execute the action  
- generating questions such as “Where to?” or “Confirm?”  

---

## 4. Context Memory Engine (CME‑MEM)
Maintains the full PC and workflow context:

- user’s recent actions  
- last used paths and folders  
- state of ongoing tasks  
- contextual suggestions for next steps  

---

## 5. Workflow Tracker
Responsible for:

- tracking the sequence of steps  
- predicting the next logical action  
- automatic suggestions (e.g., “Do you want to insert this into README?”)  

---

## 6. UI Confirm Module
Layer for interactive confirmation tables:

- selecting the target folder  
- confirming actions  
- safety dialogs  
- automatic window opening based on command type  

---

## 7. Email Composer (no sending)
This module generates:

- email drafts  
- structured text  
- professional responses  

It never sends anything — it only prepares content.

---

## 8. Automatic Input Triage Engine (AITE)
A module that automatically detects the type of input and assigns it to the correct category without requiring questions.

**Recognized Types:**

- Text → stored in text storage  
- Photo / image → moved to the gallery (media storage)  
- Application / installer → placed into the applications section  

**Functions:**

- automatic input type detection  
- routing to the correct module  
- metadata preparation  
- integration with FS‑AGENT and CME‑MEM  

AITE ensures that SIRIUS AI understands what the user inserted or downloaded and classifies it immediately.

---

## 9. Windows System Capabilities Layer (WIN‑CAP)
A dedicated integration layer that allows SIRIUS LOCAL AI to work with the full Windows 11 environment through controlled, high‑level capabilities.

**Core responsibilities:**

- provide a catalog of OS‑level capabilities (files, apps, windows, audio, devices)  
- expose safe, abstracted functions to the AI (no raw system calls from the model)  
- enforce permissions and allowed scopes (which folders, which apps, which devices)  

**Example capability modules:**

- `file_ops`  
  - find projects (e.g., “find all SIRIUS projects and open the latest”)  
  - create structured folders (e.g., “create v1.3.0 folder with substructure”)  
  - open folders in Explorer  

- `app_ops`  
  - launch applications (e.g., “start Real-Time MIDI Notation”)  
  - detect running apps (e.g., VS Code)  
  - focus or arrange windows  

- `window_ops`  
  - snap windows left/right  
  - position SIRIUS next to VS Code  
  - basic window layout automation  

- `audio_ops`  
  - get current audio output device  
  - compare with preferred device  
  - switch output if needed (e.g., “if sound is not going to the right device, change it”)  

**Behavioral pattern:**

For commands like:

- “Find all SIRIUS projects on disk and open the latest.”  
- “Launch Real-Time MIDI Notation and place its window next to VS Code.”  
- “Check if audio is going to the correct device and switch if not.”  
- “Create a new folder for v1.3.0 and prepare the structure.”

SIRIUS will:

1. understand the request (CME)  
2. decompose it into concrete OS actions  
3. execute them via WIN‑CAP modules (file_ops, app_ops, window_ops, audio_ops)  
4. coordinate confirmations via UI Confirm Module and FS‑AGENT where needed  

WIN‑CAP makes SIRIUS a true **local OS‑level AI agent** instead of a pure text assistant.

---

## 10. Modularity and Extensibility
Each module is independent and can be extended with:

- new command types  
- new UI components  
- new workflow logic  
- new security layers  
- new types of automatic triage  
- new Windows capabilities (additional WIN‑CAP modules)  

---

## 11. Project Status
**ALPHA** – architecture definition, module design, and implementation preparation.
