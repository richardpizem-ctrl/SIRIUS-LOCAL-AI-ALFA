# Module Map – SIRIUS LOCAL AI ALFA

Tento dokument definuje všetky moduly projektu, ich účel, zodpovednosti a vzájomné prepojenia. Slúži ako orientačná mapa architektúry.

---

## 1. Runtime Core
**Účel:** Centrálna vrstva systému.  
**Zodpovednosti:**
- inicializácia modulov
- plánovanie úloh
- bezpečnostné obmedzenia
- správa životného cyklu

---

## 2. Filesystem Agent (FS-AGENT)
**Účel:** Bezpečné operácie so súbormi.  
**Zodpovednosti:**
- presúvanie, kopírovanie, mazanie
- validácia ciest
- potvrdenia akcií
- spätná väzba pre používateľa

---

## 3. Command Interpreter (CME)
**Účel:** Preklad používateľských príkazov.  
**Zodpovednosti:**
- rozpoznanie typu príkazu
- extrakcia parametrov
- rozhodovanie, ktorý modul vykoná akciu
- generovanie otázok „Kam?“ a „Potvrdiť?“

---

## 4. Context Memory Engine (CME-MEM)
**Účel:** Držanie kontextu a posledných krokov.  
**Zodpovednosti:**
- sledovanie posledných akcií
- uchovávanie ciest a stavov
- poskytovanie kontextových návrhov

---

## 5. Workflow Tracker
**Účel:** Logika sekvencií krokov.  
**Zodpovednosti:**
- sledovanie workflow
- predikcia ďalšieho kroku
- automatické návrhy akcií

---

## 6. UI Confirm Module
**Účel:** Interaktívne tabuľky a potvrdenia.  
**Zodpovednosti:**
- výber cieľového priečinka
- potvrdenie akcie
- bezpečnostné dialógy
- automatické otváranie okien podľa typu príkazu

---

## 7. Email Composer
**Účel:** Generovanie textov emailov (bez odosielania).  
**Zodpovednosti:**
- návrhy emailov
- profesionálne odpovede
- štruktúrované texty

---

## 8. Automatic Input Triage Engine (AITE)
**Účel:** Automatické rozpoznávanie typu vstupu a jeho zaradenie.  
**Zodpovednosti:**
- detekcia typu vstupu (text, foto, aplikácia)
- smerovanie do správneho úložiska
- tvorba metadát
- integrácia s FS-AGENT a CME-MEM

AITE zabezpečuje, že SIRIUS AI okamžite pochopí, čo používateľ vložil alebo stiahol, a správne to zatriedi bez potreby otázok.

---

## 9. Future Modules (rozšíriteľnosť)
**Možné budúce moduly:**
- UI Automation Layer
- Voice Command Layer
- System Monitoring Layer
- Plugin API

---

## 10. Prepojenia medzi modulmi
- **CME → FS-AGENT:** rozhoduje, čo sa má vykonať  
- **CME → UI Confirm:** generuje otázky  
- **CME-MEM → Workflow Tracker:** poskytuje kontext  
- **AITE → FS-AGENT:** smeruje vstupy podľa typu  
- **AITE → CME-MEM:** ukladá metadáta o vstupe  
- **Runtime Core → všetky moduly:** inicializácia a bezpečnosť
