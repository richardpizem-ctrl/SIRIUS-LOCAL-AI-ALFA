# ⚡ PERFORMANCE GUIDE – SIRIUS LOCAL AI (v5.8 UNIFIED)

This document defines the performance model, optimization rules, and runtime guarantees of the  
**Unified Orchestration, PanelAPI, TimeCore/Guard & Enhanced COLNIK‑AUTONOMY Architecture 5.8**.

Version **5.8 UNIFIED** expands the original 5.7.0 rules with:

- **Unified Orchestrator (`sirius_orchestrator.py`) (constant-time execution pipeline)**  
- **PanelAPI & Interactive [ÁNO/NIE] Confirmation Loops (non-blocking gating)**  
- **TimeCore Temporal Tracking & Guard Security Supervision (lightweight runtime supervision)**  
- **AITE 5.8 (faster semantic + deep explainability multimodal triage)**  
- **Workflow Engine 5.8 (constant‑time transitions, COLNIK‑validated + AUTONOMY‑aware routing)**  
- **Reasoning Engine 5.8 (multi‑hop, inheritance, transitivity, rule chaining)**  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP (Explainability Engines)**  
- **Unified Knowledge Graph 5.8 + KG‑LIGHT (stabilized indexing via `autosave_kg.json`)**  
- **System Agent 5 (constant‑time identity + permission validation)**  
- **Security Family 5.x (Identity Engine 3.1, hardened checks)**  
- **Self‑Repair Layer 5.8 (bounded diagnostics, safe fallback)**  
- **System Intelligence Layer 5.8 (cached system context, deep explainability traces)**  
- **Mobile Runtime 5.8 (optimized mobile execution)**  
- **UI Automation Engine 5.1 (deterministic fallback, unified routing)**  
- **COLNIK‑6.x (enterprise validation, rule enforcement, workflow filtering — Standard & IPC Mode)**  
- **AUTONOMY 6.x (proposal/confirmation cycle & Triage Mode)**  

All processing is fully local; no data leaves the user's device.

---

# 1. Performance Philosophy

- predictable performance > raw speed  
- no hidden automation  
- no uncontrolled loops  
- no unnecessary background tasks  
- deterministic behavior across all modules  
- minimal overhead in all operations  
- plugin execution must follow strict performance rules  
- SCHOOLWORK workflows must remain instant  
- **Security Family 5.x must not introduce latency or blocking behavior**  
- identity checks must remain constant‑time  
- STRANGER‑mode restrictions must be lightweight  
- Self‑Repair Layer must run only in safe, controlled intervals  
- Reasoning Engine must remain bounded and deterministic  
- **System Agent 5 validation must be O(1)**  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP must generate explanations in bounded time**  
- **UI Automation Engine 5.1 must not block the runtime**  
- **System Intelligence Layer 5.8 must not perform deep scans during active workflows**  
- **COLNIK‑6.x validation (Standard & IPC Mode) must remain constant‑time**  
- **AUTONOMY 6.x proposal/confirmation & Triage Mode must remain bounded**  
- **Orchestrator, PanelAPI, and TimeCore/Guard overhead must remain < 2ms per cycle**  
- unified PC/Mobile performance must remain consistent  

---

# 2. Runtime Guarantees (Runtime 5.8)

- no race conditions  
- no parallel writes  
- no blocking operations without confirmation (`PanelAPI`)  
- no network calls  
- no unpredictable system modifications  
- event routing is O(1) via `sirius_orchestrator.py`  
- plugin loading is cached and isolated  
- AI Loop 5.x uses safe interval scheduling  
- SCHOOLWORK Engine must not delay routing  
- **identity checks remain O(1)**  
- **time‑limit checks remain O(1)**  
- Self‑Repair checks must be lightweight  
- semantic routing must remain constant‑time  
- **System Agent 5 must validate actions in constant time**  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP must produce deterministic, bounded explanations**  
- **UI Automation Engine 5.1 fallback logic must be bounded**  
- **System Intelligence Layer 5.8 must use cached system context**  
- **COLNIK‑6.x must validate workflow + KG operations in constant time**  
- **AUTONOMY 6.x must validate proposals/confirmations in constant time**  
- **TimeCore & Guard tracking must operate with zero thread blocking**  
- unified PC/Mobile execution must not introduce overhead  

---

# 3. Filesystem Performance (FS‑AGENT 5.8)

Rules:

- validate paths before performing operations  
- avoid scanning entire drives unless necessary  
- use cached context when possible  
- avoid repeated directory enumeration  
- ensure rollback‑safe operations  
- minimize disk I/O during workflows  
- SCHOOLWORK files must route instantly  
- **Security Family 5.x must not slow down FS‑AGENT operations**  
- identity‑restricted file operations must remain O(1)  
- semantic file classification must be lightweight  
- **System Agent 5 must not add overhead to FS operations**  
- **System Intelligence Layer 5.8 must not trigger deep scans during FS workflows**  
- **COLNIK‑6.x must validate FS operations without overhead**  
- unified PC/Mobile filesystem logic must remain fast  

---

# 4. WIN‑CAP Performance (WIN‑CAP 5.x)

- window operations must be atomic  
- app detection must be cached  
- audio device scanning must be minimal  
- system context must be lightweight  
- avoid repeated OS queries  
- capability wrappers must remain fast and predictable  
- SCHOOLWORK‑related system actions must bypass restrictions instantly  
- **identity‑restricted operations must not add overhead**  
- STRANGER‑mode checks must be constant‑time  
- automation operations must remain bounded  
- **UI Automation Engine 5.1 must use cached capability lookups**  
- **System Intelligence Layer 5.8 must avoid redundant system calls**  
- **COLNIK‑6.x must validate capability routing instantly**  
- unified PC/Mobile capability logic must remain consistent  

---

# 5. UI & PanelAPI Performance (GUI 5.8)

- no heavy rendering  
- animations must be lightweight and optional  
- confirmation dialogs (`PanelAPI` [ÁNO/NIE]) must appear instantly  
- avoid unnecessary redraws  
- UI components must remain modular and efficient  
- plugin‑driven UI elements must not block the main loop  
- SCHOOLWORK indicators must be instant  
- **FAMILY mode warnings must be non‑blocking and instant**  
- semantic UI hints must be pre‑computed  
- **UI Automation Engine 5.1 visual feedback must be O(1)**  
- explainability visualizer must be lightweight  
- unified PC/Mobile UI rendering must remain smooth  

---

# 6. Workflow & Orchestrator Performance (Workflow Engine 5.8)

- workflows must not recompute state  
- context memory must be minimal  
- transitions must be O(1) via `sirius_orchestrator.py`  
- plugin workflows must follow deterministic rules  
- no long‑running tasks inside workflows  
- avoid deep recursion or nested transitions  
- SCHOOLWORK workflows must bypass restrictions without overhead  
- **identity‑restricted workflows must remain lightweight**  
- semantic transitions must be cached  
- **System Agent 5 validation must not slow workflow transitions**  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP must generate workflow explanations in bounded time**  
- **System Intelligence Layer 5.8 must not interrupt workflow execution**  
- **COLNIK‑6.x must validate workflow steps instantly**  
- **AUTONOMY 6.x must validate proposals/confirmations instantly**  
- unified PC/Mobile workflows must remain consistent  

---

# 7. AI Loop Performance (AI Loop 5.x)

- interval tasks must be short  
- no blocking operations  
- no heavy computations  
- plugin heartbeat rules must be optimized  
- deterministic scheduling  
- safe error handling without retry loops  
- SCHOOLWORK tasks must not delay the loop  
- **time‑limit checks must be constant‑time**  
- Self‑Repair checks must run in low‑impact intervals  
- Reasoning Engine hooks must be bounded  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP must not run inside the AI Loop**  
- **UI Automation Engine 5.1 must not run inside the AI Loop**  
- **System Intelligence Layer 5.8 must run diagnostics only in low‑impact windows**  
- **COLNIK‑6.x must not run heavy validation inside the AI Loop**  
- **AUTONOMY 6.x must not run heavy proposals/confirmations inside the AI Loop**  
- unified PC/Mobile loop behavior must remain stable  

---

# 8. Reasoning Engine Performance (v5.8)

- reasoning depth must be capped  
- no unbounded chain‑of‑thought  
- symbolic rules must be pre‑indexed  
- pack‑aware reasoning must remain O(1) for lookup  
- no recursive rule expansion without limits  
- SCHOOLWORK reasoning must remain instant  
- identity‑restricted reasoning must not add overhead  
- **AITE 5.8 must pre‑compute semantic tags for faster reasoning**  
- **Reasoning Engine 5.8 must use cached pack indexes**  
- **KG_EXPLAIN_DEEP must generate deterministic proof + evidence trees**  
- **COLNIK‑6.x must validate reasoning steps instantly**  
- **AUTONOMY 6.x must validate reasoning proposals/confirmations instantly**  
- unified PC/Mobile reasoning must remain deterministic  

---

# 9. Logging Performance

- logs must be short and structured  
- no verbose debug output  
- no sensitive data  
- no timestamps unless needed  
- avoid logging inside tight loops  
- plugin logs must follow the same rules  
- SCHOOLWORK events must not log academic content  
- **Security Family 5.x must not log identity data or behavior patterns**  
- Self‑Repair logs must be minimal and safe  
- **UI Automation Engine 5.1 logs must be constant‑time**  
- **System Intelligence Layer 5.8 logs must avoid repeated system queries**  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP logs must remain bounded and deterministic**  
- **COLNIK‑6.x must not produce heavy logs**  
- **AUTONOMY 6.x must not produce heavy proposal/confirmation logs**  
- **TimeCore & Guard audit logs must be buffered and asynchronous**  

---

# 10. Plugin System Performance (Plugin System 5.x)

- plugin loading is cached  
- NL command detection is O(1)  
- workflows must be lightweight  
- GUI elements must not block runtime  
- AI tasks must be optimized  
- plugins must not introduce heavy operations  
- SCHOOLWORK‑aware plugins must remain instant  
- **plugins must not bypass or slow down Security Family 5.x checks**  
- reasoning hooks must be bounded  
- **System Agent 5 must validate plugin actions instantly**  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP must not be triggered unnecessarily**  
- **COLNIK‑6.x must validate plugin actions instantly**  
- **AUTONOMY 6.x must validate plugin proposals/confirmations instantly**  
- unified PC/Mobile plugin behavior must remain efficient  

---

# 11. Security Family Performance (v5.8)

### Identity Engine 3.1
- identity classification must be constant‑time  
- no heavy behavioral analysis  
- no background training loops  
- no scanning of large datasets  
- STRANGER detection must be instant  
- **System Agent 5 must enforce identity rules without overhead**  
- **COLNIK‑6.x must validate identity‑restricted actions instantly**  
- **AUTONOMY 6.x must validate identity‑aware proposals instantly**

### Time‑Limits Engine v3
- time checks must be O(1)  
- no timers running in tight loops  
- no blocking UI alerts  
- no repeated disk writes  
- FAMILY mode transitions must be instant  

### Schoolwork Engine 5.8
- schoolwork detection must be lightweight  
- no deep semantic loops  
- bypass logic must be instant  
- SCHOOLWORK workflows must never be delayed  

### Family Mode
- restrictions must not slow down NL routing  
- safe‑mode must not block runtime operations  
- warnings must be non‑blocking  
- OWNER‑level overrides must be instant  

---

# 12. Self‑Repair & Health‑Check Layer (v5.8)

- integrity checks must be lightweight  
- no deep scanning of source code  
- repairs must be safe and bounded  
- no blocking operations during runtime  
- patch suggestions must be pre‑computed  
- health reports must be instant  
- no repeated disk I/O  
- **System Agent 5 integrity must be checked in constant‑time**  
- **UI Automation Engine 5.1 modules must be validated without overhead**  
- **System Intelligence Layer 5.8 must avoid heavy diagnostics during workflows**  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP must not slow down repair logic**  
- **COLNIK‑6.x must validate repair actions instantly**  
- **AUTONOMY 6.x must validate repair proposals instantly**  
- unified PC/Mobile diagnostics must remain efficient  

---

# Document Status

**Version:** 5.8 UNIFIED  
Performance rules are fully aligned with the Unified Orchestration, PanelAPI, TimeCore/Guard & Enhanced COLNIK‑AUTONOMY Architecture 5.8 and prepared for future enhancements in v6.0.0.
