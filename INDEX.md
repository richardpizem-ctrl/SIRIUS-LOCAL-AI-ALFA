# SIRIUS‑LOCAL‑AI‑ALFA  
**Lokálny AI systém s modulárnou architektúrou, real‑time spracovaním a plnou autonómiou.**

SIRIUS‑LOCAL‑AI‑ALFA je lokálny AI framework navrhnutý pre rýchlosť, stabilitu a modulárnosť.  
Projekt je postavený na jasnej architektúre, ktorá oddeľuje logiku, runtime, workflow, UI a triage systém.  
Celý systém funguje offline, bez externých závislostí a bez cloudových služieb.

---

## 📌 Obsah
- [Architektúra](ARCHITECTURE.md)
- [Module Map](MODULE_MAP.md)
- [Styleguide](STYLEGUIDE.md)
- [Testing Guide](TESTING_GUIDE.md)
- [Performance Guide](PERFORMANCE_GUIDE.md)
- [Release Plan](RELEASE_PLAN.md)

---

## 🚀 Hlavné vlastnosti

### **Modulárna architektúra**
Každý modul je izolovaný:
- `commands/`
- `context/`
- `filesystem/`
- `runtime/`
- `triage/`
- `ui/`
- `ui_components/`
- `workflow/`

Systém je navrhnutý tak, aby sa dal rozširovať bez zásahu do jadra.

---

### **Automatic Input Triage Engine (AITE)**
AITE analyzuje vstupy, klasifikuje ich a smeruje do správnych modulov.  
Zabezpečuje:
- správne rozpoznanie typu operácie  
- bezpečné smerovanie  
- nulové konflikty medzi modulmi  

---

### **Real‑Time Processing**
Systém obsahuje vlastný real‑time engine s:
- stabilným event loopom  
- optimalizovaným spracovaním  
- nízkou latenciou  
- predvídateľným výkonom  

---

### **UI vrstva**
UI je postavené na modulárnych komponentoch:
- `ui/` – logika UI  
- `ui_components/` – grafické prvky  
- `ui_components/animations/` – animácie (pripravené pre v2.0.0 a v3.0.0)

---

### **Workflow Engine**
Workflow vrstva riadi:
- operácie so súbormi  
- sekvenčné procesy  
- bezpečné vykonávanie príkazov  
- spätnú väzbu pre UI  

---

## 📁 Štruktúra projektu

