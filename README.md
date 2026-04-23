# SIRIUS LOCAL AI ALFA

Modulárny lokálny AI runtime pre správu súborov, workflow a bezpečné vykonávanie príkazov v rámci jedného PC. Projekt je navrhnutý ako rozšíriteľná architektúra s oddelenými modulmi pre filesystem, interpretáciu príkazov, kontextovú pamäť, workflow tracking, UI potvrdenia a automatický triage vstupov.

## Hlavné vlastnosti
- automatické presúvanie súborov a priečinkov
- kontextové tabuľky „Kam?“ a „Potvrdiť?“
- bezpečnostné potvrdenia pred každou akciou
- modulárna architektúra (filesystem, command interpreter, context memory, workflow tracker, UI)
- generovanie emailových návrhov bez automatického odoslania
- AI drží celý koncept PC a posledné kroky používateľa
- rozšíriteľné moduly podľa budúcich problémov
- **automatický triage vstupov (AITE) – AI sama rozpozná, či ide o text, foto alebo aplikáciu a správne to zaradí**

## Automatic Input Triage Engine (AITE)
AITE je modul, ktorý automaticky rozpoznáva typ vstupu a bez otázok ho zaradí do správnej kategórie:

### Rozpoznávané typy:
- **Text** → uloží sa do textového úložiska
- **Foto / obrázok** → presunie sa do galérie (media storage)
- **Aplikácia / inštalačný súbor** → zaradí sa do sekcie aplikácií

### Funkcie:
- automatická detekcia typu vstupu
- smerovanie do správneho úložiska
- tvorba metadát
- integrácia s FS-AGENT a CME-MEM

AITE zabezpečuje, že SIRIUS AI okamžite pochopí, čo používateľ vložil alebo stiahol, a správne to zatriedi.

## Stav projektu
ALFA – návrh architektúry, príprava modulov.
