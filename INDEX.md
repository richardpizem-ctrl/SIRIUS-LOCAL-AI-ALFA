# SIRIUS‑LOCAL‑AI‑ALFA  
**A local AI system with a modular architecture, real‑time processing, and full autonomy.**

SIRIUS‑LOCAL‑AI‑ALFA is a local AI framework designed for speed, stability, and modularity.  
The project is built on a clear architecture that separates logic, runtime, workflow, UI, and the triage system.  
The entire system runs offline, without external dependencies or cloud services.

---

## 📌 Table of Contents
- [Architecture](ARCHITECTURE.md)
- [Module Map](MODULE_MAP.md)
- [Styleguide](STYLEGUIDE.md)
- [Testing Guide](TESTING_GUIDE.md)
- [Performance Guide](PERFORMANCE_GUIDE.md)
- [Release Plan](RELEASE_PLAN.md)

---

## 🚀 Key Features

### **Modular Architecture**
Each module is isolated:
- `commands/`
- `context/`
- `filesystem/`
- `runtime/`
- `triage/`
- `ui/`
- `ui_components/`
- `workflow/`

The system is designed to be extended without modifying the core.

---

### **Automatic Input Triage Engine (AITE)**
AITE analyzes inputs, classifies them, and routes them to the correct modules.  
It ensures:
- correct operation detection  
- safe routing  
- zero conflicts between modules  

---

### **Real‑Time Processing**
The system includes a custom real‑time engine with:
- a stable event loop  
- optimized processing  
- low latency  
- predictable performance  

---

### **UI Layer**
The UI is built on modular components:
- `ui/` – UI logic  
- `ui_components/` – graphical elements  
- `ui_components/animations/` – animations (prepared for v2.0.0 and v3.0.0)

---

### **Workflow Engine**
The workflow layer manages:
- file operations  
- sequential processes  
- safe command execution  
- feedback for the UI  

---

## 📁 Project Structure
src/
├── commands/
├── context/
├── email/
├── filesystem/
├── runtime/
├── triage/
├── ui/
├── ui_components/
│    └── animations/
├── workflow/
└── sirius.py

Each directory has a clear responsibility and is described in **MODULE_MAP.md**.

---

## 🧪 Testing
The project includes a complete testing plan:
- manual tests  
- Git Bash tests  
- real‑time tests  
- UI tests  
- workflow sequence tests  

Details are in **TESTING_GUIDE.md**.

---

## ⚙️ Performance
The system is optimized for:
- low latency  
- long‑term stability  
- predictable processing  
- minimal thread blocking  

More in **PERFORMANCE_GUIDE.md**.

---

## 🗓️ Release Plan

### **v1.0.0 – Stable Release**
- complete architecture  
- all modules in Phase 4  
- UI + workflow + runtime  
- documentation  
- final GitHub test  

### **v2.0.0 – Extended Architecture**
- EventBus deque  
- Graphic Primitives separation  
- multithreaded StreamHandler  
- undo/redo  
- cached grid rendering  
- TextInput class  
- hover effects  

### **v3.0.0 – Advanced Visualizations**
- RGB pulsing based on velocity  
- polyphonic key‑pressure waveform  
- 3D key‑press effect  
- MPE visualization (X/Y/Z)  
- per‑note vibrato animation  

---

## 🧩 License
The project is open‑source and available to the community.  
The license is provided in **LICENSE**.

---

## ✨ Author
**Richard Pizem**  
Visionary architect & solo maintainer  
SIRIUS‑LOCAL‑AI‑ALFA

