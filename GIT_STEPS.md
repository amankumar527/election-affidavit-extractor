# 🚀 GitHub Pe Upload Karne Ke Steps — Copy Paste Karo

---

## STEP 1 — GitHub Pe New Repository Banao

1. GitHub.com kholo → Login karo
2. Top-right mein "+" button → "New repository" click karo
3. Fill karo:
   - **Repository name**: `election-affidavit-extractor`
   - **Description**: `Automated extraction of candidate data from ECI affidavit PDFs`
   - **Public** select karo
   - ❌ README initialize mat karo (already hai)
4. **"Create repository"** click karo
5. Page pe jo URL dikhega woh copy karo (example: `https://github.com/yourname/election-affidavit-extractor.git`)

---

## STEP 2 — Apne Computer Pe Ye Commands Chalao

Yeh folder kahan save hai uske andar terminal/cmd kholo aur ek-ek karke yeh commands run karo:

```bash
# 1. Git initialize karo
git init

# 2. Saari files stage karo
git add .

# 3. Pehla commit karo
git commit -m "feat: initial project - ECI affidavit PDF data extractor"

# 4. Branch ka naam set karo
git branch -M main

# 5. GitHub se connect karo (apna URL daalo)
git remote add origin https://github.com/YOUR_USERNAME/election-affidavit-extractor.git

# 6. Push karo
git push -u origin main
```

> ⚠️ `YOUR_USERNAME` ki jagah apna GitHub username daalo

---

## STEP 3 — Excel Output File Upload Karo

Excel file manually upload karo:
1. GitHub pe apni repo kholo
2. `data/output/` folder mein jao
3. "Add file" → "Upload files" click karo
4. `affidavit_candidate_phone_constituency.xlsx` drag karo
5. Commit message: `data: add sample Excel output`
6. "Commit changes" click karo

---

## STEP 4 — Screenshots Upload Karo

Same tarah `screenshots/` folder mein apne screenshots daalo:
- Output Excel ka screenshot
- Code run hone ka screenshot (Image 7 wala — jahan "DONE!" print hua)

---

## STEP 5 — Repository Ko Polish Karo

GitHub repo page pe:
1. **Description** mein likho: `Automated PDF data extraction from ECI affidavits using Python, OCR & Regex`
2. **Website**: `https://affidavit.eci.gov.in/`
3. **Topics/Tags** add karo (gear icon click karo):
   ```
   python  data-extraction  ocr  pandas  regex  election-data  pdfplumber  pytesseract  data-analysis  open-government-data
   ```

---

## ✅ Verification — Yeh Check Karo

- [ ] README preview sahi dikh raha hai
- [ ] `src/` folder mein 3 files hain
- [ ] `requirements.txt` visible hai
- [ ] `.gitignore` visible hai
- [ ] Excel output `data/output/` mein hai
- [ ] Topics add ho gaye hain

---

## 🎯 Final GitHub Link Example

```
https://github.com/YOUR_USERNAME/election-affidavit-extractor
```

Yeh link apne resume aur portfolio mein add karo! 🚀
