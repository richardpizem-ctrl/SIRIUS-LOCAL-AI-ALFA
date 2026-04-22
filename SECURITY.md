# Security Policy – SIRIUS LOCAL AI ALFA

Tento dokument definuje bezpečnostné zásady projektu a pravidlá pre nahlasovanie zraniteľností. Systém pracuje so súborovým systémom používateľa, preto je bezpečnosť najvyššou prioritou.

---

## 1. Bezpečnostný model
SIRIUS LOCAL AI ALFA funguje výhradne lokálne a nikdy:
- neodosiela dáta mimo zariadenia
- nevykonáva akcie bez potvrdenia používateľa
- nepracuje so sieťovými operáciami
- neukladá citlivé dáta mimo lokálneho kontextu

Všetky operácie sú explicitne potvrdené používateľom.

---

## 2. Prístup k súborom
Filesystem Agent (FS‑AGENT):
- vykonáva iba povolené operácie
- vždy vyžaduje potvrdenie pred presunom, kopírovaním alebo mazáním
- validuje cesty a zabraňuje nebezpečným operáciám (napr. root-level delete)

---

## 3. Ochrana pred neúmyselnými akciami
Systém obsahuje:
- dvojstupňové potvrdenia
- kontextové varovania
- ochranu pred rekurzívnym mazáním
- ochranu pred presunom mimo povolených oblastí

---

## 4. Nahlasovanie zraniteľností
Ak objavíte bezpečnostnú chybu, nahláste ju súkromne:

**security@sirius-local-ai.dev**  
(placeholder – nahradí sa po vytvorení oficiálnej domény)

Prosíme:
- neposielajte zraniteľnosti ako verejné issues
- neposielajte exploit kód do verejných komentárov

---

## 5. Podporované verzie
Bezpečnostné aktualizácie sú poskytované pre:
- ALFA (aktuálna fáza)
- BETA (po vydaní)
- 1.0 (stabilná verzia)

Staršie verzie nemusia dostávať opravy.

---

## 6. Zásady pre príspevky
Každý príspevok musí:
- rešpektovať bezpečnostný model
- neobchádzať potvrdenia používateľa
- nezasahovať do sandboxu
- neumožniť nebezpečné operácie bez validácie

---

## 7. Stav dokumentu
Aktuálna verzia: **ALFA**
