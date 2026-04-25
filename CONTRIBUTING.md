# 🤝 Contributing Guidelines – SIRIUS LOCAL AI ALFA

Thank you for your interest in contributing to **SIRIUS LOCAL AI ALFA**.  
This document defines the rules, processes, and expectations for all contributors.  
The goal is to maintain a **clean, safe, modular, and predictable** local AI system.

---

# ⚠️ ALPHA WARNING

SIRIUS LOCAL AI ALFA interacts directly with the Windows 11 environment, including filesystem operations, window management, application control, and system‑level APIs.  
The project is currently in **ALPHA**, and internal behavior may change as modules evolve.

- Windows Defender and SmartScreen may classify the runtime as an “Unknown App”.  
- Some actions may require elevated permissions (UAC).  
- The runtime must run with the same privilege level as the applications it controls.  
- Antivirus tools may produce false positives, especially when packaging Python code into executables.  
- Accessibility and window‑control APIs may be restricted depending on system configuration.

**Users are encouraged to test features independently.**  
This is an ALPHA‑stage developer tool — the author does not provide individual guidance for basic operations.

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

---

# 2. 🚀 How to Start

1. **Fork** the repository  
2. **Create a new branch** for your change  
3. **Implement** the change according to the architecture  
4. **Test** it in your local environment  
5. **Submit a Pull Request** with a clear description  

Recommended branch naming:

```
feature/<name>
fix/<name>
refactor/<name>
docs/<name>
```

---

# 3. 🧼 Code Style

All contributions must follow the project’s **STYLEGUIDE.md**.

Key rules:

- clean, readable, consistent  
- no magic constants  
- clear naming of functions and modules  
- comments only where necessary  
- comments explain **why**, not **what**  
- avoid unnecessary complexity  
- follow the architecture and module map  
- functions ideally 5–25 lines  
- no monolithic modules  
- no deep nesting — prefer early returns  
- imports grouped: standard → third‑party → internal  

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
- **CME** → test ambiguity handling and parameter extraction  
- **Workflow** → test state transitions  
- **WIN‑CAP** → test safe fallback behavior  

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

Breaking architectural boundaries requires prior approval.

---

# 9. 📝 Commit Message Style

Use clear, structured commit messages:

```
feat: added new workflow validation
fix: corrected path resolution in FS-AGENT
refactor: simplified command routing logic
docs: updated INSTALLATION.md
```

Avoid vague messages like “update”, “fix stuff”, “changes”.

---

# 10. 📄 License

All contributions are accepted only in accordance with the project’s **MIT License**.

---

# 📌 Document Status

Current version: **ALPHA**  
This document will evolve as the system approaches Phase 4 stability.
