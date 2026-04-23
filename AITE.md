# Automatic Input Triage Engine (AITE)

AITE je modul SIRIUS LOCAL AI ALFA, ktorý automaticky rozpoznáva typ vstupu
a smeruje ho do správnej kategórie bez potreby otázok alebo potvrdení.

---

## 1. Účel modulu
AITE zabezpečuje, že AI okamžite pochopí, čo používateľ vložil, stiahol
alebo odoslal, a správne to zatriedi:

- text → textové úložisko
- foto / obrázok → galéria (media storage)
- aplikácia / inštalačný súbor → sekcia aplikácií

---

## 2. Funkcie modulu

### 2.1 Automatická detekcia typu vstupu
AITE rozpoznáva:
- čistý text
- obrázky (png, jpg, jpeg, webp, gif)
- aplikácie (exe, msi, zip, apk, dmg)
- dokumenty (pdf, docx, txt) – voliteľné rozšírenie

### 2.2 Routing (smerovanie)
Podľa typu vstupu AITE rozhodne:
- kam súbor patrí
- aké metadáta sa majú uložiť
- ktorý modul má prevziať ďalšie spracovanie

### 2.3 Integrácia s ostatnými modulmi
AITE spolupracuje s:
- FS-AGENT (práca so súbormi)
- CME-MEM (kontextová pamäť)
- Workflow Tracker (predikcia ďalších krokov)

---

## 3. Architektúra modulu

### 3.1 Komponenty
- **InputClassifier** – rozpoznáva typ vstupu
- **InputRouter** – rozhoduje, kam sa má vstup uložiť
- **MetadataBuilder** – vytvára metadáta pre ďalšie moduly
- **AITEController** – hlavná riadiaca vrstva

### 3.2 Tok spracovania
1. Používateľ vloží text / obrázok / súbor
2. InputClassifier určí typ
3. InputRouter vyberie cieľový modul
4. FS-AGENT vykoná presun / uloženie
5. CME-MEM uloží kontext
6. Workflow Tracker ponúkne ďalší krok

---

## 4. Budúce rozšírenia
- OCR pre automatické čítanie textu z obrázkov
- detekcia videí
- kategorizácia dokumentov podľa obsahu
- automatické tagovanie médií

---

## 5. Stav modulu
ALFA – definícia, návrh, príprava implementácie.
