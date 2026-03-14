import re

# ===========================
# NAME PATTERNS
# ===========================
NAME_PATTERNS = [
    r'Candidate\s*Name\s*[:\-]\s*([A-Z][a-zA-Z ]{3,60})',
    r'Name\s+of\s+(?:the\s+)?Deponent\s*[:\-]\s*([A-Z][a-zA-Z ]{3,60})',
    r'I,\s*([A-Z][a-zA-Z ]{3,60})\s*(?:son|daughter|wife|husband)\s+of',
    r'([A-Z][a-zA-Z ]{3,60})\s*(?:son|daughter|wife|husband)\s+of',
    r'(?:Father\'?s|Mother\'?s|Husband\'?s)\s+Name\s*[:\-]\s*([A-Z][a-zA-Z ]{3,60})',
    r'(?:Shri|Mr\.?|Mrs\.?)\s+([A-Z][a-zA-Z ]{3,60})'
]

# ===========================
# PHONE / WHATSAPP PATTERNS
# ===========================
PHONE_PATTERNS = [
    r'My\s+contact\s+telephone\s+number(?:s)?\s*(?:is|are)\s*[:\-]?\s*([0-9,\s\-]+)',
    r'Contact\s+Telephone\s+Number(?:s)?\s*(?:is|are)?\s*[:\-]?\s*([0-9,\s\-]+)',
    r'Telephone\s+Number(?:s)?\s*(?:is|are)?\s*[:\-]?\s*([0-9,\s\-]+)',
    r'Mobile\s+No\.?\s*[:\-]?\s*([0-9,\s\-]+)',
    r'WhatsApp\s*(?:No\.?|Number)?\s*[:\-]?\s*([0-9,\s\-]+)'
]

# Generic Indian phone: +91 optional, starts 6-9, 10 digits
SINGLE_PHONE_PATTERN = re.compile(r'(?:\+91[\s\-]?)?[6-9]\d{9}')

# ===========================
# ASSEMBLY CONSTITUENCY PATTERNS
# ===========================
ASSEMBLY_PATTERNS = [
    r'FROM\s+([0-9]{1,3}\s*[-–,]\s*[A-Z][A-Za-z \.\(\)\/]{2,60})\s+ASSEMBLY\s+CONSTITUENCY',
    r'enrolled\s+in\s+([0-9]{1,3}\s*[-–,]\s*[A-Z][A-Za-z \.\(\)\/]{2,60})\s+Assembly\s+constituency',
    r'Number\s+and\s+name\s+of\s+the\s+constituency.*?\s([0-9]{1,3}\s*[-–,]?\s*[A-Z][A-Za-z \.\(\)\/]{2,60})\s+ASSEMBLY\s+CONSTITUENCY',
    r'\b([0-9]{1,3}\s*[,–-]\s*[A-Z][A-Za-z \.\(\)\/]{2,60})\s+CONSTITUENCY\b',
    r'\b([0-9]{1,3}\s+[A-Z][A-Za-z \.\(\)\/]{2,60})\s+Assembly\s+Constituency\b',
]
