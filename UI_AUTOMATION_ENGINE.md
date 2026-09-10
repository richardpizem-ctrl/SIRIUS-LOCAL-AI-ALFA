# 🎛 UI AUTOMATION ENGINE 5.1 — Deterministic, Explainable, Orchestrator-Supervised, COLNIK‑Validated OS Automation  
**Status:** ✔ Active  
**Version:** 5.1 (Updated for 5.8 UNIFIED)  
**Component:** UI Automation Engine  
**Role:** Safe, deterministic, explainable, orchestrator-supervised, autonomy‑aware automation of Windows 11 UI

---

## 🎯 Purpose  
UI Automation Engine 5.1 is responsible for executing deterministic, safe, explainable UI actions across Windows 11.  
It integrates identity validation, KG reasoning, central orchestration (`sirius_orchestrator.py`), interactive `PanelAPI` confirmation loops, temporal/security supervision via `TimeCore` and `Guard`, COLNIK‑6.x (Standard & IPC Mode) enterprise safety, AUTONOMY‑6.x (Control & Triage Mode) supervised gating, and System Intelligence Layer context awareness.

This engine allows SIRIUS to operate Windows 11 **precisely, safely, intelligently, and fully offline**.

---

## 🧩 Architecture Overview  
**Workflow Engine → `sirius_orchestrator.py` → UI Automation Engine → System Agent → COLNIK → AUTONOMY → PanelAPI → EXECUTE**

### Core Responsibilities  
- perform deterministic UI actions managed by `sirius_orchestrator.py`  
- resolve UI targets semantically  
- prevent mis‑clicks and unsafe automation  
- validate identity and permissions  
- integrate KG explainability  
- route decisions through COLNIK‑6.x (Standard & IPC Mode)  
- coordinate orchestrator and autonomy proposals (`PanelAPI` [ÁNO/NIE])  
- unify PC/Mobile automation logic  

### Key Files  
- `ui_automation/ui_engine.py`  
- `ui_automation/ui_targets.json`  
- `ui_automation/ui_fallback.json`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `IPC_DATA/ui_actions.json`  

---

## 🔍 Automation Pipeline  

### **1 — Target Resolution**  
UI Automation Engine resolves UI targets using:  
- Win32  
- UIA  
- WinRT  
- semantic KG metadata  
- fuzzy matching 5.8  
- identity‑aware filtering  

Targets are validated before any action is executed.

---

### **2 — Identity‑Aware Gating**  
Before automation begins, the engine checks:  
- FAMILY mode  
- STRANGER mode  
- SCHOOLWORK bypass (Schoolwork Engine 5.8)  
- ENVOY 5 permissions  
- identity‑restricted UI actions  

Unsafe identity contexts block automation.

---

### **3 — System‑Context Evaluation**  
The engine queries the System Intelligence Layer and `Guard`:  
- OS health  
- anomaly detection  
- risky UI states  
- repair‑aware context  
- PC/Mobile environment  

Automation is paused or denied during unstable states.

---

### **4 — KG‑Enhanced Explainability**  
Every UI action generates:  
- KG_EXPLAIN  
- KG_EXPLAIN_DEEP  
- semantic justification  
- multi‑hop reasoning  
- evidence metadata  

Explainability is mandatory for all UI operations.

---

### **5 — COLNIK‑Validated Routing (Standard & IPC Mode)**  
All UI actions are validated through COLNIK‑6.x:  
- enterprise‑grade safety  
- deterministic routing  
- reversible action checks  
- threat classification  
- explainability logs  

Unsafe UI actions are blocked automatically.

---

### **6 — AUTONOMY & PanelAPI-Aware Proposals**  
AUTONOMY‑6.x (Control & Triage Mode) and interactive `PanelAPI` (`[ÁNO/NIE]`) receive proposals for:  
- risky UI actions  
- identity‑restricted UI sequences  
- system‑context‑unsafe automation  
- multi‑step UI workflows  

AUTONOMY and human oversight confirm or deny transitions.

---

### **7 — Deterministic Execution**  
Once validated, UI actions are executed with:  
- mis‑click prevention 3.2  
- safe fallback logic  
- sandbox‑protected execution  
- reversible action guarantees  

Automation is always safe and predictable.

---

## 🧱 Capabilities  

### **Deterministic UI Automation**  
- click  
- type  
- navigate  
- open/close windows  
- interact with controls  
- multi‑step UI workflows under orchestrator control  

### **Semantic Targeting**  
- KG‑enhanced target resolution (`autosave_kg.json`)  
- fuzzy matching 5.8  
- identity‑aware filtering  
- safe fallback logic  

### **Explainability**  
- KG_EXPLAIN  
- KG_EXPLAIN_DEEP  
- multi‑hop reasoning  
- evidence trees  
- confidence scoring  

### **Safety & Validation**  
- COLNIK‑validated UI actions (Standard & IPC Mode)  
- AUTONOMY‑aware gating & PanelAPI oversight  
- System Agent threat blocking  
- reversible actions  

---

## 🔐 Safety Rules  
- ❌ No UI automation during unstable OS states  
- 🔒 Identity validation required  
- 🛡 COLNIK validation (Standard & IPC Mode) required  
- 🛡 AUTONOMY confirmation required  
- 💬 PanelAPI `[ÁNO/NIE]` gating active for high-risk UI interactions  
- ⚠ Explainability required  
- 🔁 Reversible actions enforced  
- 📉 Mis‑click prevention always active  

---

## 📊 Module Status  
- ✔ Fully implemented (Runtime 5.8)  
- ✔ Semantic targeting stable  
- ✔ Fuzzy matching improved  
- ✔ Orchestrator integration complete  
- ✔ PanelAPI confirmation gates active  
- ✔ TimeCore & Guard supervision active  
- ✔ COLNIK validation integrated (Standard & IPC Mode)  
- ✔ AUTONOMY gating active  
- ✔ Explainability functional  
- ✔ PC/Mobile automation unified  

---

## 🏁 Summary  
UI Automation Engine 5.1 is the deterministic, explainable, orchestrator-supervised, autonomy‑aware automation core of SIRIUS Local AI (v5.8).  
It performs safe, validated, reversible UI actions across Windows 11 using KG reasoning, identity enforcement, system‑context awareness, central orchestration, and enterprise‑grade COLNIK validation.

It enables SIRIUS to operate Windows 11 **intelligently, safely, predictively, and fully offline**.
