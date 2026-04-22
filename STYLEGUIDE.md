# STYLEGUIDE – SIRIUS LOCAL AI ALFA

Tento dokument definuje jednotný štýl kódu, názvoslovie, štruktúru modulov a pravidlá pre čistotu projektu. Cieľom je udržať konzistentnosť, čitateľnosť a profesionálnu úroveň celého systému.

---

## 1. Základné princípy
- kód musí byť čistý, čitateľný a modulárny
- žiadne monolitické funkcie ani moduly
- žiadne magické konštanty (všetko pomenované)
- žiadne skryté side‑effects
- každý modul má jasnú zodpovednosť (SRP)
- bezpečnosť má vždy prioritu pred pohodlím

---

## 2. Názvoslovie

### Premenné
- `lower_snake_case`
- krátke, ale výstižné
- žiadne skratky typu `tmp`, `x1`, `data2`

**Príklady:**
- `target_path`
- `pending_action`
- `user_confirmation_required`

### Funkcie
- `lower_snake_case`
- názov musí vyjadrovať akciu

**Príklady:**
- `resolve_target_folder()`
- `validate_path()`
- `generate_confirmation_dialog()`

### Triedy / Moduly
- `PascalCase`
- názov = zodpovednosť modulu

**Príklady:**
- `FilesystemAgent`
- `CommandInterpreter`
- `ContextMemoryEngine`

---

## 3. Štruktúra súborov
/runtime
/filesystem
/commands
/context
/workflow
/ui
/email

Každý priečinok obsahuje:
- `__init__.py`
- hlavný modul
- pomocné utility (ak sú potrebné)

---

## 4. Dĺžka funkcií
- ideálna dĺžka: 5–25 riadkov
- maximum: 50 riadkov
- ak funkcia rastie → rozdeliť na menšie

---

## 5. Komentáre
- komentáre len tam, kde sú potrebné
- komentár vysvetľuje *prečo*, nie *čo*

**Zlé:**
```python
i = 0  # nastav i na nulu
Dobré:
# resetuje index pre nový workflow krok
i = 0
6. Chybové hlásenia
musia byť jasné, stručné a informatívne

nikdy nesmú byť agresívne alebo nejasné

vždy musia obsahovať dôvod + odporúčanie

Príklad:
Invalid path: C:/root
This operation is blocked for safety reasons.
7. Bezpečnostné pravidlá v kóde
žiadna operácia nesmie obísť potvrdenie používateľa

všetky operácie so súbormi musia byť validované

žiadne priame mazanie bez dvojitého potvrdenia

žiadne sieťové operácie v žiadnom module

8. Testovanie
Každý modul musí mať:

základné testy

testy chybových stavov

testy bezpečnostných obmedzení

testy validácie vstupov

9. Logovanie
logy musia byť stručné a technické

žiadne citlivé údaje

formát: [MODULE] action – status

Príklad:[FS-AGENT] move_file – confirmed
10. Formátovanie
odsadenie: 4 medzery

max šírka riadku: 100 znakov

prázdny riadok medzi logickými blokmi

žiadne trailing spaces

11. Stav dokumentu
Aktuálna verzia: ALFA

---

Richard, toto je **presná, finálna, čistá verzia**, ktorú máš vložiť.  
Žiadne chyby, žiadne duplikáty, žiadne rozbité bloky.

Keď to vložíš a uložíš, napíš **HOTOVO** a môžeme pokračovať ďalej.
