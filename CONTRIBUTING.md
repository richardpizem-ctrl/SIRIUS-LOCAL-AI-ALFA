# 🤝 Contributing Guidelines – SIRIUS LOCAL AI (v5.8 UNIFIED)

Thank you for your interest in contributing to **SIRIUS LOCAL AI**.  
This document defines the rules, processes, and expectations for all contributors.  
The goal is to maintain a **clean, safe, modular, deterministic, explainable, and intelligent** local AI system built on the **Unified Orchestration, PanelAPI, TimeCore/Guard & Enhanced COLNIK‑AUTONOMY Architecture 5.8**.

All processing is fully local.  
No data leaves your device.

Version **5.8** updates these guidelines to include:

- **Unified Orchestrator (`sirius_orchestrator.py`)**  
- **PanelAPI & Interactive [ÁNO/NIE] Confirmation Loops**  
- **TimeCore Temporal Tracking & Guard Security Supervision**  
- **Unified Reasoning & Deep Explainability Architecture 5.8**  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP (Explainability Engines)**  
- **Reasoning Engine 5.8 (multi-hop, inheritance, transitivity)**  
- **Proof Tree & Evidence Tree Foundations**  
- **Confidence Scoring Foundations**  
- **Rule Chaining Foundations**  
- **Workflow Engine 5.8 (explainability routing)**  
- **Unified Knowledge Graph 5.8 (comfort commands, stabilized autoload)**  
- **AITE 5.8 (semantic + explainability triage)**  
- **Identity Engine 3.1**  
- **SECURITY FAMILY 5.x**  
- **Schoolwork Engine 5.8**  
- **System Agent 5**  
- **COLNIK‑6.x Validation Layer (Standard & IPC Mode)**  
- **AUTONOMY 6.x (Control & Triage Mode)**  
- hardened deterministic routing  
- cross-platform safety rules  

---

# 1. 🔐 Core Principles

- **Security has absolute priority**  
- **Explainability must remain transparent and deterministic**  
- **No action may bypass user confirmations (`PanelAPI` [ÁNO/NIE])**  
- **Modular architecture must remain clean and separated**  
- **All contributions must respect existing module APIs and `sirius_orchestrator.py`**  
- **No network operations or external data transmission**  
- **No hidden automation or background actions without TimeCore/Guard supervision**  
- **Every change must preserve system transparency and predictability**  
- **No global mutable state**  
- **No circular imports**  
- **Deterministic, reversible behavior whenever possible**  
- **Plugin System 5.x rules must be followed**  
- **Safety-critical modules must never be weakened or bypassed**, including:  
  - SECURITY FAMILY 5.x  
  - Identity Engine 3.1  
  - Schoolwork Engine 5.8  
  - Time-Limits Engine v3  
  - Self-Repair Layer 5.8  
  - UI Automation Engine 5.1  
  - System Agent 5  
  - ENVOY Execution/Permission Layers 5  
  - COLNIK‑6.x Validation Layer (Standard & IPC Mode)  
  - AUTONOMY 6.x (Control & Triage Mode)  
  - PanelAPI & TimeCore/Guard Supervision  
- **Reasoning Engine 5.8 must not be extended unsafely**  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP must remain transparent and correct**  

---

# 2. 🚀 How to Start

1. **Fork** the repository  
2. **Create a new branch** for your change  
3. **Implement** the change according to the Runtime 5.8 architecture  
4. **Test** it in your local environment (PC or Mobile)  
5. **Submit a Pull Request** with a clear description  

Recommended branch naming:
- feature/<name>  
- fix/<name>  
- refactor/<name>  
- docs/<name>  

---

# 3. 🧼 Code Style

All contributions must follow the project’s **STYLEGUIDE.md**.

Key rules:

- clean, readable, consistent  
- no magic constants  
- clear naming of functions and modules  
- comments explain **why**, not **what**  
- avoid unnecessary complexity  
- follow the architecture and module map  
- functions ideally 5–25 lines  
- no monolithic modules  
- no deep nesting — prefer early returns  
- imports grouped: standard → third-party → internal  
- plugin code must follow Plugin API 5.x  
- SECURITY FAMILY 5.x code must follow safety-first design  
- SCHOOLWORK ENGINE 5.8 must remain intact and non-bypassable  
- Reasoning Engine 5.8 integrations must be deterministic and safe  
- Self-Repair Layer 5.8 must not be disabled or bypassed  
- UI Automation Engine 5.1 integrations must follow deterministic fallback rules  
- System Agent 5 must validate all system-level actions  
- ENVOY 5 must sanitize all system requests  
- COLNIK‑6.x must validate all KG mutations, workflow steps, and IPC payloads  
- AUTONOMY 6.x must manage proposals and Triage Mode securely  
- PanelAPI and TimeCore/Guard components must remain active and uncompromised  
- KG_EXPLAIN & KG_EXPLAIN_DEEP output must remain transparent and correct  

---

# 4. 🧪 Testing Requirements

Every change must include:

- basic functional tests  
- verification of security constraints  
- input validation  
- error-state testing  
- predictable behavior under invalid inputs  
- no silent failures  
- no destructive operations without confirmation  
- no reliance on network access  

If your change affects:

- **FS-AGENT 5.x** → test path validation, safety prompts  
- **NL Router 5.x** → test semantic routing and ambiguity handling  
- **Workflow Engine 5.8 & Orchestrator** → test semantic transitions, `sirius_orchestrator.py` routing + explainability routing  
- **Reasoning Engine 5.8** →  
  - multi-hop inference  
  - inheritance reasoning  
  - transitive reasoning  
  - deterministic rule chaining  
  - proof tree nodes  
  - evidence trees  
  - confidence scoring  
- **WIN-CAP 5.x** → test safe fallback behavior  
- **Plugin System 5.x** → test manifest, NL commands, tasks, workflows, GUI elements  
- **UI Automation Engine 5.1** →  
  - fuzzy matching behavior  
  - fallback logic  
  - deterministic retries  
  - safe OS-level routing  
- **SECURITY FAMILY 5.x** →  
  - identity classification (OWNER / FAMILY / STRANGER)  
  - time-limit enforcement v3  
  - schoolwork bypass logic  
  - safe-mode restrictions  
  - STRANGER-mode protections  
- **Schoolwork Engine 5.8** →  
  - subject detection  
  - difficulty scoring  
  - bypass logic  
- **Self-Repair Layer 5.8** →  
  - integrity checks  
  - fallback behavior  
- **System Agent 5** →  
  - validation of all system actions  
  - deterministic safety enforcement  
- **ENVOY Execution/Permission Layers 5** →  
  - sanitization  
  - identity filtering  
  - safe routing  
- **COLNIK‑6.x Validation Layer (Standard & IPC Mode)** →  
  - KG mutation validation  
  - workflow step authorization  
  - anomaly detection  
  - IPC synchronization with AUTONOMY  
- **AUTONOMY 6.x (Control & Triage Mode)** →  
  - proposal generation  
  - confirmation logic  
  - Triage Mode execution  
  - safe autonomous routing  
- **PanelAPI, TimeCore & Guard** →  
  - interactive [ÁNO/NIE] prompt handling  
  - temporal execution timing  
  - runtime anomaly supervision  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP** →  
  - correct inference history  
  - deterministic explanation output  

---

# 5. 📥 Pull Request Rules

A valid PR must include:

- clear description of the change  
- explanation of why the change is needed  
- reference to related Issues (if applicable)  
- test results or manual test notes  

Restrictions:

- no large PRs — prefer smaller, well-structured steps  
- PRs must **not** modify the architecture without prior discussion  
- PRs must follow module boundaries  
- PRs must not introduce new dependencies without approval  
- PRs must not break determinism or safety guarantees  
- plugin PRs must include updated manifest if needed  
- PRs must not weaken SECURITY FAMILY 5.x protections  
- PRs must not interfere with SCHOOLWORK ENGINE 5.8  
- PRs must not disable or bypass the Self-Repair Layer  
- PRs must not misuse Reasoning Engine 5.8  
- PRs must not compromise UI Automation Engine 5.1 safety rules  
- PRs must not bypass System Agent 5 validation  
- PRs must not bypass ENVOY Execution/Permission Layers 5  
- PRs must not bypass COLNIK‑6.x validation or IPC synchronization  
- PRs must not bypass PanelAPI user confirmation gates  
- PRs must not disable TimeCore/Guard supervision  
- PRs must not distort or hide KG_EXPLAIN or KG_EXPLAIN_DEEP inference history  
- PRs must not misuse AUTONOMY 6.x decision logic or Triage Mode  

---

# 6. ❌ What We Do Not Accept

- network-based features  
- automatic actions without confirmation  
- bypassing security rules  
- monolithic modules  
- undocumented API changes  
- hidden background tasks  
- features that break modularity  
- unsafe filesystem or system operations  
- code that relies on OS-specific hacks  
- contributions that reduce clarity or predictability  
- plugins that violate Plugin API 5.x  
- attempts to disable FAMILY mode, time limits, or schoolwork engine  
- attempts to weaken STRANGER-mode protections  
- attempts to bypass Identity Engine 3.1  
- attempts to disable Self-Repair Layer or TimeCore/Guard supervision  
- unsafe Reasoning Engine extensions  
- unsafe or non-deterministic UI automation behavior  
- attempts to bypass System Agent 5  
- attempts to bypass ENVOY 5  
- attempts to bypass COLNIK‑6.x or PanelAPI  
- attempts to manipulate KG_EXPLAIN or KG_EXPLAIN_DEEP output  
- attempts to misuse AUTONOMY 6.x decision logic or Triage Mode  

---

# 7. 💬 Communication

All discussions take place through:

- **Issues**  
- **Pull Request comments**  

Guidelines:

- be respectful and constructive  
- provide technical reasoning  
- avoid vague or incomplete reports  
- include reproduction steps when reporting issues  

---

# 8. 🧭 Architecture Compliance

All contributions must respect:

- **ARCHITECTURE.md (v5.8)**  
- **MODULE_MAP.md**  
- **STYLEGUIDE.md**  
- **SECURITY.md**  
- **Plugin API 5.x**  
- **SECURITY FAMILY 5.x design rules**  
- **Schoolwork Engine 5.8 rules**  
- **Self-Repair Layer 5.8 requirements**  
- **UI Automation Engine 5.1 specifications**  
- **System Agent 5 safety model**  
- **ENVOY 5 sanitization rules**  
- **COLNIK‑6.x validation rules (Standard & IPC Mode)**  
- **AUTONOMY 6.x Control & Triage Mode rules**  
- **PanelAPI, TimeCore & Guard supervision rules**  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP explainability rules**  
- **Unified Orchestrator (`sirius_orchestrator.py`) execution rules**  

Breaking architectural boundaries requires prior approval.

---

# 9. 📝 Commit Message Style

Use clear, structured commit messages:

- feat: added orchestrator PanelAPI integration  
- fix: corrected COLNIK IPC synchronization  
- refactor: simplified reasoning rule chaining  
- docs: updated INSTALLATION.md  

Avoid vague messages like “update”, “fix stuff”, “changes”.

---

# 10. 🧒 Family Safety Requirements (v5.8)

Contributors must respect the integrity of the **SECURITY FAMILY 5.x** module:

- behavior-based identity must remain deterministic  
- FAMILY mode must remain safe and restricted  
- time-limits v3 must not be bypassable  
- **schoolwork must always be allowed**  
- stranger-mode must remain locked down  
- OWNER-level actions must remain protected  
- Identity Engine 3.1 must not be weakened  
- Schoolwork Engine 5.8 must remain intact  
- UI Automation Engine 5.1 must not perform unsafe actions  
- System Agent 5 must validate all system-level actions  
- ENVOY 5 must sanitize all system requests  
- COLNIK‑6.x must validate all KG mutations, workflow steps, and IPC payloads  
- AUTONOMY 6.x must remain safe in Control & Triage Mode  
- PanelAPI must maintain required user confirmation gates  
- TimeCore & Guard must oversee runtime stability  
- KG_EXPLAIN & KG_EXPLAIN_DEEP must remain transparent and correct  

Any PR affecting SECURITY FAMILY, SCHOOLWORK ENGINE, UI Automation Engine, ENVOY, System Agent, COLNIK, AUTONOMY, PanelAPI, TimeCore/Guard, or KG_EXPLAIN must include **explicit safety tests**.

---

# 11. 📄 License

All contributions are accepted only in accordance with the project’s **MIT License**.

---

# 📌 Document Status

Current version: **5.8 (Unified Orchestration, PanelAPI, TimeCore/Guard & COLNIK-AUTONOMY Architecture)**
