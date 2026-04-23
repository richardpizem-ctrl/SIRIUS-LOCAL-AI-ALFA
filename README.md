SIRIUS LOCAL AI ALFA
A modular local AI runtime for file management, workflow automation, and safe command execution within a single PC.
The project is designed as an extensible architecture with separated modules for filesystem operations, command interpretation, context memory, workflow tracking, UI confirmations, and automatic input triage.

Main Features
automatic file and folder relocation

contextual “Where to?” and “Confirm?” tables

safety confirmations before every action

modular architecture (filesystem, command interpreter, context memory, workflow tracker, UI)

email draft generation without automatic sending

AI maintains the full concept of the PC and the user’s recent actions

extensible modules for future problem domains

Automatic Input Triage Engine (AITE) – AI automatically detects whether the input is text, a photo, or an application and routes it correctly

Automatic Input Triage Engine (AITE)
AITE is a module that automatically detects the type of input and assigns it to the correct category without asking the user.

Recognized types
Text → stored in the text storage

Photo / image → moved to the gallery (media storage)

Application / installer → placed into the applications section

Functions
automatic input type detection

routing to the correct storage

metadata generation

integration with FS‑AGENT and CME‑MEM

AITE ensures that SIRIUS AI immediately understands what the user inserted or downloaded and classifies it correctly.

Project Status
ALPHA – architecture design and module preparation.
