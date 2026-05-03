# 📜 CHANGELOG – SIRIUS LOCAL AI (v2.0.0)

All notable changes to this project are documented in this file.  
The project follows a clean, structured, version‑based changelog format.

---

# 2.0.0 – Full System Stabilization (Current Release)
**Status:** Stable  
**Phase:** ALFA → BETA transition  
**Target:** Complete Runtime 2.0 architecture

### Added
- Runtime Core 2.0  
- Plugin System 2.0 (NL commands, AI tasks, workflows, AI loop rules, GUI elements)  
- Natural Language Router 2.0  
- Workflow Engine 2.0  
- AI Loop 2.0  
- GUI Layer 2.0  
- AITE 2.0 (Automatic Input Triage Engine)  
- WIN‑CAP 2.0 (Windows System Capabilities Layer)  
- Full plugin suite (automation, clipboard, example, file_manager, notes, system_tools, translator)  
- Stabilized core modules (runtime, context, filesystem, commands)  
- Updated documentation set (ARCHITECTURE, MODULE_MAP, RELEASE_NOTES, ROADMAP, SECURITY, INSTALLATION)  
- Complete documentation refresh for Runtime 2.0 architecture  

### Improved
- deterministic behavior across all modules  
- module isolation and safety boundaries  
- plugin loading and runtime orchestration  
- workflow execution stability  
- NL routing accuracy and fallback logic  
- filesystem safety checks  
- context memory consistency  
- GUI responsiveness and safety prompts  

### Security
- strict no‑network policy  
- safe plugin sandboxing  
- validated filesystem operations  
- deterministic AI loop execution  
- controlled access to Windows capabilities  
- expanded safety boundaries for destructive operations  

### (NEW – v3.0.0 PREVIEW)
- SECURITY FAMILY module scaffolding  
- behavior‑based identity (OWNER / FAMILY / STRANGER)  
- restricted mode for children  
- safe‑mode for unknown users  
- time‑based limits for children  
- **Schoolwork Priority Mode** — schoolwork always bypasses FAMILY restrictions and time limits  
- integration hooks for AITE → SECURITY FAMILY (schoolwork detection)  
- new submodule: `time_limits.py`  
- new submodule: `schoolwork_detector.py` (planned)  
- new submodule: `identity_engine.py` (planned)  
- new submodule: `family_mode.py` (planned)  

---

# 1.0.0 – Initial Stable Release (Historical)
**Status:** Completed  
**Target:** First fully working modular system

### Added
- complete modular architecture  
- Runtime Core  
- Command Interpreter (CME)  
- Filesystem Agent (FS‑AGENT)  
- Context Memory Engine (CME‑MEM)  
- Workflow Tracker  
- UI Confirm Module  
- Automatic Input Triage Engine (AITE)  
- Windows System Capabilities Layer (WIN‑CAP)  
- full documentation set  

### Improved
- safety boundaries  
- confirmation workflows  
- deterministic behavior  
- module isolation  

### Security
- strict no‑network policy  
- double‑confirmation deletion  
- path validation  
- safe fallback behavior  

---

# 0.9.0 – Pre‑Release Architecture Freeze
### Added
- initial module structure  
- early WIN‑CAP integration  
- basic workflow engine  
- initial UI confirmation layer  

### Changed
- reorganized project folders  
- improved module boundaries  

---

# 0.8.0 – Early Prototype
### Added
- basic command interpreter  
- early filesystem operations  
- first workflow tests  

---

# Document Status
Current version: **2.0.0 (Stable)**  
Changelog will continue to evolve as new versions (2.x → 3.0.0 → 4.0.0) are released.
