# 🔧 SELF‑REPAIR LAYER 5.8 — Autonomous Integrity, Recovery & Runtime Stabilization  
**Status:** ✔ Active  
**Version:** 5.8 (Updated for 5.8 UNIFIED)  
**Component:** Self‑Repair Layer  
**Role:** Automatic detection, stabilization, recovery, and repair of runtime components, configs, KG, workflows, and system context under orchestrator supervision

---

## 🎯 Purpose  
The Self‑Repair Layer 5.8 is responsible for maintaining the stability, integrity, and reliability of SIRIUS Local AI.  
It detects corruption, missing modules, unstable states, broken configs, KG inconsistencies, and runtime anomalies — then repairs them automatically or routes them through `sirius_orchestrator.py`, interactive `PanelAPI` confirmation loops, `TimeCore`/`Guard` supervision, and AUTONOMY‑6.x for supervised recovery.

Self‑Repair ensures that SIRIUS remains **stable, deterministic, safe, and fully operational**, even under failure conditions.

---

## 🧩 Architecture Overview  
**System Intelligence Layer → Self‑Repair Layer → `sirius_orchestrator.py` → System Agent → AUTONOMY → COLNIK → PanelAPI → Runtime 5.8**

### Core Responsibilities  
- detect corrupted or missing files  
- validate runtime integrity  
- repair configs and JSON stores  
- stabilize KG operations (`autosave_kg.json`)  
- recover workflow states  
- enforce safe fallback logic  
- integrate explainability  
- coordinate orchestrator-supervised and autonomy‑aware recovery  
- protect the offline runtime  

### Key Files  
- `self_repair/self_repair_engine.py`  
- `self_repair/integrity_map.json`  
- `self_repair/baseline_runtime4/`  
- `self_repair/repair_log.json`  
- `autosave_kg.json`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  

---

## 🔍 Repair Pipeline  

### **1 — Integrity Scan**  
Self‑Repair performs periodic scans managed under `TimeCore` temporal bounds:  
- file existence  
- file size  
- file format  
- module presence  
- config validity  
- KG consistency  
- workflow state integrity  

If any anomaly is detected, repair mode is triggered.

---

### **2 — System‑Context Validation**  
Self‑Repair queries the System Intelligence Layer and `Guard`:  
- OS health  
- anomaly detection  
- risky states  
- repair‑required conditions  
- PC/Mobile environment  

Repairs are paused during unsafe system states.

---

### **3 — Baseline Comparison**  
Self‑Repair compares runtime files with the baseline:  
- baseline_runtime4  
- integrity_map.json  
- module signatures  
- config templates  

Missing or corrupted files are restored automatically.

---

### **4 — KG Stabilization**  
Self‑Repair validates the Knowledge Graph:  
- entity consistency  
- relation consistency  
- autosave integrity (`autosave_kg.json`)  
- import/export structure  
- multi‑hop stability  

If KG is corrupted, Self‑Repair restores `autosave_kg.json`.

---

### **5 — Workflow Recovery**  
Self‑Repair restores:  
- workflow states  
- pending transitions  
- safe fallback logic  
- autonomy‑aware recovery paths  

Broken workflows are repaired without losing context.

---

### **6 — COLNIK‑Validated Repair (Standard & IPC Mode)**  
All repair actions are validated through COLNIK‑6.x:  
- enterprise‑grade safety  
- deterministic routing  
- reversible repair logic  
- threat classification  
- explainability logs  

Unsafe repairs are blocked.

---

### **7 — AUTONOMY & PanelAPI-Aware Repair Proposals**  
AUTONOMY‑6.x (Control & Triage Mode) and interactive `PanelAPI` `[ÁNO/NIE]` receive proposals for:  
- risky repairs  
- identity‑restricted repairs  
- KG‑related repairs  
- workflow recovery  
- system‑context‑dependent repairs  

AUTONOMY confirms or denies transitions, backed by human oversight.

---

## 🧱 Repair Capabilities  

### **Automatic Repairs**  
- missing files  
- corrupted configs  
- broken JSON stores  
- KG autosave restoration  
- workflow state recovery  
- module re‑initialization  

### **Stabilization**  
- degraded‑mode fallback  
- safe‑mode isolation  
- sandboxed repair execution  
- reversible repair logic  

### **Explainability**  
- KG_EXPLAIN  
- KG_EXPLAIN_DEEP  
- repair reasoning  
- evidence metadata  
- confidence scoring  

---

## 🔐 Safety Rules  
- ❌ No repairs during unstable OS states  
- 🔒 COLNIK validation (Standard & IPC Mode) required  
- 🛡 AUTONOMY confirmation required  
- 💬 PanelAPI `[ÁNO/NIE]` gating active for sensitive structural restorations  
- ⚠ Explainability required  
- 🧠 Identity‑aware repair logic  
- 🔁 Reversible repairs enforced  
- 📉 Threat detection always active  

---

## 📊 Module Status  
- ✔ Fully implemented (Runtime 5.8)  
- ✔ Integrity scans stable  
- ✔ KG stabilization active  
- ✔ Workflow recovery functional  
- ✔ Orchestrator integration complete  
- ✔ PanelAPI confirmation gates active  
- ✔ TimeCore & Guard supervision active  
- ✔ COLNIK validation integrated (Standard & IPC Mode)  
- ✔ AUTONOMY gating active  
- ✔ Explainability traces operational  
- ✔ PC/Mobile repair logic unified  

---

## 🏁 Summary  
Self‑Repair Layer 5.8 is the autonomous stabilization and recovery core of SIRIUS Local AI.  
It detects corruption, repairs modules, restores configs, stabilizes the KG, recovers workflows, and ensures that every repair is safe, explainable, orchestrator-supervised, autonomy‑aware, and COLNIK‑validated.

It transforms SIRIUS into a **self‑healing, stable, deterministic, offline‑intelligent workstation** capable of maintaining reliability under any failure condition.
