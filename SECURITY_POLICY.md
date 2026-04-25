# 🔐 SECURITY POLICY – SIRIUS LOCAL AI ALFA

This document defines the security rules, expectations, and responsibilities for users and contributors of **SIRIUS LOCAL AI ALFA**.  
The system interacts with Windows 11 APIs and must always operate in a safe, predictable, and controlled manner.

---

# ⚠️ ALPHA WARNING

SIRIUS LOCAL AI ALFA is currently in **ALPHA**.  
Internal behavior, module boundaries, and system capabilities may change as development progresses.

Security‑related considerations:

- Windows Defender or SmartScreen may classify the runtime as an “Unknown App”.  
- Some operations may require elevated permissions (UAC).  
- Antivirus tools may produce false positives during development or packaging.  
- Accessibility and window‑control APIs may be restricted depending on system configuration.  
- All processing is fully local; **no data leaves the user’s PC**.  
- The author does not provide individual guidance for basic operations.

Users are encouraged to test features independently.

---

# 1. 🛡 Security Principles

- **No operation may execute without explicit user confirmation.**  
- **No module may bypass safety checks.**  
- **No network communication is allowed anywhere in the system.**  
- **All filesystem operations must be validated and reversible when possible.**  
- **No hidden automation or background tasks.**  
- **No global mutable state.**  
- **All privileged actions must go through WIN‑CAP.**

These principles ensure predictable, transparent, and safe behavior.

---

# 2. 🔒 Filesystem Safety Rules

- destructive actions (delete, overwrite) require double confirmation  
- protected directories must be blocked  
- invalid paths must be rejected  
- no recursive operations without explicit approval  
- no automatic cleanup or background deletion  

FS‑AGENT is the only module allowed to perform filesystem operations.

---

# 3. 🪟 Windows System Interaction Rules

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

---

# 4. 🔍 Input Validation

All user inputs must be:

- validated  
- sanitized  
- classified by AITE  
- rejected if ambiguous or unsafe  

Unsupported input types must not be processed.

---

# 5. 🧪 Security Testing Requirements

Every release must include:

- filesystem safety tests  
- workflow validation tests  
- permission‑level tests  
- WIN‑CAP capability tests  
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

Current version: **ALPHA**  
This policy will evolve as the system approaches v1.0.0.
