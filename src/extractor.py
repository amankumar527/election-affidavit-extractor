import os
import pdfplumber
import pytesseract
import pandas as pd
from src.utils import extract_name, extract_phones, extract_assembly

# ===========================
# ✅ CONFIG — Update these paths
# ===========================

# Windows users: update this path to your Tesseract installation
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Folder containing all affidavit PDFs
PDF_FOLDER = r"C:\Users\Shivam\Downloads\electionData"

# Output Excel file name
OUTPUT_FILE = "data/output/affidavit_candidate_phone_constituency.xlsx"


# ===========================
# PDF TEXT EXTRACTION
# ===========================

def extract_text_with_pdfplumber(file_path: str) -> str:
    """Extract text from digital/text-based PDF pages."""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    return text


def ocr_pdf_with_pdfplumber(file_path: str) -> str:
    """OCR fallback for scanned/image-based PDFs using pytesseract."""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            img = page.to_image(resolution=300).original
            text += pytesseract.image_to_string(img)
            text += "\n"
    return text


# ===========================
# MAIN LOOP
# ===========================

results = []

pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.lower().endswith(".pdf")]
print(f"📂 Found {len(pdf_files)} PDF files. Starting extraction...\n")

for i, file in enumerate(pdf_files, 1):
    file_path = os.path.join(PDF_FOLDER, file)
    text = ""

    # Step 1: Try normal text extraction
    try:
        text = extract_text_with_pdfplumber(file_path)
    except Exception as e:
        print(f"  ⚠️  pdfplumber failed for {file}: {e}")
        text = ""

    # Step 2: OCR fallback if text too short
    if len(text.strip()) < 50:
        print(f"  🔍 Running OCR on: {file}")
        try:
            text = ocr_pdf_with_pdfplumber(file_path)
        except Exception as e:
            print(f"  ❌ OCR also failed for {file}: {e}")

    # Step 3: Extract fields
    name = extract_name(text)
    phones = extract_phones(text)
    assembly = extract_assembly(text)

    row = {
        "pdf_file": file,
        "candidate_name": name,
        "assembly_constituency": assembly
    }

    # Store up to 5 phone numbers in separate columns
    for j in range(5):
        row[f"phone_{j+1}"] = phones[j] if j < len(phones) else ""

    results.append(row)
    print(f"  ✅ [{i}/{len(pdf_files)}] {file} → {name} | {assembly} | {phones[:2]}")


# ===========================
# SAVE TO EXCEL
# ===========================

df = pd.DataFrame(results)

cols = ["pdf_file", "candidate_name", "assembly_constituency",
        "phone_1", "phone_2", "phone_3", "phone_4", "phone_5"]
df = df.reindex(columns=cols)

os.makedirs("data/output", exist_ok=True)
df.to_excel(OUTPUT_FILE, index=False)

# Summary stats
total = len(df)
found_name = (df["candidate_name"] != "NOT FOUND").sum()
found_phone = (df["phone_1"] != "").sum()
found_assembly = (df["assembly_constituency"] != "NOT FOUND").sum()

print(f"\n{'='*50}")
print(f"✅ EXTRACTION COMPLETE!")
print(f"{'='*50}")
print(f"📄 Total PDFs processed : {total}")
print(f"👤 Names found          : {found_name}/{total} ({found_name/total*100:.1f}%)")
print(f"📞 Phones found         : {found_phone}/{total} ({found_phone/total*100:.1f}%)")
print(f"🏛️  Constituency found   : {found_assembly}/{total} ({found_assembly/total*100:.1f}%)")
print(f"💾 Output saved to      : {OUTPUT_FILE}")
