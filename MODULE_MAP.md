# Module Map – SIRIUS LOCAL AI ALFA

This document defines all modules of the project, their purpose, responsibilities, and interconnections.  
It serves as an architectural orientation map.

---

## 1. Runtime Core
**Purpose:** Central system layer.  
**Responsibilities:**
- module initialization  
- task scheduling  
- security restrictions  
- lifecycle management  

---

## 2. Filesystem Agent (FS‑AGENT)
**Purpose:** Safe file operations.  
**Responsibilities:**
- moving, copying, deleting  
- path validation  
- action confirmations  
- user feedback  

---

## 3. Command Interpreter (CME)
**Purpose:** Translation of user commands.  
**Responsibilities:**
- recognizing command type  
- extracting parameters  
- deciding which module executes the action  
- generating “Where to?” and “Confirm?” questions  

---

## 4. Context Memory Engine (CME‑MEM)
**Purpose:** Maintaining context and recent actions.  
**Responsibilities:**
- tracking recent user actions  
- storing paths and states  
- providing contextual suggestions  

---

## 5. Workflow Tracker
**Purpose:** Logic of step sequences.  
**Responsibilities:**
- tracking workflow  
- predicting the next step  
- generating automatic action suggestions  

---

## 6. UI Confirm Module
**Purpose:** Interactive confirmation tables.  
**Responsibilities:**
- selecting the target folder  
- confirming actions  
- safety dialogs  
- automatic window opening based on command type  

---

## 7. Email Composer
**Purpose:** Generating email text (without sending).  
**Responsibilities:**
- email drafts  
- professional responses  
- structured text generation  

---

## 8. Automatic Input Triage Engine (AITE)
**Purpose:** Automatic detection and classification of input type.  
**Responsibilities:**
- detecting input type (text, image, application)  
- routing to the correct storage  
- metadata generation  
- integration with FS‑AGENT and CME‑MEM  

AITE ensures that SIRIUS AI immediately understands what the user inserted or downloaded and classifies it correctly without asking questions.

---

## 9. Future Modules (Extensibility)
**Possible future modules:**
- UI Automation Layer  
- Voice Command Layer  
- System Monitoring Layer  
- Plugin API  

---

## 10. Module Interconnections
- **CME → FS‑AGENT:** decides what action should be executed  
- **CME → UI Confirm:** generates questions  
- **CME‑MEM → Workflow Tracker:** provides context  
- **AITE → FS‑AGENT:** routes inputs based on type  
- **AITE → CME‑MEM:** stores metadata about the input  
- **Runtime Core → all modules:** initialization and security  
