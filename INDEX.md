# SIRIUS‑LOCAL‑AI  
**A fully modular, offline AI runtime with a stable architecture, plugin ecosystem, and real‑time processing.**

SIRIUS‑LOCAL‑AI is a next‑generation local AI framework designed for **speed, stability, modularity, and full offline autonomy**.  
Version **2.0.0** introduces a complete Runtime 2.0 architecture, Plugin System 2.0, Workflow Engine 2.0, AI Loop 2.0, GUI 2.0, and a fully stabilized module ecosystem.

The entire system runs **100% locally**, without external dependencies or cloud services.

---

## 📌 Table of Contents
- [Architecture](ARCHITECTURE.md)
- [Module Map](MODULE_MAP.md)
- [Styleguide](STYLEGUIDE.md)
- [Testing Guide](TESTING_GUIDE.md)
- [Performance Guide](PERFORMANCE_GUIDE.md)
- [Release Notes](RELEASE_NOTES.md)
- [Roadmap](ROADMAP.md)

---

## 🚀 Key Features

### **Modular Architecture (v2.0.0)**
Each module is isolated and follows strict boundaries:

- `commands/` – NL routing and command logic  
- `context/` – context memory engine  
- `filesystem/` – safe file operations  
- `runtime/` – Runtime Core 2.0  
- `triage/` – AITE 2.0  
- `ui/` – GUI logic  
- `ui_components/` – graphical elements  
- `workflow/` – Workflow Engine 2.0  
- `plugins/` – Plugin System 2.0  

The system is designed to be extended **without modifying the core**.

---

### **Plugin System 2.0**
Plugins can define:

- NL commands  
- AI tasks  
- workflows  
- AI loop rules  
- GUI elements  

All official plugins are fully prepared for v2.0.0.

---

### **Automatic Input Triage Engine (AITE 2.0)**
AITE analyzes inputs, classifies them, and routes them to the correct modules.

It ensures:

- correct input type detection  
- safe routing  
- deterministic behavior  
- zero conflicts between modules  

---

### **Real‑Time Processing**
The system includes a custom real‑time engine with:

- a stable event loop  
- optimized processing  
- low latency  
- predictable performance  

---

### **GUI Layer 2.0**
The UI is built on modular components:

- `ui/` – UI logic  
- `ui_components/` – graphical elements  
- `ui_components/animations/` – animations (ready for v2.0.0 and v3.0.0)  

---

### **Workflow Engine 2.0**
The workflow layer manages:

- multi‑step processes  
- safe command execution  
- plugin workflows  
- predictable state transitions  
- UI feedback  

---
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
├── plugins/
└── sirius.py
## 📁 Project Structure (v2.0.0)

Each directory has a clear responsibility and is described in **MODULE_MAP.md**.

---

## 🧪 Testing
The project includes a complete testing plan:

- manual tests  
- Git Bash tests  
- real‑time tests  
- UI tests  
- workflow sequence tests  
- plugin integration tests  

Details are in **TESTING_GUIDE.md**.

---

## ⚙️ Performance
The system is optimized for:

- low latency  
- long‑term stability  
- predictable processing  
- minimal thread blocking  
- efficient event routing  

More in **PERFORMANCE_GUIDE.md**.

---

## 🗓️ Release Plan

### **v2.0.0 – Current Stable Release**
- Runtime 2.0  
- Plugin System 2.0  
- Workflow Engine 2.0  
- AI Loop 2.0  
- GUI 2.0  
- AITE 2.0  
- WIN‑CAP 2.0  
- Full plugin suite  
- Complete documentation refresh  

### **v3.0.0 – Intelligent Runtime**
- AI‑assisted triage  
- semantic workflows  
- advanced GUI/tray/voice integration  
- contextual automation  

### **v4.0.0 – Self‑Repair & Health‑Check Layer**
- integrity checks  
- safe automatic repairs  
- patch suggestions  
- system‑wide health reporting  

---

## 🧩 License
The project is open‑source and available to the community.  
The license is provided in **LICENSE**.

---

## ✨ Author
**Richard Pizem**  
Visionary architect & solo maintainer  
SIRIUS‑LOCAL‑AI

