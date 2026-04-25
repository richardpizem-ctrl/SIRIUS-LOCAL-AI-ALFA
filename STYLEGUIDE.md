🎨 STYLEGUIDE – SIRIUS LOCAL AI ALFA
This document defines the unified code style, naming conventions, module structure, and cleanliness rules for the project. The goal is to maintain consistency, readability, and a professional standard across the entire system.

⚠️ ALPHA WARNING
SIRIUS LOCAL AI ALFA interacts with Windows 11 system APIs, filesystem operations, window management, and application control. The project is currently in ALPHA, and module behavior may evolve as development continues.

Some operations may require elevated permissions (UAC).

Windows Defender or SmartScreen may classify the runtime as an “Unknown App”.

Antivirus tools may generate false positives during development.

Modules must run with the same privilege level as the applications they control.

All processing is fully local; no data leaves the user's PC.
Users are encouraged to test features independently. This is an ALPHA‑stage developer tool — the author does not provide individual guidance for basic operations.

Core Principles

code must be clean, readable, and modular

no monolithic functions or modules

no magic constants — everything must be named

no hidden side effects

every module must follow SRP (Single Responsibility Principle)

security always has priority over convenience

predictable, transparent behavior

consistent structure across all modules

minimal cognitive load for future maintainers

Naming Conventions

Variables

lower_snake_case

short but descriptive

no meaningless abbreviations
Examples: target_path, pending_action, user_confirmation_required

Functions

lower_snake_case

name must express an action

verbs first, nouns second
Examples: resolve_target_folder(), validate_path(), generate_confirmation_dialog(), load_context_state()

Classes / Modules

PascalCase

name = responsibility of the module
Examples: FilesystemAgent, CommandInterpreter, ContextMemoryEngine, WorkflowTracker

Constants

UPPER_SNAKE_CASE

must be descriptive
Examples: MAX_RETRY_COUNT, DEFAULT_TIMEOUT_MS

File Structure
Each module has its own folder:
/runtime
/filesystem
/commands
/context
/workflow
/ui
/email
/ui_components
/ui_components/animations

Each folder contains:

init.py

main module

helper utilities (if needed)

no cross‑module imports except through public interfaces

Function Length

ideal length: 5–25 lines

maximum: 50 lines

if a function grows too large, split it

avoid deeply nested logic

prefer early returns over complex branching

Comments

comments only where necessary

comments explain why, not what

avoid redundant comments

Error Messages

clear, concise, informative

never aggressive or vague

must include a reason + recommendation

avoid technical jargon unless necessary

Security Rules in Code

no operation may bypass user confirmation

all file operations must be validated

no direct deletion without double confirmation

no network operations in any module

no hidden background tasks

no automatic actions without explicit approval

no implicit state sharing

all privileged operations must go through WIN‑CAP

Testing
Every module must include:

basic tests

error‑state tests

security‑constraint tests

input‑validation tests

predictable behavior tests

no reliance on external network or cloud

Logging

concise and technical

no sensitive data

format: [MODULE] action – status
Example: [FS-AGENT] move_file – confirmed

Formatting

indentation: 4 spaces

max line width: 100 characters

blank line between logical blocks

no trailing spaces

consistent import ordering

group imports: standard → third‑party → internal

Module Boundaries

modules may not access each other's internals

communication must go through public interfaces

Runtime Core is the only module allowed to initialize all others

no circular imports

no global mutable state

Document Status
Current version: ALPHA
The styleguide may evolve as the system approaches Phase 4 stability.
