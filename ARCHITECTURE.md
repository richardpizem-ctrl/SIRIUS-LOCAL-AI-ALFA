# Architektúra projektu SIRIUS LOCAL AI ALFA

SIRIUS LOCAL AI ALFA je modulárny lokálny AI runtime navrhnutý tak, aby bezpečne a presne vykonával príkazy v rámci jedného PC. Architektúra je rozdelená do samostatných modulov, ktoré spolu komunikujú cez definované rozhrania a držia konzistentný kontext používateľa.

---

## 1. Runtime Core
Základná vrstva systému, ktorá zabezpečuje:
- inicializáciu modulov
- správu životného cyklu
- plánovanie úloh
- bezpečnostné obmedzenia (sandboxing, povolené operácie)

---

## 2. Filesystem Agent (FS-AGENT)
Zodpovedný za všetky operácie so súbormi:
- presúvanie, kopírovanie, mazanie
- validácia ciest
- bezpečnostné potvrdenia
- spätná väzba pre používateľa

FS-AGENT nikdy nevykoná akciu bez explicitného potvrdenia.

---

## 3. Command Interpreter (CME)
Vrstva, ktorá prekladá používateľské príkazy do interných akcií:
- rozpoznávanie typu príkazu
- extrakcia parametrov
- rozhodovanie, ktorý modul má akciu vykonať
- generovanie otázok typu „Kam?“ alebo „Potvrdiť?“

---

## 4. Context Memory Engine (CME-MEM)
Drží celý koncept PC a workflow:
- posledné akcie používateľa
- posledné cesty a priečinky
- stav rozpracovaných úloh
- kontextové návrhy ďalších krokov

---

## 5. Workflow Tracker
Zodpovedný za:
- sledovanie sekvencie krokov
- predikciu ďalšieho logického kroku
- automatické ponuky (napr. „Chceš vložiť do README?“)

---

## 6. UI Confirm Module
Vrstva pre interaktívne tabuľky:
- výber cieľového priečinka
- potvrdenie akcie
- bezpečnostné dialógy
- automatické otváranie okien podľa typu príkazu

---

## 7. Email Composer (bez odosielania)
Modul generuje:
- návrhy emailov
- štruktúrované texty
- profesionálne odpovede

Nikdy nič neodosiela — iba pripravuje obsah.

---

## 8. Modularita a rozšíriteľnosť
Každý modul je samostatný a môže byť rozšírený:
- nové typy príkazov
- nové UI komponenty
- nové workflow logiky
- nové bezpečnostné vrstvy

---

## 9. Stav projektu
ALFA – definícia architektúry, návrh modulov, príprava implementácie.
