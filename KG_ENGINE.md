# 🧠 KG ENGINE 6.x — Knowledge Graph Core  
**Status:** ✔ Active  
**Version:** 6.x  
**SIRIUS Local AI Version:** 5.8  
**Component:** KG ENGINE  
**Role:** Unified symbolic knowledge graph engine powering explainability, relations, exports, imports, and multi-hop reasoning under orchestrator and PanelAPI supervision

---

## 🎯 Purpose  
The KG ENGINE 6.x module is the central symbolic knowledge system of SIRIUS Local AI (v5.8).  
It manages entities, relations, semantic structures, and graph-based reasoning operations.  
All explainability, relation discovery, and multi-hop inference rely on this engine.

KG ENGINE provides deterministic, transparent, and fully inspectable knowledge operations driven by `sirius_orchestrator.py` and guarded by `TimeCore` and `Guard`.

---

## 🧩 Architecture Overview  
**Runtime 5.8 → `sirius_orchestrator.py` → KG ENGINE → ReasoningEngine5 → AUTONOMY → COLNIK (IPC Mode) → PanelAPI [ÁNO/NIE] → EXECUTE**

### Core Responsibilities  
- Manage entities and relations  
- Provide semantic explainability (KG_EXPLAIN, KG_EXPLAIN_DEEP)  
- Perform relation discovery (KG_RELATE)  
- Handle graph import/export  
- Support multi-hop reasoning  
- Maintain deterministic symbolic structure (`autosave_kg.json`)  
- Provide comfort commands for developer workflow  

### Key Files  
- `KG/kg_engine.py`  
- `KG/kg_store/`  
- `KG/autosave_kg.json`  
- `KG/kg_export.json`  
- `KG/kg_import.json`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  

---

## 🧱 Knowledge Structure  

### **Entities**  
Fundamental nodes representing concepts, objects, categories, or abstract ideas.

### **Relations**  
Directed semantic links between entities, such as:  
- `A is B`  
- `A part_of B`  
- `A related_to B`  
- `A causes B`  

### **Metadata**  
Each relation stores:  
- confidence  
- novelty score  
- origin module  
- timestamps  
- multi-hop depth  

---

## 🔍 Core Operations  

### **KG_EXPLAIN**  
Provides a human-readable explanation of why two entities are connected.  
Shows direct relations and supporting metadata.

### **KG_EXPLAIN_DEEP**  
Generates multi-hop explanations across several layers of the graph.  
Used for deep symbolic reasoning and transparency.

### **KG_RELATE**  
Discovers semantic relations between two entities using:  
- direct edges  
- multi-hop paths  
- transitive inference  
- novelty scoring  

### **KG_EXPORT**  
Exports the entire knowledge graph into a portable JSON structure.

### **KG_IMPORT**  
Loads external or saved knowledge graphs into the engine under strict validation and `PanelAPI` confirmation.

### **Comfort Commands**  
Developer-friendly commands:  
- `kg add entity X`  
- `kg add relation A B`  
- `kg list entities`  
- `kg list relations`  
- `kg search X`  
- `kg rename entity`  
- `kg unset relation`  

---

## 🔄 Operational Cycle  

### **1 — Load KG**  
KG ENGINE loads the current graph from:  
`KG/kg_store/`  
or  
`autosave_kg.json`

### **2 — Process Operation**  
Depending on the request routed via `sirius_orchestrator.py`:  
- add entity  
- add relation  
- explain  
- relate  
- export  
- import  

### **3 — Update Graph**  
All changes are deterministic and validated through COLNIK-6.x and Guard.  
Autosave is triggered after each modification.

### **4 — Provide Output**  
Results are returned to:  
- ReasoningEngine5  
- AUTONOMY (Control & Triage Mode)  
- Developer Mode (`PanelAPI` / UI PANEL)

---

## 🔐 Safety Rules  
- ❌ No destructive graph operations without explicit confirmation (`PanelAPI` [ÁNO/NIE])  
- 🔒 Autosave (`autosave_kg.json`) ensures graph integrity  
- 🧠 Deterministic relation evaluation  
- ⚠ Multi-hop depth capped to prevent runaway inference  
- 🛡 No modification of autonomy logic  

---

## 📊 Module Status  
- ✔ Fully implemented (Runtime 5.8)  
- ✔ Multi-hop reasoning verified  
- ✔ Explainability layers functional  
- ✔ Orchestrator integration complete  
- ✔ PanelAPI confirmation gates active  
- ✔ Import/export stable  
- ✔ Autosave/autoload operational  
- ✔ Developer comfort commands active  

---

## 🏁 Summary  
KG ENGINE 6.x is the symbolic core of SIRIUS Local AI (v5.8).  
It manages entities, relations, explainability, and multi-hop reasoning with deterministic precision.  
The engine is fully integrated with Runtime 5.8, `sirius_orchestrator.py`, ReasoningEngine5, AUTONOMY, COLNIK, and PanelAPI, forming the foundation of SIRIUS’s transparent and enterprise-ready knowledge system.
