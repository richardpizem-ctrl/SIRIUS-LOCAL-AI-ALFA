# 🎛 UI PANEL 6.x — Futuristic Neon Interface (VO VÝVOJI)  
**Status:** ⚠️ Vo vývoji (Active Development)  
**Version:** 6.x  
**SIRIUS Local AI Version:** 5.8  
**Component:** UI PANEL  
**Role:** Unified visual interface for user and developer interaction with SIRIUS Local AI under orchestrator and PanelAPI supervision

---

## 🎯 Purpose  
UI PANEL 6.x module provides a futuristic, neon‑styled interface for interacting with the SIRIUS Local AI system.  
It serves as the primary visual layer for both **User Mode** and **Developer Mode**, enabling clear workflow navigation, module monitoring, interactive human-in-the-loop confirmation loops (`PanelAPI` [ÁNO/NIE]), and command execution.

*Upozornenie:* Tento modul je aktuálne **vo vývoji** (active development) a priebežne sa prispôsobuje centralizovanej architektúre orchestrátora (`sirius_orchestrator.py`), časovému a bezpečnostnému dohľadu (`TimeCore`/`Guard`) a pokročilým módom COLNIK-6.x a AUTONOMY-6.x.

---

## 🧩 Architecture Overview  
**UI PANEL → `sirius_orchestrator.py` → PanelAPI → Runtime 5.8 → Autonomy 6.x → COLNIK (IPC Mode) → EXECUTE → KG Engine → Reasoning Engine**

### Core Responsibilities  
- Display system state and diagnostics (integrated with `TimeCore` and `Guard`)  
- Provide input/output fields for interaction and interactive `PanelAPI` prompts (`[ÁNO/NIE]`)  
- Visualize autonomy workflow and orchestrator state  
- Switch between User and Developer modes  
- Show module activity (COLNIK, EXECUTE, KG, Reasoning, Orchestrator)  
- Provide neon‑styled futuristic interface elements  

### Key Files  
- `UI/ui_panel.html`  
- `UI/ui_panel.css`  
- `UI/ui_panel.js`  
- `PANEL_API/panel_api.py`  
- `ASSETS/neon_theme/`  

---

## 🖥 Interface Layout  

### **Top Section — Output Display**  
Large high‑contrast neon panel showing:  
- AI responses  
- Diagnostics  
- Workflow steps  
- Module logs  
- Autonomy cycle status  
- Orchestrator telemetry & `PanelAPI` confirmation prompts (`[ÁNO/NIE]`)  

### **Bottom Section — Input Field**  
Compact neon input bar for:  
- Commands  
- Queries  
- Developer instructions  
- KG operations  
- Runtime controls  

### **Side Panel — Module Status**  
Real‑time indicators for:  
- Unified Orchestrator (`sirius_orchestrator.py`)  
- PanelAPI & TimeCore/Guard  
- AUTONOMY 6.x (Control & Triage Mode)  
- COLNIK 6.x (Standard & IPC Mode)  
- EXECUTE 6.x  
- KG Engine (`autosave_kg.json`)  
- Reasoning Engine  
- System health  

---

## 🔀 Modes  

### **User Mode**  
- Simplified interface  
- Clean neon layout  
- Basic commands  
- High‑level system overview  
- Safe operations with interactive `PanelAPI` safety gates  

### **Developer Mode**  
- Full diagnostics and orchestrator tracing  
- Module logs and `TimeCore`/`Guard` telemetry  
- KG tools  
- Autonomy debugging  
- File operations (safe)  
- Advanced workflow visualization  

---

## 🎨 Design Principles  
- Futuristic neon aesthetic  
- High contrast for readability  
- Modular panel layout  
- Smooth transitions  
- Minimalistic but powerful  
- Clear separation of user vs developer controls  

---

## 📊 Module Status  
- ⚠️ **Vo vývoji (Active Development)**  
- ✔ UI layout defined  
- ✔ Neon theme integrated  
- ✔ User/Developer modes functional  
- ✔ Output/Input pipeline connected  
- ✔ Module indicators active  
- 🔄 Prebieha integrácia s centrálnym orchestrátorom (`sirius_orchestrator.py`) a živými `PanelAPI` `[ÁNO/NIE]` potvrdzovacími slučkami  

---

## 🏁 Summary  
UI PANEL 6.x je primárne vizuálne rozhranie pre SIRIUS Local AI (v5.8) a je **aktuálne vo vývoji**.  
Poskytuje futuristické neonové prostredie s prehľadnou vizualizáciou pracovných postupov, dvoma režimami interakcie, podporou interaktívneho schvaľovania cez `PanelAPI` a monitorovaním modulov v reálnom čase pod dohľadom orchestrátora.
