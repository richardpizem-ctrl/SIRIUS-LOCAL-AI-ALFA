# 🔐 SECURITY POLICY – SIRIUS LOCAL AI (v2.0.0)

This document defines the security rules, expectations, and responsibilities for users and contributors of **SIRIUS LOCAL AI**.  
The system interacts with Windows 11 APIs and must always operate in a safe, predictable, and controlled manner.

All processing is fully local; no data leaves the user’s PC.

---

# 1. 🛡 Security Principles

- **No operation may execute without explicit user confirmation.**  
- **No module may bypass safety checks.**  
- **No network communication is allowed anywhere in the system.**  
- **All filesystem operations must be validated and reversible when possible.**  
- **No hidden automation or background tasks.**  
- **No global mutable state.**  
- **All privileged actions must go through WIN‑CAP 2.0.**  
- **Plugins must follow strict capability boundaries.**

These principles ensure predictable, transparent, and safe behavior.

---

# 2. 🔒 Filesystem Safety Rules (FS‑AGENT 2.0)

- destructive actions (delete, overwrite) require double confirmation  
- protected directories must be blocked  
- invalid paths must be rejected  
- no recursive operations without explicit approval  
- no automatic cleanup or background deletion  
- rollback‑safe operations must be used whenever possible  

FS‑AGENT is the only module allowed to perform filesystem operations.

---

# 3. 🪟 Windows System Interaction Rules (WIN‑CAP 2.0)

All system‑level actions must:

- go through WIN‑CAP  
- validate permissions  
- avoid modifying system state without confirmation  
- avoid interacting with system‑critical processes  
- fail safely if access is denied  

WIN‑CAP must never:

- inject input  
- simulate keystrokes  
- modify registry keys  
- alter system configuration  
- perform privileged actions without explicit user approval  

---

# 4. 🔍 Input Validation (AITE 2.0)

All user inputs must be:

- validated  
- sanitized  
- classified by AITE  
- rejected if ambiguous or unsafe  

Unsupported input types must not be processed.

AITE ensures deterministic routing and prevents unsafe operations.

---

# 5. 🧪 Security Testing Requirements

Every release must include:

- filesystem safety tests  
- workflow validation tests  
- permission‑level tests  
- WIN‑CAP capability tests  
- plugin sandboxing tests  
- error‑state and fallback tests  

Security tests must be reproducible and manual.

---

# 6. 🧾 Reporting Security Issues

If you discover a security vulnerability:

- **Do NOT open a public Issue.**  
- Contact the maintainer privately at:  
  **richardpizem@gmail.com**

Include:

- description of the issue  
- reproduction steps  
- affected modules  
- expected vs. actual behavior  

You will receive a response within **72 hours**.

---

# 7. 🛠️ Self‑Repair & Health‑Check Layer (v4.0.0)

A future security‑critical module designed to maintain long‑term system stability.

### Responsibilities:
- integrity checks for core modules (runtime, context, commands, filesystem)  
- detection of corrupted states, missing files, invalid configs  
- safe automatic repairs (cache reset, index rebuild, default config restore)  
- patch suggestions for code‑level fixes (manual approval required)  
- strict protection against uncontrolled source‑code modifications  
- system‑wide health reporting to Runtime Core  

### Security Guarantees:
- no automatic modification of source code  
- no self‑rewriting behavior  
- all repairs must be reversible  
- all repairs must be logged  
- all high‑risk repairs require explicit user approval  

This layer will be implemented in **version 4.0.0**, after the system reaches full stability.

---

# 8. 📄 Supported Versions

Only the **latest stable release** receives security updates.

---

# 9. 📌 Document Status

Current version: **2.0.0 (Stable)**  
This policy will evolve as new modules and capabilities are introduced.
