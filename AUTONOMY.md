# ⚡ AUTONOMY 6.x — Autonomous Decision Engine  
**Status:** ✔ Completed  
**Version:** 6.x  
**SIRIUS Local AI Version:** 5.8  
**Component:** AUTONOMY  
**Role:** Core autonomous reasoning, proposal‑generation, Control & Triage Mode engine

---

## 🎯 1. Purpose  
The AUTONOMY 6.x module is the central decision‑making engine of the SIRIUS Local AI system (v5.8).  
Its mission is to analyze system state, evaluate reasoning outputs, generate safe proposals, coordinate through Control & Triage Mode, and orchestrate the full autonomy cycle via the unified orchestrator (`sirius_orchestrator.py`) and PanelAPI.

AUTONOMY is responsible for producing deterministic, validated, and safe actions that flow into the IPC pipeline alongside COLNIK-6.x.

---

## 🧠 2. Architecture Overview  
**ReasoningEngine5 → AUTONOMY (Control & Triage Mode) → proposals.json → COLNIK (IPC Mode) → EXECUTE → responses.json → AUTONOMY**

### 🔍 Core Responsibilities  
- Interpret reasoning outputs  
- Generate structured proposals  
- Enforce safety, confirmation rules, and [ÁNO/NIE] loops via PanelAPI  
- Operate Control & Triage Mode for rapid anomaly containment  
- Maintain autonomy cycle timing with TimeCore & Guard supervision  
- Integrate responses from EXECUTE  
- Update internal state for next cycle

### 📁 Key Files  
- `AUTONOMY/autonomy.py`  
- `AUTONOMY/state_manager.py`  
- `AUTONOMY/triage_mode.py`  
- `IPC_DATA/proposals.json`  
- `IPC_DATA/responses.json`  

---

## 🔄 3. Operational Cycle  

### **Step 1 — Read System State**  
AUTONOMY collects data from ReasoningEngine5, TimeCore temporal monitors, Guard security checks, and internal state managers.

### **Step 2 — Analyze & Reason**  
- Evaluate current conditions  
- Detect required actions or trigger Triage Mode if anomalies occur  
- Apply rule‑based logic  
- Enforce deterministic decision paths via `sirius_orchestrator.py`  

### **Step 3 — Generate Proposals**  
AUTONOMY produces structured proposals and writes them to:  
`IPC_DATA/proposals.json`

Each proposal contains:  
- Action type  
- Target path  
- Safety level  
- Required confirmations (`PanelAPI` [ÁNO/NIE])  
- Execution metadata  

### **Step 4 — Wait for Execution**  
AUTONOMY enters a controlled wait state until COLNÍK (in Standard & IPC Mode) and EXECUTE finish processing.

### **Step 5 — Process Responses**  
AUTONOMY reads:  
`IPC_DATA/responses.json`  
and updates internal state based on execution results.

### **Step 6 — Cleanup & Next Cycle**  
AUTONOMY clears temporary buffers and begins the next autonomous cycle under Guard runtime supervision.

---

## 🔐 4. Safety Rules  

### **Critical Safety Guarantees**  
- 🔒 AUTONOMY never performs direct file operations  
- ⚠ Sensitive actions require explicit confirmation via PanelAPI [ÁNO/NIE] loops  
- 🧠 No dependency on Devin parser or NLP subsystems  
- ❌ No destructive actions without multi‑layer validation  
- 🔁 Duplicate detection before proposal generation  
- 🛡 Full isolation from EXECUTE logic  

These rules ensure that autonomy remains predictable, safe, and fully controlled.

---

## 📊 5. Module Status  
- ✔ Fully implemented  
- ✔ Production‑stable (Runtime 5.8)  
- ✔ Deterministic decision flow verified  
- ✔ Control & Triage Mode integrated  
- ✔ Proposal generation validated  
- ✔ COLNÍK IPC handshake verified  
- ✔ EXECUTE integration verified  
- ✔ PanelAPI [ÁNO/NIE] confirmation hooks active  
- ✔ Safe‑action enforcement confirmed  
- ✔ Clean cycle behavior confirmed  

---

## 📂 6. Related Files  
- `AUTONOMY/autonomy.py`  
- `AUTONOMY/state_manager.py`  
- `REASONING/engine5.py`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `IPC_DATA/proposals.json`  
- `IPC_DATA/responses.json`  

---

## 🏁 7. Summary  
AUTONOMY 6.x is the core decision engine of SIRIUS Local AI (v5.8).  
It generates safe, validated proposals, manages autonomous cycles (including Control & Triage Mode), and integrates tightly with COLNÍK, PanelAPI, and EXECUTE.  
Its deterministic logic ensures stable and predictable autonomous behavior across the entire SIRIUS 5.8 / 6.x framework.

This module is fully ready for production deployment.
