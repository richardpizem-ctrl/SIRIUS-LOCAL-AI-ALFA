# 🤝 Contributing Guidelines – SIRIUS LOCAL AI (v2.0.0)

Thank you for your interest in contributing to **SIRIUS LOCAL AI**.  
This document defines the rules, processes, and expectations for all contributors.  
The goal is to maintain a **clean, safe, modular, and predictable** local AI system built on the stable Runtime 2.0 architecture.

All processing is fully local.  
No data leaves your PC.

---

# 1. 🔐 Core Principles

- **Security has absolute priority**  
- **No action may bypass user confirmations**  
- **Modular architecture must remain clean and separated**  
- **All contributions must respect existing module APIs**  
- **No network operations or external data transmission**  
- **No hidden automation or background actions**  
- **Every change must preserve system transparency and predictability**  
- **No global mutable state**  
- **No circular imports**  
- **Deterministic, reversible behavior whenever possible**  
- **Plugin System 2.0 rules must be followed**  

---

# 2. 🚀 How to Start

1. **Fork** the repository  
2. **Create a new branch** for your change  
3. **Implement** the change according to the architecture  
4. **Test** it in your local environment  
5. **Submit a Pull Request** with a clear description  

Recommended branch naming:
feature/<name>
fix/<name>
refactor/<name>
docs/<name>
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
- imports grouped: standard → third‑party → internal  
- plugin code must follow Plugin API 2.0  

---

# 4. 🧪 Testing Requirements

Every change must include:

- basic functional tests  
- verification of security constraints  
- input validation  
- error‑state testing  
- predictable behavior under invalid inputs  
- no silent failures  
- no destructive operations without confirmation  
- no reliance on network access  

If your change affects:

- **FS‑AGENT** → test path validation, safety prompts  
- **NL Router 2.0** → test ambiguity handling and routing  
- **Workflow Engine 2.0** → test state transitions  
- **AI Loop 2.0** → test interval rule execution  
- **WIN‑CAP 2.0** → test safe fallback behavior  
- **Plugin System 2.0** → test manifest, NL commands, tasks, workflows, GUI elements  

---

# 5. 📥 Pull Request Rules

A valid PR must include:

- clear description of the change  
- explanation of why the change is needed  
- reference to related Issues (if applicable)  
- test results or manual test notes  

Restrictions:

- no large PRs — prefer smaller, well‑structured steps  
- PRs must **not** modify the architecture without prior discussion  
- PRs must follow module boundaries  
- PRs must not introduce new dependencies without approval  
- PRs must not break determinism or safety guarantees  
- plugin PRs must include updated manifest if needed  

---

# 6. ❌ What We Do Not Accept

- network‑based features  
- automatic actions without confirmation  
- bypassing security rules  
- monolithic modules  
- undocumented API changes  
- hidden background tasks  
- features that break modularity  
- unsafe filesystem or system operations  
- code that relies on OS‑specific hacks  
- contributions that reduce clarity or predictability  
- plugins that violate Plugin API 2.0  

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

- **ARCHITECTURE.md**  
- **MODULE_MAP.md**  
- **STYLEGUIDE.md**  
- **SECURITY.md**  
- **Plugin API 2.0**  

Breaking architectural boundaries requires prior approval.

---

# 9. 📝 Commit Message Style

Use clear, structured commit messages:

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
- imports grouped: standard → third‑party → internal  
- plugin code must follow Plugin API 2.0  

---

# 4. 🧪 Testing Requirements

Every change must include:

- basic functional tests  
- verification of security constraints  
- input validation  
- error‑state testing  
- predictable behavior under invalid inputs  
- no silent failures  
- no destructive operations without confirmation  
- no reliance on network access  

If your change affects:

- **FS‑AGENT** → test path validation, safety prompts  
- **NL Router 2.0** → test ambiguity handling and routing  
- **Workflow Engine 2.0** → test state transitions  
- **AI Loop 2.0** → test interval rule execution  
- **WIN‑CAP 2.0** → test safe fallback behavior  
- **Plugin System 2.0** → test manifest, NL commands, tasks, workflows, GUI elements  

---

# 5. 📥 Pull Request Rules

A valid PR must include:

- clear description of the change  
- explanation of why the change is needed  
- reference to related Issues (if applicable)  
- test results or manual test notes  

Restrictions:

- no large PRs — prefer smaller, well‑structured steps  
- PRs must **not** modify the architecture without prior discussion  
- PRs must follow module boundaries  
- PRs must not introduce new dependencies without approval  
- PRs must not break determinism or safety guarantees  
- plugin PRs must include updated manifest if needed  

---

# 6. ❌ What We Do Not Accept

- network‑based features  
- automatic actions without confirmation  
- bypassing security rules  
- monolithic modules  
- undocumented API changes  
- hidden background tasks  
- features that break modularity  
- unsafe filesystem or system operations  
- code that relies on OS‑specific hacks  
- contributions that reduce clarity or predictability  
- plugins that violate Plugin API 2.0  

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

- **ARCHITECTURE.md**  
- **MODULE_MAP.md**  
- **STYLEGUIDE.md**  
- **SECURITY.md**  
- **Plugin API 2.0**  

Breaking architectural boundaries requires prior approval.

---

# 9. 📝 Commit Message Style

Use clear, structured commit messages:
feat: added new workflow validation
fix: corrected path resolution in FS-AGENT
refactor: simplified NL routing logic
docs: updated INSTALLATION.md

Avoid vague messages like “update”, “fix stuff”, “changes”.

---

# 10. 📄 License

All contributions are accepted only in accordance with the project’s **MIT License**.

---

# 📌 Document Status

Current version: **2.0.0 (Stable)**  
This document will evolve as new modules and capabilities are introduced in v3.0.0 and v4.0.0.


