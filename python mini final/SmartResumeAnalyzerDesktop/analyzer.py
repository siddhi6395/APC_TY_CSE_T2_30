"""
analyzer.py - Resume Content Processing and Analysis Module
Demonstrates NLTK processing, Regular Expressions, String Manipulation, and Data Structures.
(SYLLABUS CONCEPT: Unit 1 - Data Structures & Strings, Unit 3 - NLTK & RegEx)
"""

import re
from collections import Counter
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist

# Configurable Categorized Technical Skill Dictionary
# (SYLLABUS CONCEPT: Unit 1 - Dictionaries & Lists)
SKILL_CATEGORIES = {
    "Programming": [
        "Python", "Java", "C++", "C#", "C", "JavaScript", "TypeScript",
        "PHP", "Ruby", "Swift", "Go", "Rust", "Kotlin", "R", "MATLAB", "DSA"
    ],
    "Web Development": [
        "HTML", "HTML5", "CSS", "CSS3", "JavaScript", "React", "React.js",
        "Angular", "Vue", "Vue.js", "Node.js", "Express", "Django", "Flask",
        "FastAPI", "Bootstrap", "Tailwind", "REST API", "GraphQL"
    ],
    "Databases": [
        "SQL", "MySQL", "PostgreSQL", "SQLite", "MongoDB", "Redis",
        "Oracle", "Microsoft SQL Server", "Firebase", "Cassandra"
    ],
    "Data Science & Analytics": [
        "NumPy", "Pandas", "Matplotlib", "Seaborn", "Scikit-learn", "SciPy",
        "Data Analysis", "Data Visualization", "Statistics", "Power BI", "Tableau", "Excel"
    ],
    "AI / Machine Learning": [
        "Machine Learning", "Deep Learning", "Artificial Intelligence", "NLP",
        "Natural Language Processing", "TensorFlow", "Keras", "PyTorch", "OpenCV",
        "Computer Vision", "Neural Networks"
    ],
    "Cloud & DevOps Tools": [
        "AWS", "Azure", "GCP", "Google Cloud", "Docker", "Kubernetes",
        "Git", "GitHub", "GitLab", "CI/CD", "Linux", "Bash", "Jira", "Cybersecurity"
    ]
}

# Key Resume Section Header Regular Expressions
# Whitespace-tolerant and covers realistic variations in capitalization, spacing, and punctuation
# (SYLLABUS CONCEPT: Unit 3 - Regular Expressions)
SECTION_PATTERNS = {
    "Career Objective": r"\b(objective|career\s+objective|professional\s+summary|executive\s+summary|career\s+summary|summary\s+of\s+qualifications|summary|profile|professional\s+profile|about\s+me)\b",
    "Education": r"\b(education|academic\s+background|academic\s+qualifications|educational\s+qualifications|qualification|qualifications|academics|scholastic\s+background|scholastic|degrees)\b",
    "Technical Skills": r"\b(skills|technical\s+skills|key\s+skills|core\s+skills|technologies|skills\s*&\s*expertise|technical\s+expertise|tools\s*&\s*technologies|core\s+competencies|areas\s+of\s+expertise|development\s+skills|programming\s+languages|technical\s+proficiencies)\b",
    "Projects": r"\b(projects|academic\s+projects|key\s+projects|personal\s+projects|capstone\s+projects|technical\s+projects|selected\s+projects|project\s+work|major\s+projects)\b",
    "Work Experience": r"\b(experience|work\s+experience|professional\s+experience|employment\s+history|work\s+history|relevant\s+experience|industry\s+experience|career\s+history)\b",
    "Internships": r"\b(internships?|practical\s+training|industrial\s+training|virtual\s+internships?|internship\s+experience|certifications?\s*(?:&|and)\s*internships?)\b",
    "Certifications": r"\b(certifications?|certifications?\s*(?:&|and)\s*internships?|certificates?|certifications?\s*&\s*licenses|licenses\s*&\s*certifications?|courses\s*(?:&|and)\s*certifications?|training\s*(?:&|and)\s*certifications?|courses|trainings?)\b",
    "Achievements": r"\b(achievements?|accomplishments?|awards?|honors?|honours?|awards?\s*(?:&|and)\s*honors?|extracurricular(?:\s+activities)?|co-curricular(?:\s+activities)?|key\s+achievements?)\b",
    "Languages": r"(?:^|\n)\s*(?:[\d•\-\*]+\.?\s*)?languages\s*[:\-—]?\s*(?:\n|$)|(?<!programming\s)\b(languages\s+known|linguistic\s+skills|spoken\s+languages|language\s+proficiency)\b",
    "Interests": r"\b(interests?|hobbies|hobbies\s*(?:&|and)\s*interests?|personal\s+interests?|areas\s+of\s+interest)\b"
}

# Professional Action Words for Resume Impact Analysis
ACTION_WORDS = [
    "developed", "designed", "implemented", "created", "built", "managed",
    "analyzed", "automated", "optimized", "tested", "improved", "deployed",
    "engineered", "architected", "integrated", "spearheaded", "formulated",
    "orchestrated", "lead", "led", "enhanced", "resolved", "collaborated",
    "refactored", "migrated", "scaled", "computed", "modeled", "launched"
]

# Keyword mappings for Career-Field Estimation
CAREER_FIELD_KEYWORDS = {
    "Software Development": ["python", "java", "c++", "c#", "object oriented", "software", "developer", "git", "data structures", "algorithms", "oop", "dsa"],
    "Web Development": ["html", "css", "javascript", "react", "node", "django", "flask", "web", "frontend", "backend", "full stack", "api", "express", "mongodb"],
    "Data Science": ["numpy", "pandas", "data science", "machine learning", "scikit-learn", "python", "statistics", "model", "r", "jupyter"],
    "Data Analytics": ["sql", "excel", "power bi", "tableau", "data analysis", "analytics", "visualization", "reporting", "dashboard"],
    "Artificial Intelligence / ML": ["machine learning", "deep learning", "nlp", "tensorflow", "pytorch", "neural networks", "ai", "computer vision", "ai/ml"],
    "Cloud Computing": ["aws", "azure", "gcp", "docker", "kubernetes", "cloud", "devops", "ci/cd", "terraform"],
    "Cybersecurity": ["cybersecurity", "security", "penetration testing", "network", "firewall", "cryptography", "vulnerability", "ethical hacking"]
}


def clean_text(text: str) -> str:
    """
    Normalizes whitespace and cleans extracted text while preserving line breaks
    for layout and section analysis. Also heals single-character split lines if present.
    (SYLLABUS CONCEPT: Unit 1 - String Methods)
    """
    if not text:
        return ""
    # Normalize unicode non-breaking and zero-width spaces
    text = text.replace('\xa0', ' ').replace('\u200b', '').replace('\ufeff', '')
    # Normalize CRLF and CR to LF
    text = text.replace('\r\n', '\n').replace('\r', '\n')

    # Detect and heal single-character split lines if extracted text has split glyphs
    lines = text.splitlines()
    non_empty = [l.strip() for l in lines if l.strip()]
    if len(non_empty) > 15 and (sum(1 for l in non_empty if len(l) == 1) / len(non_empty)) > 0.45:
        reconstructed = []
        curr = []
        for line in lines:
            s = line.strip()
            if len(s) == 1:
                curr.append(s)
            elif len(s) == 0:
                if curr:
                    reconstructed.append("".join(curr))
                    curr = []
                reconstructed.append("")
            else:
                if curr:
                    reconstructed.append("".join(curr))
                    curr = []
                reconstructed.append(s)
        if curr:
            reconstructed.append("".join(curr))
        lines = reconstructed

    # Collapse horizontal spaces/tabs on each line
    cleaned_lines = [re.sub(r'[ \t]+', ' ', line).strip() for line in lines]
    cleaned = '\n'.join(cleaned_lines)
    # Collapse 3 or more consecutive newlines down to 2
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    return cleaned.strip()


def analyze_text_nltk(text: str) -> tuple[list, list, FreqDist, list]:
    """
    Tokenizes text and calculates word frequencies using NLTK RegexpTokenizer and FreqDist.
    (SYLLABUS CONCEPT: Unit 3 - NLTK Library)
    """
    if not isinstance(text, str):
        empty_freq_dist = FreqDist()
        return [], [], empty_freq_dist, []

    # Tokenize words offline without requiring downloaded NLTK corpora
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text.lower())
    
    # Filter out short tokens and numbers for word frequency analysis
    words = [t for t in tokens if len(t) > 2 and not t.isdigit()]
    
    # Calculate NLTK Frequency Distribution
    freq_dist = FreqDist(words)
    top_words = freq_dist.most_common(10)
    
    return tokens, words, freq_dist, top_words


def extract_contact_details(text: str) -> dict:
    """
    Extracts email, phone number (supporting Indian 10-digit and international formats),
    LinkedIn URL or profile reference, and GitHub URL or profile reference.
    Distinguishes verified URLs from detected profile references.
    (SYLLABUS CONCEPT: Unit 3 - Regular Expressions)
    """
    contact = {
        "email": None,
        "phone": None,
        "linkedin": None,
        "linkedin_is_url": False,
        "github": None,
        "github_is_url": False
    }
    
    if not isinstance(text, str) or not text:
        return contact

    # 1. Email detection pattern (handles mailto: prefixes, emojis, and standard formats)
    email_match = re.search(r'(?:mailto:)?([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', text)
    if email_match:
        contact["email"] = email_match.group(1).rstrip('.')

    # 2. Phone number detection:
    # First priority: Indian mobile/phone numbers (10 digits starting with 6-9, optional +91 or 0, optional spaces/hyphens)
    phone_indian = re.search(
        r'(?:(?:\+91|0)[\s-]?)?[6-9]\d{4}[\s-]?\d{5}\b|'
        r'(?:(?:\+91|0)[\s-]?)?[6-9]\d{2}[\s-]?\d{3}[\s-]?\d{4}\b|'
        r'(?:(?:\+91|0)[\s-]?)?[6-9]\d{9}\b',
        text
    )
    if phone_indian:
        contact["phone"] = phone_indian.group(0).strip()
    else:
        # Fallback to international phone formats (e.g. +1 987-654-3210, (987) 654-3210)
        phone_intl = re.search(r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b', text)
        if phone_intl:
            contact["phone"] = phone_intl.group(0).strip()

    # 3. LinkedIn detection:
    # A. Check for verified clickable URL
    linkedin_url = re.search(r'(https?://)?(www\.)?linkedin\.com/(?:in|pub)/[\w\-_%]+/?', text, re.IGNORECASE)
    if linkedin_url:
        matched_url = linkedin_url.group(0).strip()
        if not matched_url.startswith("http"):
            matched_url = "https://" + matched_url
        contact["linkedin"] = matched_url
        contact["linkedin_is_url"] = True
    else:
        # B. Check for detected profile reference (e.g. 'Arya Jadhav | LinkedIn', 'LinkedIn: /in/johndoe', 'LinkedIn Profile')
        ref_match = re.search(
            r'([a-zA-Z0-9_\-.\s]{2,30})\s*\|\s*linkedin\b|'
            r'\blinkedin\s*[:|–—\-]\s*([a-zA-Z0-9_\-.\s/]{2,35})|'
            r'(?:in/([a-zA-Z0-9_\-]{3,30}))|'
            r'\b(linkedin\s+profile)\b',
            text,
            re.IGNORECASE
        )
        if ref_match:
            contact["linkedin"] = ref_match.group(0).strip()
            contact["linkedin_is_url"] = False
        elif re.search(r'\blinkedin\b', text, re.IGNORECASE):
            contact["linkedin"] = "LinkedIn (Profile Reference)"
            contact["linkedin_is_url"] = False

    # 4. GitHub detection:
    # A. Check for verified clickable URL
    github_url = re.search(r'(https?://)?(www\.)?github\.com/[\w\-_%]+/?', text, re.IGNORECASE)
    if github_url:
        matched_gh = github_url.group(0).strip()
        if not matched_gh.startswith("http"):
            matched_gh = "https://" + matched_gh
        contact["github"] = matched_gh
        contact["github_is_url"] = True
    else:
        # B. Check for detected profile reference (e.g. 'GitHub: username', 'Git-Hub: username')
        gh_ref = re.search(
            r'(?:github|git-hub)\s*[:|–—\-]\s*([a-zA-Z0-9_\-]{2,35})|'
            r'github\.com/([\w\-_%]+)',
            text,
            re.IGNORECASE
        )
        if gh_ref:
            contact["github"] = gh_ref.group(0).strip()
            contact["github_is_url"] = False

    return contact


def detect_sections(text: str) -> dict:
    """
    Detects present and missing sections in the resume using whitespace-tolerant regex patterns.
    (SYLLABUS CONCEPT: Unit 1 - Dictionaries & Loops, Unit 3 - Regular Expressions)
    """
    results = {}
    if not isinstance(text, str):
        return {section: False for section in SECTION_PATTERNS}

    for section, pattern in SECTION_PATTERNS.items():
        match = re.search(pattern, text, re.MULTILINE | re.IGNORECASE)
        results[section] = bool(match)
        
    return results


def detect_skills(text: str) -> tuple[dict, set]:
    """
    Detects technical skills by category using word boundaries and contextual rules.
    Prevents false positives on C++ and single-letter languages like C and R.
    Returns categorized dictionary and a set of all unique skills.
    (SYLLABUS CONCEPT: Unit 1 - Sets & Dictionaries, Unit 3 - Regular Expressions)
    """
    detected_by_category = {category: [] for category in SKILL_CATEGORIES}
    all_detected_skills = set()

    if not isinstance(text, str) or not text.strip():
        return detected_by_category, all_detected_skills
    
    # Helper: Contextual check for single-letter C programming language
    def _is_c_language(txt: str) -> bool:
        c_patterns = [
            r'(?i:\b(?:languages?|programming|coding|skills)\s*:[^\n]*?)\bC\b(?![+#])',
            r'\bC\s*(?:,|/|&)\s*(?:C\+\+|Java|Python|C#|Assembly|Rust|Go)\b',
            r'\b(?:Java|Python|C\+\+|Assembly|Rust|Go)\s*(?:,|/|&)\s*C\b(?![+#])',
            r'(?i:\bC\s+(?:programming|language|compiler|developer|code)\b)',
            r'(?i:\b(?:embedded|ansi)\s+C\b)',
            r'(?<![a-zA-Z0-9])C(?:\s*,\s*|\s*/\s*)C\+\+'
        ]
        return any(bool(re.search(p, txt)) for p in c_patterns)

    # Helper: Contextual check for single-letter R programming language
    def _is_r_language(txt: str) -> bool:
        r_patterns = [
            r'(?i:\b(?:languages?|programming|coding|data\s+science|skills)\s*:[^\n]*?)\bR\b',
            r'\bR\s*(?:,|/|&)\s*(?:Python|SQL|MATLAB|SAS|Julia)\b',
            r'\b(?:Python|SQL|MATLAB|SAS|Julia)\s*(?:,|/|&)\s*R\b',
            r'(?i:\bR\s+(?:programming|language|scripting|studio|package|packages)\b)'
        ]
        return any(bool(re.search(p, txt)) for p in r_patterns)

    for category, skills in SKILL_CATEGORIES.items():
        cat_skills = []
        for skill in skills:
            detected = False
            
            if skill == "C":
                detected = _is_c_language(text)
            elif skill == "R":
                detected = _is_r_language(text)
            elif skill == "C++":
                pattern = r'(?<![a-zA-Z0-9])C\+\+(?![a-zA-Z0-9+])'
                detected = bool(re.search(pattern, text))
            elif skill == "C#":
                pattern = r'(?<![a-zA-Z0-9])C#(?![a-zA-Z0-9#])'
                detected = bool(re.search(pattern, text))
            elif skill == "Go":
                pattern = (
                    r'(?i:\b(?:languages?|programming|coding|skills)\s*:[^\n]*?)\bGo\b|'
                    r'(?i:\b(?:golang|go\s+developer|go\s+programming|go\s+language)\b)|'
                    r'\bGo\s*(?:,|/|&)\s*(?:Python|Java|Rust|C\+\+|Docker)\b'
                )
                detected = bool(re.search(pattern, text))
            elif skill in ["JavaScript", "React", "Node.js", "Express", "GitHub", "Cybersecurity", "DSA"]:
                # Check standard skill name plus recognized aliases
                alias_map = {
                    "JavaScript": [r'\bjavascript\b', r'\bjs\b'],
                    "React": [r'\breact(?:\.js|js)?\b'],
                    "Node.js": [r'\bnode(?:\.js|js)?\b'],
                    "Express": [r'\bexpress(?:\.js|js)?\b'],
                    "GitHub": [r'\bgit-?hub\b'],
                    "Cybersecurity": [r'\bcyber-?security\b', r'\binformation\s+security\b'],
                    "DSA": [r'\bdsa\b', r'\bdata\s+structures\b']
                }
                aliases = alias_map.get(skill, [r'\b' + re.escape(skill) + r'\b'])
                detected = any(bool(re.search(pat, text, re.IGNORECASE)) for pat in aliases)
            else:
                pattern = r'\b' + re.escape(skill) + r'\b'
                detected = bool(re.search(pattern, text, re.IGNORECASE))
                
            if detected:
                cat_skills.append(skill)
                all_detected_skills.add(skill)
                
        detected_by_category[category] = cat_skills
        
    return detected_by_category, all_detected_skills


def analyze_action_words(text: str) -> tuple[list, int]:
    """
    Detects and counts professional action words used in bullet points.
    (SYLLABUS CONCEPT: Unit 1 - List Comprehension & Lambda Functions)
    """
    if not isinstance(text, str):
        return [], 0

    tokens = [t.lower() for t in re.findall(r'\b[a-zA-Z]+\b', text)]
    token_counts = Counter(tokens)
    
    found_words = []
    for word in ACTION_WORDS:
        count = token_counts.get(word, 0)
        if count > 0:
            found_words.append((word.capitalize(), count))
            
    # Sort action words by frequency descending using lambda function
    # (SYLLABUS CONCEPT: Unit 1 - Lambda Functions)
    found_words.sort(key=lambda x: x[1], reverse=True)
    total_count = sum(c for _, c in found_words)
    
    return found_words, total_count


def estimate_career_field(text: str, detected_skills: set) -> tuple[str, dict]:
    """
    Estimates the primary career field using keyword frequency scoring.
    (SYLLABUS CONCEPT: Unit 1 - Control Flow & Data Structures)
    """
    if not isinstance(text, str) or not text.strip():
        field_scores = {field: 0 for field in CAREER_FIELD_KEYWORDS}
        return "Other / Undetermined", field_scores

    text_lower = text.lower()
    field_scores = {}
    
    for field, keywords in CAREER_FIELD_KEYWORDS.items():
        score = 0
        for kw in keywords:
            matches = len(re.findall(r'\b' + re.escape(kw) + r'\b', text_lower))
            score += matches
            if any(kw == skill.lower() for skill in detected_skills):
                score += 2  # Higher weight for detected technical skills
        field_scores[field] = score
        
    # Sort fields by score
    sorted_fields = sorted(field_scores.items(), key=lambda x: x[1], reverse=True)
    
    top_field, top_score = sorted_fields[0]
    if top_score == 0:
        estimated_field = "Other / Undetermined"
    else:
        estimated_field = top_field
        
    return estimated_field, field_scores
