# Automatic Input Triage Engine (AITE)

AITE is a core module of **SIRIUS‑LOCAL‑AI v2.0.0** responsible for automatic detection, classification, and routing of user‑provided input.  
It ensures that the system immediately understands what the user inserted, downloaded, or provided — without questions, confirmations, or manual selection.

AITE is fully integrated into the **Runtime 2.0 architecture**, cooperating with the Filesystem Agent, Context Memory Engine, and Workflow Engine.

---

## ⚠️ MODULE STATUS — v2.0.0 (STABLE FOUNDATION)

AITE is now part of the stabilized module set in SIRIUS‑LOCAL‑AI v2.0.0.  
Its architecture is complete, predictable, and ready for future extensions.

- Fully local processing  
- Safe filesystem operations  
- Deterministic routing  
- Integrated with RuntimeManager 2.0  
- No external services or cloud dependencies  

AITE is stable, but additional capabilities (OCR, video detection, semantic classification) are planned for future versions.

---

## 1. Module Purpose

AITE automatically determines the type of input and routes it to the correct subsystem:

- **text →** text storage  
- **photo / image →** gallery (media storage)  
- **application / installer →** applications section  
- **documents →** document storage  
- **schoolwork →** *priority academic mode (NEW – v3.0.0)*  

This enables seamless automation and eliminates the need for user interaction during input handling.

---

## 2. Module Functions

### 2.1 Automatic Input Type Detection

AITE recognizes:

- plain text  
- images: png, jpg, jpeg, webp, gif  
- applications: exe, msi, zip, apk, dmg  
- documents: pdf, docx, txt  
- (future) audio, video, OCR‑based text extraction  
- (future) **schoolwork classification** — math, essays, homework, assignments  

### 2.2 Routing Logic

Based on the detected type, AITE determines:

- the correct storage location  
- the metadata to generate  
- the module responsible for further processing  
- whether a workflow or automation rule should be triggered  
- **whether the input qualifies as schoolwork and must bypass FAMILY time limits**  

### 2.3 Integration with Other Modules

AITE cooperates with:

- **FS‑AGENT** — performs file operations  
- **CME‑MEM** — stores context metadata  
- **Workflow Engine 2.0** — triggers next‑step predictions  
- **RuntimeManager 2.0** — orchestrates module communication  
- **SECURITY FAMILY (v3.0.0)** — ensures schoolwork is always allowed even under FAMILY restrictions  

---

## 3. Module Architecture

### 3.1 Components

- **InputClassifier** — detects the input type  
- **InputRouter** — selects the correct destination  
- **MetadataBuilder** — generates metadata for CME‑MEM  
- **AITEController** — orchestrates the entire triage process  
- **(v3.0.0) SchoolworkDetector** — identifies academic content and flags it as priority  

### 3.2 Processing Flow

1. User inserts text / image / file  
2. **InputClassifier** determines the type  
3. **SchoolworkDetector** checks if the content is academic  
4. **InputRouter** selects the target module  
5. **FS‑AGENT** performs the move/save operation  
6. **CME‑MEM** stores metadata  
7. **Workflow Engine** may trigger next‑step automation  
8. **SECURITY FAMILY** bypasses time limits if the input is schoolwork  

---

## 4. Future Extensions (Planned for v2.x → v3.x)

- OCR for automatic text extraction from images  
- Video detection and classification  
- Document semantic categorization  
- Automatic media tagging  
- AI‑assisted triage using contextual understanding  
- **Schoolwork Priority Mode** (NEW)  
  - academic detection  
  - FAMILY time‑limit bypass  
  - safe unrestricted access for homework  

---

## 5. Module Status — v2.0.0

AITE is **stable**, fully integrated, and ready for production use in SIRIUS‑LOCAL‑AI v2.0.0.  
Its architecture is complete and prepared for future intelligent extensions in version 3.0.0, including **schoolwork prioritization**.
