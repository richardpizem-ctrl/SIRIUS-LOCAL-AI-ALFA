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
Každý modul má vlastný priečinok:

