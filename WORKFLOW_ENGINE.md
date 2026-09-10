# 🔄 WORKFLOW ENGINE 5.8 — Deterministic, Explainable, Orchestrator-Supervised, System‑Aware Multi‑Step Logic  
**Status:** ✔ Active  
**Version:** 5.8  
**Component:** Workflow Engine  
**Role:** Safe, deterministic, orchestrator-supervised, autonomy‑aware multi‑step workflow execution for SIRIUS Local AI

---

## 🎯 Purpose  
Workflow Engine 5.8 is responsible for orchestrating multi‑step logic inside SIRIUS Local AI.  
It ensures that every workflow is executed safely, explainably, identity‑aware, system‑aware, and validated through central orchestration (`sirius_orchestrator.py`), interactive `PanelAPI` confirmation loops, temporal/security supervision via `TimeCore` and `Guard`, COLNIK‑6.x (Standard & IPC Mode), and AUTONOMY‑6.x (Control & Triage Mode).

This engine transforms high‑level tasks into deterministic sequences of actions, with full explainability and OS‑context awareness.

---

## 🧩 Architecture Overview  
**System Intelligence Layer → `sirius_orchestrator.py` → Workflow Engine → COLNIK → AUTONOMY → PanelAPI → EXECUTE → UI Automation Engine**

### Core Responsibilities  
- plan multi‑step workflows managed by `sirius_orchestrator.py`  
- validate workflow safety and execution bounds (`TimeCore`/`Guard`)  
- enforce identity rules  
- evaluate system context  
- integrate KG reasoning (`autosave_kg.json`)  
- generate explainability traces  
- coordinate orchestrator and autonomy proposals (`PanelAPI` [ÁNO/NIE])  
- route decisions through COLNIK‑6.x (Standard & IPC Mode)  
- execute deterministic fallback logic  

### Key Files  
- `workflow/workflow_engine.py`  
- `workflow/workflow_planner.py`  
- `workflow/workflow_state.json`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `IPC_DATA/workflow_proposals.json`  

---

## 🔍 Workflow Pipeline  

### **1 — Intent Detection**  
Workflow Engine receives a high‑level intent via `sirius_orchestrator.py` from:  
- AITE  
- AUTONOMY  
- UI PANEL (`PanelAPI`)  
- System Intelligence Layer  

Intent is classified and mapped to a workflow template.

---

### **2 — Identity‑Aware Gating**  
Before planning begins, the engine checks:  
- FAMILY mode  
- STRANGER mode  
- SCHOOLWORK bypass (Schoolwork Engine 5.8)  
- identity permissions  
- ENVOY 5 restrictions  

No workflow proceeds without identity validation.

---

### **3 — System‑Context Evaluation**  
Workflow Engine queries the System Intelligence Layer and `Guard`:  
- OS health  
- risky states  
- anomaly detection  
- repair‑aware context  
- PC/Mobile environment  

If the system is unstable, the workflow is paused or denied.

---

### **4 — KG‑Driven Planning**  
The engine uses the Knowledge Graph (`autosave_kg.json`) to:  
- resolve semantic targets  
- understand relationships  
- infer required steps  
- detect dependencies  
- generate explainability metadata  

KG_EXPLAIN and KG_EXPLAIN_DEEP are used for planning transparency.

---

### **5 — COLNIK‑Validated Routing (Standard & IPC Mode)**  
Every workflow transition is validated through COLNIK‑6.x:  
- allow/deny evaluation  
- enterprise‑grade safety  
- reversible action checks  
- threat detection  
- deterministic routing  

No unsafe transition is allowed.

---

### **6 — AUTONOMY & PanelAPI-Aware Proposals**  
AUTONOMY‑6.x (Control & Triage Mode) and interactive `PanelAPI` (`[ÁNO/NIE]`) receive workflow proposals:  
- confirms safe transitions  
- rejects unsafe ones  
- provides fallback logic  
- generates autonomy explanations  

Workflows never execute blindly.

---

### **7 — Deterministic Execution**  
Once validated, the workflow is executed through `sirius_orchestrator.py` via:  
- EXECUTE 6.x  
- UI Automation Engine 5.1  
- System Agent 5  

All actions are reversible, explainable, and logged under `TimeCore` monitoring.

---

## 🧱 Workflow Types  

### **Simple Workflows**  
- open application  
- navigate UI  
- fetch data  
- perform single-step tasks under orchestrator control  

### **Multi‑Step Workflows**  
- system maintenance  
- file operations  
- multi‑window automation  
- complex UI sequences  

### **Context‑Aware Workflows**  
- repair‑aware workflows  
- identity‑restricted workflows  
- system‑intelligent workflows  
- KG‑driven workflows (`autosave_kg.json`)  

---

## 🔐 Safety Rules  
- ❌ No workflow runs during unstable OS states  
- 🔒 Identity validation required  
- 🛡 COLNIK validation (Standard & IPC Mode) required  
- 🛡 AUTONOMY confirmation required  
- 💬 PanelAPI `[ÁNO/NIE]` gating active for high-impact multi-step sequences  
- ⚠ Explainability required  
- 🔁 Reversible actions enforced  
- 📉 Fallback logic always available  

---

## 📊 Module Status  
- ✔ Fully implemented (Runtime 5.8)  
- ✔ Identity‑aware gating functional  
- ✔ System‑context evaluation stable  
- ✔ KG‑driven planning verified  
- ✔ Orchestrator integration complete  
- ✔ PanelAPI confirmation gates active  
- ✔ TimeCore & Guard supervision active  
- ✔ COLNIK validation integrated (Standard & IPC Mode)  
- ✔ AUTONOMY gating active  
- ✔ Multi‑step workflows stable  
- ✔ Developer diagnostics available  

---

## 🏁 Summary  
Workflow Engine 5.8 is the central logic orchestrator of SIRIUS Local AI.  
It transforms high‑level intents into safe, deterministic, explainable workflows validated through identity, system context, KG reasoning, centralized orchestration, PanelAPI confirmation, COLNIK‑6.x, and AUTONOMY‑6.x.

It ensures that SIRIUS operates Windows 11 intelligently, safely, predictively, and fully explainably — across both PC and Mobile environments.
