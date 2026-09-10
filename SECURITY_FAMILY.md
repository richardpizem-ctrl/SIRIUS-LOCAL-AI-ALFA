# 🔐 SECURITY FAMILY 5.x — Identity Engine 3.1 & Unified Permission Framework  
**Status:** ✔ Active  
**Version:** 5.x (Updated for 5.8 UNIFIED)  
**Component:** Security Family  
**Role:** Identity enforcement, permission gating, safety modes, orchestrator-supervised, autonomy‑aware and COLNIK‑validated security logic

---

## 🎯 Purpose  
Security Family 5.x is the unified identity and permission enforcement layer of SIRIUS Local AI.  
It ensures that every workflow, automation request, KG mutation, reasoning step, and OS‑level action is validated through identity rules, explainability, orchestrator execution (`sirius_orchestrator.py`), interactive `PanelAPI` confirmation loops, `TimeCore`/`Guard` supervision, COLNIK‑6.x (Standard & IPC Mode), and AUTONOMY‑6.x (Control & Triage Mode).

Security Family protects the workstation from unsafe operations, unauthorized changes, and identity‑restricted actions.

---

## 🧩 Architecture Overview  
**Identity Engine → Security Family → `sirius_orchestrator.py` → System Agent → AUTONOMY → COLNIK → PanelAPI → EXECUTE**

### Core Responsibilities  
- enforce identity modes  
- validate permissions  
- block unauthorized actions  
- integrate explainability  
- provide orchestrator-supervised and autonomy‑aware gating  
- validate KG mutations  
- protect UI automation  
- unify PC/Mobile identity logic  

### Key Files  
- `security_family/security_family.py`  
- `security_family/identity_modes.json`  
- `security_family/permissions.json`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `IPC_DATA/security_events.json`  

---

## 🔍 Identity Modes  

### **FAMILY Mode**  
Full trusted mode.  
Allows safe workflows, UI automation, KG operations, and system actions under orchestrator supervision.

### **STRANGER Mode**  
Restricted mode.  
Blocks sensitive workflows, KG mutations, OS‑level actions, and UI automation.

### **SCHOOLWORK Mode (Bypass)**  
Special mode for school tasks (Schoolwork Engine 5.8).  
Allows safe KG operations and reasoning, blocks OS automation.

### **ENVOY 5 Permission Layer**  
Controls external fetch permissions and identity‑restricted operations.

---

## 🔍 Permission Pipeline  

### **1 — Identity Validation**  
Security Family checks:  
- user identity  
- active mode  
- permission level  
- ENVOY restrictions  
- SCHOOLWORK bypass  

If identity validation fails, the action is blocked.

---

### **2 — Explainability Enforcement**  
Every identity decision generates:  
- KG_EXPLAIN  
- KG_EXPLAIN_DEEP  
- identity reasoning  
- permission justification  
- autonomy reasoning  

Explainability is mandatory for all identity‑restricted operations.

---

### **3 — COLNIK‑Validated Security (Standard & IPC Mode)**  
All allow/deny decisions are validated through COLNIK‑6.x:  
- enterprise‑grade safety  
- deterministic routing  
- reversible action checks  
- threat classification  
- explainability logs  

Security Family never allows unsafe identity transitions.

---

### **4 — AUTONOMY & PanelAPI Gating**  
AUTONOMY‑6.x (Control & Triage Mode) and interactive `PanelAPI` receive proposals for:  
- identity‑restricted workflows  
- unsafe KG mutations  
- risky OS‑level actions  
- UI automation attempts  

AUTONOMY and human-in-the-loop prompts confirm or deny transitions.

---

### **5 — KG Mutation Protection**  
Security Family validates:  
- entity creation  
- relation creation  
- relation deletion  
- KG imports  
- KG exports  

Unsafe or identity‑restricted KG mutations are blocked.

---

### **6 — UI Automation Protection**  
Security Family blocks:  
- unverified UI actions  
- unsafe automation  
- identity‑restricted UI sequences  
- privilege‑escalation UI operations  

All UI actions require identity validation.

---

## 🧱 Protection Layers  

### **Identity Layer**  
- FAMILY / STRANGER / SCHOOLWORK modes  
- constant‑time identity validation  
- ENVOY 5 permission enforcement  

### **KG Layer**  
- KG mutation validation  
- KG explainability  
- multi‑hop identity reasoning  

### **Automation Layer**  
- UI automation gating  
- OS‑level action validation  
- reversible action enforcement  

### **Orchestrator & Autonomy Layer**  
- centralized execution (`sirius_orchestrator.py`)  
- supervised gating and `PanelAPI` human confirmation (`[ÁNO/NIE]`)  
- proposal/confirmation logic  
- fallback routing  

---

## 🔐 Safety Rules  
- ❌ No unsafe identity transitions  
- 🔒 COLNIK validation (Standard & IPC Mode) required  
- 🛡 AUTONOMY confirmation required  
- 💬 PanelAPI `[ÁNO/NIE]` gating active for sensitive identity shifts  
- ⚠ Explainability required  
- 🧠 KG‑aware identity reasoning  
- 🔁 Reversible actions enforced  
- 📉 Threat detection always active  

---

## 📊 Module Status  
- ✔ Fully implemented (Runtime 5.8)  
- ✔ Identity modes stable  
- ✔ Permission logic hardened  
- ✔ Orchestrator routing verified  
- ✔ PanelAPI confirmation gates active  
- ✔ TimeCore & Guard supervision active  
- ✔ KG mutation protection active  
- ✔ UI automation protection integrated  
- ✔ COLNIK validation functional (Standard & IPC Mode)  
- ✔ AUTONOMY gating active  
- ✔ PC/Mobile identity logic unified  

---

## 🏁 Summary  
Security Family 5.x is the unified identity and permission enforcement layer of SIRIUS Local AI (v5.8).  
It validates every workflow, KG mutation, reasoning step, and OS‑level action through identity rules, explainability, orchestrator supervision, PanelAPI confirmation, COLNIK‑6.x, and AUTONOMY‑6.x.

It ensures that SIRIUS operates Windows 11 **safely, intelligently, identity‑aware, autonomy‑aware, and fully explainably**.
