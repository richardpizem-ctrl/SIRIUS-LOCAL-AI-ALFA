# SIRIUS Kýklos Gate (COLNIK-6.x) – Primitive Decision Gate & IPC Tutorial

## 1. Overview

The **SIRIUS Kýklos Gate (COLNIK-6.x)** is the final, primitive decision gate in the SIRIUS runtime.  
Its purpose is extremely simple: **it decides whether a command or workflow step is ALLOWED or DENIED**, operating across both **Standard Mode** and high-performance **IPC Mode** for synchronization with AUTONOMY-6.x.

COLNIK does not perform reasoning, KG operations, workflow transformations, or autonomy logic.  
It is a single checkpoint placed directly above the autonomy and execution layers, managed via `sirius_orchestrator.py` and supervised by `TimeCore` and `Guard`.

COLNIK relies on existing security modules to make its decision.  
It does not replace them — it only uses their results alongside interactive `PanelAPI` human confirmation gates (`[ÁNO/NIE]`).

---

## 2. Why COLNIK Is Primitive

SIRIUS already contains multiple advanced security modules:

- **PermissionLayer5**  
- **PolicyEngine5**  
- **BehaviorFilter5**  
- **FamilySafetyRules5_x**  
- **ContextualBehaviorEngine5**  

These modules:

- know the rules  
- evaluate policies  
- filter unsafe behavior  
- enforce safety  
- analyze context  

COLNIK does **not** duplicate their work.  
Instead, COLNIK uses their outputs to make one final decision:

> **Should this command be allowed to reach autonomy and execution?**

This keeps the architecture clean and future-proof.

---

## 3. Execution Pipeline

This is the exact pipeline for Runtime 5.8:
User Command  
↓  
InputParser5  
↓  
`sirius_orchestrator.py` (Unified Orchestrator)  
↓  
WorkflowEngine5  
↓  
KÝKLOS GATE (COLNIK-6.x Standard & IPC Mode)  
↓  
PanelAPI (`[ÁNO/NIE]` Confirmation Loop)  
↓  
┌───────────────┐  
│    ALLOW      |  
│    or DENY    |  
└───────────────┘  
↓  
AUTONOMY 6.x (Control & Triage Mode)  
↓  
EXECUTE / OS

COLNIK is the **final inspection checkpoint** before any autonomous action is executed.

---

## 4. Security Modules Protecting COLNIK

COLNIK is primitive, but it is protected by **five core security modules** that already exist in SIRIUS:

### 4.1 PermissionLayer5
Checks whether the identity (user or agent) has the required permissions.  
Outputs: **ALLOW / DENY / REQUIRE-CONFIRMATION**

### 4.2 PolicyEngine5
Evaluates global and local policies from `policies_envoy.json`.  
Outputs: **ALLOWED-BY-POLICY / BLOCKED-BY-POLICY**

### 4.3 BehaviorFilter5
Filters unsafe or suspicious behavior patterns.  
Outputs: **SAFE / RISKY / BLOCK**

### 4.4 FamilySafetyRules5_x
Applies safety rules for sensitive operations (KG mutations, runtime changes).  
Outputs: **SAFE / UNSAFE**

### 4.5 ContextualBehaviorEngine5
Analyzes context, environment, and system state under `TimeCore` and `Guard` supervision.  
Outputs: **CONTEXT-OK / CONTEXT-NOT-OK**

---

## 5. How COLNIK Uses These Modules

COLNIK does not run complex logic.  
It simply collects the outputs of the modules above and performs a primitive evaluation:
IF PermissionLayer5 == ALLOW  
AND PolicyEngine5 == ALLOWED  
AND BehaviorFilter5 == SAFE  
AND FamilySafetyRules5_x == SAFE  
AND ContextualBehaviorEngine5 == CONTEXT-OK  
THEN  
ALLOW (with optional PanelAPI `[ÁNO/NIE]` check)  
ELSE  
DENY  

This is the entire decision mechanism.

---

## 6. What COLNIK Actually Does

COLNIK asks a small set of primitive questions:

### 6.1 Identity Check
Is the command truly coming from the user or a trusted agent?

### 6.2 Permission Check
Does the caller have the right to perform this action?

### 6.3 Policy Check
Does any global or local policy forbid this action?

### 6.4 Safety Check
Would executing this command harm the runtime or KG?

### 6.5 Confirmation Check
Does this command require explicit user confirmation via `PanelAPI` `[ÁNO/NIE]`?

### 6.6 Final Decision
- **ALLOW** → forward to autonomy / IPC buffer (`proposals.json`)  
- **DENY** → block, log, explain, or trigger Triage Mode  

---

## 7. COLNIK vs. Security Modules

| Component | Purpose |
|----------|---------|
| PermissionLayer5 | Knows what is allowed |
| PolicyEngine5 | Applies global/local policies |
| BehaviorFilter5 | Filters unsafe behavior |
| FamilySafetyRules5_x | Safety rules for sensitive operations |
| ContextualBehaviorEngine5 | Context-aware evaluation under TimeCore/Guard |
| **COLNIK-6.x** | **Final ALLOW/DENY decision (Standard & IPC Mode)** |

COLNIK is not a security layer — it is a **decision gate**.

---

## 8. Future Expansion (6.x → 8.x)

COLNIK will remain primitive, but new checks will be added:

- deeper policy evaluation  
- KG structural safety checks  
- agent-level permissions  
- external API safety  
- multi-user environment rules  
- autonomous agent restrictions  

The core ALLOW/DENY logic never changes.

---

## 9. Summary

- COLNIK-6.x is a **primitive decision gate**, not a complex module operating in Standard & IPC Mode.  
- It sits **above autonomy** and decides ALLOW/DENY under orchestrator supervision.  
- It uses existing security modules (PermissionLayer, PolicyEngine, BehaviorFilter…).  
- It integrates with interactive `PanelAPI` `[ÁNO/NIE]` user confirmation loops.  
- It ensures every command is safe before execution.  
- It keeps the SIRIUS runtime stable and future-proof.

This is the final, correct architecture of the Kýklos Gate for Runtime 5.8.
