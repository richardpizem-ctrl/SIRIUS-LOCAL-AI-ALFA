# Automatic Input Triage Engine (AITE)

AITE is a module of SIRIUS LOCAL AI ALFA that automatically detects the type of input
and routes it to the correct category without requiring questions or confirmations.

---

## ⚠️ ALPHA WARNING

AITE interacts with Windows 11 filesystem operations and cooperates with privileged modules
such as FS‑AGENT and CME‑MEM.  
The project is currently in **ALPHA**, and module behavior may evolve as development continues.

- Windows Defender or SmartScreen may classify the runtime as an “Unknown App”.  
- Antivirus tools may generate false positives during development.  
- Some operations may require elevated permissions (UAC).  
- All processing is fully local; no data leaves the user's PC.

**Users are encouraged to test features independently.**  
This is an ALPHA‑stage developer tool — the author does not provide individual guidance for basic operations.

---

## 1. Module Purpose

AITE ensures that the AI immediately understands what the user inserted, downloaded,
or provided, and classifies it correctly:

- text → text storage  
- photo / image → gallery (media storage)  
- application / installer → applications section  

---

## 2. Module Functions

### 2.1 Automatic Input Type Detection
AITE recognizes:
- plain text  
- images (png, jpg, jpeg, webp, gif)  
- applications (exe, msi, zip, apk, dmg)  
- documents (pdf, docx, txt) – optional extension  

### 2.2 Routing
Based on the input type, AITE decides:
- where the file belongs  
- what metadata should be stored  
- which module should handle further processing  

### 2.3 Integration with Other Modules
AITE cooperates with:
- FS‑AGENT (file operations)  
- CME‑MEM (context memory)  
- Workflow Tracker (next‑step prediction)  

---

## 3. Module Architecture

### 3.1 Components
- **InputClassifier** – detects the input type  
- **InputRouter** – decides where the input should be stored  
- **MetadataBuilder** – generates metadata for other modules  
- **AITEController** – main control layer  

### 3.2 Processing Flow
1. User inserts text / image / file  
2. InputClassifier determines the type  
3. InputRouter selects the target module  
4. FS‑AGENT performs the move / save  
5. CME‑MEM stores context  
6. Workflow Tracker suggests the next step  

---

## 4. Future Extensions
- OCR for automatic text extraction from images  
- video detection  
- document categorization based on content  
- automatic media tagging  

---

## 5. Module Status
ALPHA – definition, design, and implementation preparation.
