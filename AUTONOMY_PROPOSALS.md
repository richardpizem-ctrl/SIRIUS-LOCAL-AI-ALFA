# 🤖 AUTONOMY PROPOSALS 6.x — Supervised Autonomous Decision Generation  
**Status:** ✔ Active  
**Version:** 6.x (Updated for Runtime 5.8 UNIFIED)  
**Component:** AUTONOMY Proposal Engine  
**Role:** Generate safe, explainable, supervised autonomous proposals for system actions, workflows, KG mutations, and UI automation under orchestrator and PanelAPI supervision

---

## 🎯 Purpose  
The AUTONOMY Proposal Engine 6.x is responsible for generating **autonomous suggestions** (proposals) based on system context, KG reasoning, identity rules, predictive intelligence, and Triage Mode diagnostics.  
These proposals represent *what SIRIUS thinks should happen next* — but every proposal is supervised, validated, and confirmed through COLNIK‑6.x (Standard & IPC Mode), System Agent 5, and interactive PanelAPI loops with [ÁNO/NIE] confirmations.

AUTONOMY never executes actions directly.  
It **proposes**, **explains**, **justifies**, and **waits for validation**.

---

## 🧩 Architecture Overview  
**System Intelligence Layer → AUTONOMY Proposal Engine → `sirius_orchestrator.py` → COLNIK (IPC Mode) → PanelAPI [ÁNO/NIE] → Workflow Engine → EXECUTE**

### Core Responsibilities  
- generate autonomous proposals  
- evaluate system context via TimeCore & Guard  
- integrate KG reasoning  
- classify proposal types  
- provide explainability metadata  
- route proposals through COLNIK‑6.x (Standard & IPC Mode)  
- coordinate supervised autonomy via Control & Triage Mode  
- unify PC/Mobile autonomy logic  

### Key Files  
- `autonomy/autonomy_proposer.py`  
- `autonomy/proposals.json`  
- `autonomy/proposal_metadata.json`  
- `IPC_DATA/autonomy_events.json`  

---

## 🔍 Proposal Pipeline  

### **1 — Context Collection**  
AUTONOMY gathers signals from:  
- System Intelligence Layer  
- KG ENGINE  
- ReasoningEngine5  
- Workflow Engine  
- System Agent  
- Identity Engine  
- TimeCore & Guard Temporal/Security Monitors  

Context determines whether a proposal is safe, relevant, or necessary.

---

### **2 — Proposal Generation**  
AUTONOMY generates proposals in several categories:

#### **System Proposals**
- optimize CPU/RAM  
- clean disk  
- close heavy processes  
- stabilize OS state  
- repair‑aware suggestions  

#### **Workflow Proposals**
- continue workflow  
- pause workflow  
- reroute workflow  
- fallback workflow  
- safe-mode workflow  

#### **UI Automation Proposals**
- open settings  
- navigate control panels  
- perform safe UI actions  
- block unsafe UI sequences  

#### **KG Proposals**
- add relation  
- remove relation  
- rename entity  
- validate KG consistency  

#### **Identity Proposals**
- restrict action  
- allow safe action  
- require confirmation (`PanelAPI` [ÁNO/NIE])  
- enforce FAMILY/STRANGER mode  

---

### **3 — Explainability Generation**  
Every proposal includes:

- KG_EXPLAIN  
- KG_EXPLAIN_DEEP  
- multi-hop reasoning  
- evidence metadata  
- confidence score  
- justification text  

Explainability is mandatory for all proposals.

---

### **4 — COLNIK‑Validated Routing**  
Before a proposal is accepted, COLNIK‑6.x (Standard & IPC Mode) performs:

- enterprise-grade safety validation  
- deterministic allow/deny routing  
- reversible action checks  
- threat classification  
- identity enforcement  
- explainability verification  

Unsafe proposals are rejected automatically.

---

### **5 — System Agent Enforcement**  
System Agent 5 checks:

- identity mode  
- permission level  
- OS stability  
- threat conditions  
- UI safety  
- repair‑aware context  

If any condition fails, the proposal is blocked.

---

### **6 — Proposal Confirmation**  
AUTONOMY never executes actions.  
It waits for:

- COLNIK approval  
- System Agent approval  
- Workflow Engine acceptance  
- Explicit user confirmation via PanelAPI [ÁNO/NIE] loops  

Only then is the proposal converted into an executable action.

---

## 🧱 Proposal Types  

### **1 — ALLOW Proposal**  
Safe, validated, explainable.  
Action can proceed.

### **2 — DENY Proposal**  
Unsafe, identity‑restricted, or system‑restricted.  
Action is blocked.

### **3 — REQUIRE_CONFIRMATION Proposal**  
Action is potentially risky.  
Requires supervised approval via PanelAPI [ÁNO/NIE].

### **4 — FALLBACK Proposal**  
Suggests a safer alternative.  
Used during unstable OS states or Triage Mode triggers.

### **5 — REPAIR Proposal**  
Triggers Self‑Repair Layer 5.8.  
Used when corruption or instability is detected.

---

## 🔐 Safety Rules  
- ❌ AUTONOMY never executes actions directly  
- 🔒 COLNIK validation required  
- 🛡 System Agent enforcement required  
- ⚠ Explainability required  
- 🧠 Identity‑aware proposal logic  
- 🔁 Reversible actions enforced  
- 📉 Unsafe proposals automatically rejected  

---

## 📊 Module Status  
- ✔ Fully implemented (Runtime 5.8)  
- ✔ Proposal generation stable  
- ✔ Explainability integrated  
- ✔ COLNIK validation functional (Standard & IPC Mode)  
- ✔ System Agent gating active  
- ✔ Control & Triage Mode operational  
- ✔ PanelAPI [ÁNO/NIE] confirmation hooks active  
- ✔ Workflow integration complete  
- ✔ PC/Mobile autonomy unified  

---

## 🏁 Summary  
AUTONOMY Proposal Engine 6.x is the supervised autonomous decision generator of SIRIUS Local AI (v5.8).  
It creates safe, explainable, identity‑aware, system‑aware proposals for workflows, UI automation, KG operations, and system actions — all orchestrated via `sirius_orchestrator.py`, validated through COLNIK‑6.x, monitored by TimeCore & Guard, and confirmed via interactive PanelAPI loops.

It transforms SIRIUS into a **predictive, intelligent, supervised autonomous workstation** that never acts blindly and always explains its reasoning.
