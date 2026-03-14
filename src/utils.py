import re
from src.patterns import NAME_PATTERNS, PHONE_PATTERNS, SINGLE_PHONE_PATTERN, ASSEMBLY_PATTERNS


def extract_name(text: str) -> str:
    """Extract candidate name from affidavit text."""
    for pattern in NAME_PATTERNS:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return "NOT FOUND"


def extract_phones(text: str) -> list:
    """Extract all Indian phone numbers from affidavit text."""
    numbers = set()

    # Context-based extraction (near labels like 'Mobile No', 'Contact')
    for pattern in PHONE_PATTERNS:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            found = SINGLE_PHONE_PATTERN.findall(match)
            for num in found:
                numbers.add(num[-10:])  # keep last 10 digits

    # Fallback: find any phone number anywhere in text
    fallback = SINGLE_PHONE_PATTERN.findall(text)
    for num in fallback:
        numbers.add(num[-10:])

    return sorted(numbers)


def clean_constituency(val: str) -> str:
    """Normalize constituency name — fix spacing, hyphens, commas."""
    v = re.sub(r'\s+', ' ', val).strip()
    v = v.replace("–", "-")
    v = re.sub(r'\s*-\s*', '-', v)
    v = re.sub(r'\s*,\s*', ', ', v)
    return v


def extract_assembly(text: str) -> str:
    """Extract assembly constituency name and number from text."""
    # Full text pass
    for pat in ASSEMBLY_PATTERNS:
        m = re.search(pat, text, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL)
        if m:
            return clean_constituency(m.group(1))

    # Line-by-line fallback (handles OCR line breaks)
    for ln in text.splitlines():
        line = ln.strip()
        if not line:
            continue
        for pat in ASSEMBLY_PATTERNS:
            m = re.search(pat, line, flags=re.IGNORECASE)
            if m:
                return clean_constituency(m.group(1))

    return "NOT FOUND"
