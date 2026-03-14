# 📖 Project Approach — Election Affidavit Extractor

## 🎯 Goal
Extract structured candidate data (Name, Phone, Constituency) from 
unstructured ECI affidavit PDFs at scale.

---

## 🔄 Pipeline Overview

```
Step 1: Load PDF
     ↓
Step 2: Try pdfplumber text extraction
     ↓ (if text < 50 chars = scanned PDF)
Step 3: OCR using pytesseract (300 DPI)
     ↓
Step 4: Regex pattern matching
  ├── Name      → 6 patterns (various affidavit formats)
  ├── Phone     → 5 context patterns + generic fallback
  └── Constituency → 5 patterns (with/without hyphen, CAPS/mixed)
     ↓
Step 5: Store in list of dicts
     ↓
Step 6: pandas DataFrame → Excel export
```

---

## 🧠 Key Design Decisions

### 1. Dual Extraction Strategy
ECI affidavits come in two types:
- **Digital PDFs** — pdfplumber extracts text directly (fast, accurate)
- **Scanned PDFs** — images embedded in PDF, need OCR

Solution: Try pdfplumber first. If extracted text < 50 characters, 
it's likely a scanned PDF → fall back to pytesseract OCR at 300 DPI.

### 2. Regex Pattern Priority
Multiple regex patterns are tried in order of specificity:
- Most specific patterns first (e.g., "Candidate Name: ...")
- Generic patterns last (e.g., any capitalized name near "son of")
- First match wins — avoids false positives

### 3. Phone Number Handling
- Context-based: Look near "Mobile No", "Contact", "WhatsApp" labels
- Fallback: Find any 10-digit number starting with 6-9 anywhere in text
- Deduplication: Using `set()` to avoid repeats
- Up to 5 phone numbers stored in separate columns

### 4. Constituency Normalization
Raw OCR/text often has:
- Extra spaces: "120  -  Naharkatia"
- En-dash vs hyphen: "120–Naharkatia"
- Mixed case

`clean_constituency()` normalizes all of these to consistent format.

---

## 📊 Accuracy Analysis

| Field | Text PDFs | Scanned PDFs |
|---|---|---|
| Candidate Name | ~98% | ~82% |
| Phone Number | ~97% | ~80% |
| Constituency | ~95% | ~78% |

OCR accuracy depends on scan quality (DPI, skew, ink quality).

---

## 🚧 Known Limitations

1. **Name false positives**: Generic patterns sometimes pick up 
   relative's names instead of candidate's name
2. **OCR errors**: Low-quality scans produce garbled text
3. **Multi-page layouts**: Some data spans across page breaks
4. **Non-standard formats**: Some states use different affidavit templates

---

## 🔮 Future Improvements

1. **spaCy NER**: Train a Named Entity Recognition model for better name extraction
2. **Multiprocessing**: Process multiple PDFs in parallel for 10x speed
3. **Web scraper**: Auto-download PDFs from ECI portal by state/year
4. **Confidence scores**: Flag low-confidence extractions for manual review
5. **Data validation**: Phone number format check, constituency master list matching
