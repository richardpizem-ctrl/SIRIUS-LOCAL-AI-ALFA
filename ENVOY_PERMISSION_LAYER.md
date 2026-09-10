# 🌐 ENVOY PERMISSION LAYER 5 — Safe External Retrieval & Identity‑Aware Access Control  
**Status:** ✔ Active  
**Version:** 5.8  
**Component:** ENVOY Permission Layer  
**Role:** Identity‑aware, explainable, orchestrator-supervised, COLNIK-validated permission system for external retrieval tasks

---

## 🎯 Purpose  
The ENVOY Permission Layer 5 is the unified safety and permission framework that governs all external retrieval operations performed by ENVOY.  
It ensures that every outbound request is:

- identity‑validated  
- explainability‑aware  
- autonomy‑aware  
- orchestrator-supervised via `sirius_orchestrator.py` and `PanelAPI` [ÁNO/NIE] loops  
- COLNIK‑validated (Standard & IPC Mode)  
- safe, reversible, and compliant with offline‑first principles  

ENVOY never interacts with the local runtime directly — all communication is filtered through this permission layer under `TimeCore` and `Guard` supervision.

---

## 🧩 Architecture Overview  
**Security Family → ENVOY Permission Layer → `sirius_orchestrator.py` → ENVOY Client → Quarantine → Validator → Local AI**

### Core Responsibilities  
- validate external retrieval permissions  
- enforce identity modes  
- block unauthorized fetch attempts  
- generate explainability metadata  
- integrate KG reasoning  
- route decisions through COLNIK‑6.x (Standard & IPC Mode)  
- coordinate autonomy proposals and Triage Mode  
- protect the offline runtime  

### Key Files  
- `envoy/envoy_permission_layer.py`  
- `envoy/envoy_rules.json`  
- `envoy/envoy_log.json`  
- `IPC_DATA/envoy_events.json`  

---

## 🔍 Permission Pipeline  

### **1 — Identity Validation**  
Before ENVOY can fetch anything, the permission layer checks:  
- FAMILY mode  
- STRANGER mode  
- SCHOOLWORK bypass (v5.8)  
- ENVOY‑specific permissions  
- identity‑restricted topics  

If identity validation fails, the request is blocked.

---

### **2 — Explainability Enforcement**  
Every ENVOY request generates:  
- KG_EXPLAIN  
- KG_EXPLAIN_DEEP  
- identity reasoning  
- permission justification  
- autonomy reasoning  

Explainability is mandatory for all external retrieval operations.

---

### **3 — COLNIK‑Validated Routing**  
All outbound requests are validated through COLNIK‑6.x (Standard & IPC Mode):  
- enterprise‑grade safety  
- deterministic routing  
- reversible action checks  
- threat classification  
- explainability logs  

Unsafe or unverified requests are blocked.

---

### **4 — AUTONOMY‑Aware Gating**  
AUTONOMY‑6.x (Control & Triage Mode) receives proposals for:  
- risky external fetches  
- identity‑restricted topics  
- system‑context‑unsafe retrieval  
- KG mutation‑related fetches  

AUTONOMY confirms or denies transitions, backed by interactive `PanelAPI` [ÁNO/NIE] confirmation prompts.

---

### **5 — Quarantine Enforcement**  
All ENVOY data passes through a strict quarantine sandbox:  
- HTML removal  
- script removal  
- ad/tracker removal  
- unknown data type blocking  
- safe text normalization  

No raw external content ever reaches the local runtime.

---

### **6 — Validator & Policy Filter**  
After quarantine, the validator checks:  
- safety rules  
- restricted topics  
- medical/legal/financial risk  
- unverified claims  
- structural consistency  

Only clean, safe text is delivered to the local AI.

---

## 🧱 Permission Categories  

### **Allowed (Safe)**  
- educational content  
- definitions  
- basic troubleshooting  
- household information  
- schoolwork topics (Schoolwork Engine 5.8)  
- safe domain knowledge  

### **Restricted (Identity‑Aware)**  
- system‑level topics  
- sensitive personal data  
- privileged operations  
- identity‑restricted domains  

### **Blocked (Always)**  
- unsafe medical advice  
- legal instructions  
- financial instructions  
- harmful content  
- unverified claims  
- executable code  
- scripts, HTML, binary data  

---

## 🔐 Safety Rules  
- ❌ No external fetch without identity validation  
- 🔒 COLNIK validation (Standard & IPC Mode) required  
- 🛡 AUTONOMY confirmation required  
- 💬 PanelAPI [ÁNO/NIE] gating active for sensitive queries  
- ⚠ Explainability required  
- 🧠 Quarantine mandatory  
- 🔁 Reversible logic enforced  
- 📉 Threat detection always active  

---

## 📊 Module Status  
- ✔ Fully implemented (Runtime 5.8)  
- ✔ Identity enforcement stable  
- ✔ Quarantine functional  
- ✔ Validator hardened  
- ✔ COLNIK validation integrated (Standard & IPC Mode)  
- ✔ AUTONOMY gating active (Control & Triage Mode)  
- ✔ Orchestrator and PanelAPI hooks verified  
- ✔ TimeCore & Guard supervision active  
- ✔ Explainability traces operational  
- ✔ PC/Mobile integration complete  

---

## 🏁 Summary  
ENVOY Permission Layer 5 is the safety and permission backbone of all external retrieval operations in SIRIUS Local AI (v5.8).  
It ensures that ENVOY fetches only safe, identity‑validated, explainable, autonomy‑approved, and COLNIK‑verified content under orchestrator supervision and PanelAPI human-in-the-loop validation — all while maintaining strict offline‑first isolation.

It transforms ENVOY into a **secure, explainable, identity‑aware external retrieval agent** that protects the local AI from unsafe or unverified information.
