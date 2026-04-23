SIRIUS LOCAL AI ALFA – Project Architecture
SIRIUS LOCAL AI ALFA is a modular local AI runtime designed to safely and accurately execute commands within a single PC.
The architecture is divided into independent modules that communicate through defined interfaces and maintain a consistent user context.

1. Runtime Core
The foundational system layer responsible for:

module initialization

lifecycle management

task scheduling

security restrictions (sandboxing, allowed operations)

2. Filesystem Agent (FS‑AGENT)
Responsible for all file operations:

moving, copying, deleting

path validation

safety confirmations

user feedback

FS‑AGENT never performs an action without explicit confirmation.

3. Command Interpreter (CME)
The layer that translates user commands into internal actions:

command type recognition

parameter extraction

deciding which module should execute the action

generating questions such as “Where to?” or “Confirm?”

4. Context Memory Engine (CME‑MEM)
Maintains the full PC and workflow context:

user’s recent actions

last used paths and folders

state of ongoing tasks

contextual suggestions for next steps

5. Workflow Tracker
Responsible for:

tracking the sequence of steps

predicting the next logical action

automatic suggestions (e.g., “Do you want to insert this into README?”)

6. UI Confirm Module
Layer for interactive confirmation tables:

selecting the target folder

confirming actions

safety dialogs

automatic window opening based on command type

7. Email Composer (no sending)
This module generates:

email drafts

structured text

professional responses

It never sends anything — it only prepares content.

8. Automatic Input Triage Engine (AITE)
A module that automatically detects the type of input and assigns it to the correct category without requiring questions:

Recognized Types:
Text → stored in text storage

Photo / image → moved to the gallery (media storage)

Application / installer → placed into the applications section

Functions:
automatic input type detection

routing to the correct module

metadata preparation

integration with FS‑AGENT and CME‑MEM

AITE ensures that SIRIUS AI understands what the user inserted or downloaded and classifies it immediately.

9. Modularity and Extensibility
Each module is independent and can be extended with:

new command types

new UI components

new workflow logic

new security layers

new types of automatic triage

10. Project Status
ALPHA – architecture definition, module design, and implementation preparation.
