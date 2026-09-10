# 🧩 KG COMFORT COMMANDS — Developer‑Friendly Knowledge Graph Operations  
**Status:** ✔ Active  
**Version:** 6.x (Updated for Runtime 5.8 UNIFIED)  
**Component:** KG Comfort Commands  
**Role:** Fast, safe, deterministic developer commands for manipulating the Knowledge Graph under orchestrator and PanelAPI supervision

---

## 🎯 Purpose  
KG Comfort Commands provide a **developer‑friendly interface** for interacting with the Knowledge Graph.  
They simplify entity creation, relation management, searching, renaming, exporting, importing, and debugging — all while maintaining:

- deterministic behavior via `sirius_orchestrator.py`  
- autosave/autoload integrity (`autosave_kg.json`)  
- COLNIK‑validated safety (Standard & IPC Mode)  
- AUTONOMY‑aware gating & Triage Mode  
- PanelAPI interactive `[ÁNO/NIE]` confirmation gates  
- full explainability (KG_EXPLAIN + KG_EXPLAIN_DEEP)  

These commands are designed for **rapid development**, **debugging**, and **manual KG manipulation** inside SIRIUS Local AI.

---

## 🧩 Architecture Overview  
**Developer Mode → KG Comfort Commands → `sirius_orchestrator.py` → KG ENGINE → ReasoningEngine5 → AUTONOMY → COLNIK → PanelAPI [ÁNO/NIE]**

### Core Responsibilities  
- simplify KG operations  
- provide safe developer shortcuts  
- maintain autosave/autoload consistency  
- generate explainability metadata  
- validate KG mutations  
- support debugging and testing  
- unify PC/Mobile KG manipulation  

### Key Files  
- `KG/kg_engine.py`  
- `KG/kg_store/`  
- `KG/autosave_kg.json`  
- `KG/kg_export.json`  
- `KG/kg_import.json`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  

---

## 🔍 Command Categories  

### **1 — Entity Commands**  
#### `kg add entity <NAME>`  
Creates a new entity with deterministic metadata via the orchestrator.

#### `kg rename entity <OLD> <NEW>`  
Renames an entity while preserving relations.

#### `kg delete entity <NAME>`  
Deletes an entity (requires AUTONOMY, COLNIK, and PanelAPI `[ÁNO/NIE]` approval).

#### `kg list entities`  
Shows all entities in the KG.

---

### **2 — Relation Commands**  
#### `kg add relation <A> <B> <TYPE>`  
Creates a relation between two entities.

#### `kg unset relation <A> <B>`  
Removes a relation safely.

#### `kg list relations`  
Displays all relations with metadata.

#### `kg explain <A> <B>`  
Runs KG_EXPLAIN.

#### `kg explain deep <A> <B>`  
Runs KG_EXPLAIN_DEEP (multi‑hop).

---

### **3 — Search Commands**  
#### `kg search <TERM>`  
Searches entities and relations.

#### `kg find related <ENTITY>`  
Shows all related entities.

#### `kg find path <A> <B>`  
Shows multi‑hop path between two nodes.

---

### **4 — Import/Export Commands**  
#### `kg export`  
Exports the entire KG to `kg_export.json`.

#### `kg import <FILE>`  
Imports a KG file (requires strict validation and confirmation).

#### `kg autosave on/off`  
Controls autosave behavior under TimeCore tracking.

---

### **5 — Debug Commands**  
#### `kg debug entity <NAME>`  
Shows full metadata for an entity.

#### `kg debug relation <A> <B>`  
Shows full metadata for a relation.

#### `kg debug stats`  
Shows KG size, depth, and consistency metrics verified by Guard.

---

## 🔐 Safety & Validation  

### **Identity Validation**  
All commands respect:  
- FAMILY mode  
- STRANGER mode  
- SCHOOLWORK bypass  
- ENVOY 5 restrictions  

### **Explainability Enforcement**  
Every KG mutation generates:  
- KG_EXPLAIN  
- KG_EXPLAIN_DEEP  
- mutation reasoning  
- evidence metadata  

### **COLNIK Validation**  
All KG mutations are validated through COLNIK‑6.x (Standard & IPC Mode):  
- enterprise‑grade safety  
- reversible mutation checks  
- deterministic routing  

### **AUTONOMY Gating & PanelAPI**  
AUTONOMY‑6.x (Control & Triage Mode) and `PanelAPI` confirm or deny:  
- risky mutations  
- relation deletions  
- entity deletions  
- import operations  

---

## 📊 Module Status  
- ✔ Fully implemented (Runtime 5.8)  
- ✔ Autosave/autoload stable  
- ✔ Mutation validation active  
- ✔ Orchestrator routing verified  
- ✔ PanelAPI [ÁNO/NIE] gates active  
- ✔ Explainability integrated  
- ✔ COLNIK validation functional (Standard & IPC Mode)  
- ✔ AUTONOMY gating active  
- ✔ PC/Mobile KG manipulation unified  

---

## 🏁 Summary  
KG Comfort Commands provide a **safe, deterministic, developer‑friendly interface** for manipulating the Knowledge Graph in SIRIUS Local AI (v5.8).  
They simplify entity creation, relation management, searching, debugging, and import/export — all while maintaining explainability, orchestrator execution, autonomy‑aware gating, PanelAPI human confirmation, and COLNIK‑validated safety.

They transform KG manipulation into a **fast, intuitive, professional developer workflow** inside SIRIUS Local AI.
