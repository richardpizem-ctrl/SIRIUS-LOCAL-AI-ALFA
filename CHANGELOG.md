# 📜 CHANGELOG — SIRIUS LOCAL AI

## v5.8 — Unified Orchestrator + PanelAPI Loops + TimeCore & Guard Supervision + COLNIK/AUTONOMY IPC (2026‑09‑10)

### 🔥 Major Update
Version 5.8 delivers the **fully unified and orchestrated architecture** of the SIRIUS Runtime line.  
This release transitions execution from legacy CLI routing to the unified orchestrator (`sirius_orchestrator.py`), introduces interactive `PanelAPI` loops with [ÁNO/NIE] confirmations, integrates `TimeCore` temporal tracking and `Guard` security supervision, and elevates `COLNIK-6.x` (Standard & IPC Mode) alongside `AUTONOMY-6.x` (Control & Triage Mode) to full production readiness.

It completes the foundation established in 5.7.0 and establishes an uncompromised, interactive, and self-supervised local AI workstation environment.

---

### 🚀 Unified Orchestrator (`sirius_orchestrator.py`)
- centralized execution pipeline replacing scattered script entry points
- deterministic orchestration from input parsing to OS execution
- unified workflow context sharing across all subsystems
- robust error propagation and recovery routing

---

### 💬 PanelAPI & Interactive Loops
- interactive CLI/UI loops with [ÁNO/NIE] confirmation prompts
- real-time session state rendering
- structured user gating for sensitive or destructive operations
- seamless bridge between autonomous proposals and human-in-the-loop decisions

---

### ⏱ TimeCore & Guard Supervision
- TimeCore temporal tracking for precise execution timing and timeout management
- Guard runtime supervision and anomaly detection
- automated safety locks during erratic system behavior
- real-time telemetry logging for auditability

---

### 🛡 COLNIK‑6.x Validation Layer (Standard & IPC Mode)
- customs-style inspection of KG operations and workflow steps  
- high-performance IPC synchronization with AUTONOMY  
- reasoning safety checks and anomaly detection  
- malformed KG mutation protection  
- enterprise-grade consistency enforcement  
- integration with ENVOY Permission Layer  

COLNIK‑6.x operates across both Standard and high-speed IPC modes as the core security gatekeeper.

---

### 🤖 AUTONOMY 6.x (Control & Triage Mode)
- advanced proposal generation and confirmation logic  
- Triage Mode for rapid anomaly containment and automated mitigation  
- IPC synchronization with COLNIK  
- safe autonomous execution under Guard supervision  
- explainability-aware autonomy routing  

---

### 🧠 Unified Knowledge Graph & Reasoning Engine (v5.8)
- deterministic KG Core (cycle‑safe) with unified autosave (`autosave_kg.json`)
- multi-hop traversal and inbound/outbound reasoning context
- hierarchical proof trees and evidence trees (XAI)
- stabilized rule execution pipeline (MultiHopOrbitInference, DedicsnostVlastnosti, TranzitivneRelacie, AutoTypeInference)

---

### 🔁 WorkflowEngine5 (v5.8)
- integrated with `sirius_orchestrator.py`
- deterministic multi-stage workflows with KG_EXPLAIN_DEEP routing
- complete step registry spanning KG, Reasoning, ENVOY, COLNIK, AUTONOMY, PanelAPI, and OS actions

---

### ⚙ CLI Update (IMPORTANT)
SIRIUS Runtime 5.8 is launched via the unified orchestrator:

python sirius_orchestrator.py

---

### 🧹 Stability Improvements
- Runtime line stabilized at **100%**
- Orchestrator and PanelAPI loops fully verified
- TimeCore & Guard supervision active
- COLNIK‑6.x (Standard & IPC Mode) and AUTONOMY-6.x (Control & Triage Mode) fully synchronized

---

### 📦 Included in ZIP (SIRIUS-LOCAL-AI-5.8.zip)
- full Runtime 5.8 core and modules
- `sirius_orchestrator.py`
- `PanelAPI` module with [ÁNO/NIE] confirmation loops
- `TimeCore` and `Guard` supervision components
- updated KG modules, reasoning rules, and WorkflowEngine5
- ENVOY Permission Layer, Normalizer, Execution Layer, Quarantine
- COLNIK‑6.x validation subsystem (Standard & IPC Mode)
- AUTONOMY 6.x (Control & Triage Mode)
- Self‑Repair Layer 5.8
- autosave_kg.json (Unified Schema snapshot)

---

## v5.7.0 — Unified Logic Layer + Stabilized KG Platform + COLNIK‑AUTONOMY Integration  
(Previous version)

## v5.6.2 — Stabilized Logic Layer + Unified KG Platform  
(Previous version)

## v5.5.0 — Unified Reasoning & Explainability Architecture  
(Previous version)

## v5.0.0 — Unified Offline Reasoning Runtime  
(Previous version)

## v4.5.0 PRO — System Intelligence Expansion  
(Previous version)
