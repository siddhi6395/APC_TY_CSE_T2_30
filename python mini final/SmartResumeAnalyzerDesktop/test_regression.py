"""
test_regression.py - Comprehensive regression test suite for Smart Resume Analyzer & Scorer.
Tests PDF extraction, heading variations, contact detection (including Indian phone numbers
and LinkedIn references), skill detection precision (C, C++, etc.), scoring, and genuinely missing data.
"""

import os
import sys
import unittest
import docx

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from extractor import get_extractor, PDFExtractor, DOCXExtractor
from analyzer import (
    clean_text, analyze_text_nltk, extract_contact_details,
    detect_sections, detect_skills, analyze_action_words, estimate_career_field
)
from scorer import (
    calculate_structure_score, calculate_skills_score, calculate_contact_score,
    calculate_projects_exp_score, compute_overall_score, generate_strengths_and_suggestions
)
import database
import report


class TestResumeAnalyzerRegression(unittest.TestCase):

    def test_01_real_pdf_extraction_and_analysis(self):
        """Test extraction and end-to-end analysis of the representative sample PDF."""
        pdf_path = os.path.join(os.path.dirname(__file__), "scratch", "Arya_Jadhav_Resume.pdf")
        if not os.path.exists(pdf_path):
            self.skipTest(f"Sample PDF not found at {pdf_path}")

        extractor = get_extractor(pdf_path)
        raw_text = extractor.extract_text()
        self.assertTrue(len(raw_text) > 500, "Extracted text is too short")

        cleaned = clean_text(raw_text)
        self.assertTrue(len(cleaned.splitlines()) > 10, "Cleaned text should preserve multiple lines")

        # 1. Contact detection
        contact = extract_contact_details(cleaned)
        self.assertEqual(contact["email"], "aryajadhav279@gmail.com", "Email detection failed")
        self.assertEqual(contact["phone"], "8432705339", "Indian phone number detection failed")
        self.assertIsNotNone(contact["linkedin"], "LinkedIn reference should be detected")
        self.assertFalse(contact["linkedin_is_url"], "LinkedIn was a profile reference, not a full URL")

        # 2. Section detection
        sections = detect_sections(cleaned)
        self.assertTrue(sections["Career Objective"], "Summary section not detected")
        self.assertTrue(sections["Education"], "Education section not detected")
        self.assertTrue(sections["Technical Skills"], "Skills section not detected")
        self.assertTrue(sections["Work Experience"], "Experience section not detected")
        self.assertTrue(sections["Projects"], "Projects section not detected")
        self.assertTrue(sections["Certifications"], "Certifications section not detected")
        self.assertTrue(sections["Internships"], "Internships section not detected")

        # 3. Skills detection
        skills_by_cat, skills_set = detect_skills(cleaned)
        self.assertIn("Python", skills_set, "Python skill missing")
        self.assertIn("C++", skills_set, "C++ skill missing")
        self.assertIn("C", skills_set, "C skill missing in 'Languages: C, C++, Python'")
        self.assertIn("JavaScript", skills_set, "JavaScript / JS skill missing")
        self.assertIn("HTML", skills_set, "HTML skill missing")
        self.assertIn("CSS", skills_set, "CSS skill missing")
        self.assertIn("React", skills_set, "ReactJS skill missing")
        self.assertIn("MongoDB", skills_set, "MongoDB skill missing")

        # 4. Score calculation
        tokens, words, freq_dist, top_words = analyze_text_nltk(cleaned)
        found_actions, action_count = analyze_action_words(cleaned)
        career_field, field_scores = estimate_career_field(cleaned, skills_set)

        analysis_data = {
            "filename": "Arya_Jadhav_Resume.pdf",
            "sections": sections,
            "skills_set": skills_set,
            "skills_by_category": skills_by_cat,
            "contact": contact,
            "action_count": action_count,
            "found_action_words": found_actions,
            "word_count": len(words),
            "char_count": len(cleaned),
            "skills_count": len(skills_set),
            "career_field": career_field
        }

        breakdown, df_breakdown = compute_overall_score(analysis_data)
        strengths, suggestions = generate_strengths_and_suggestions(analysis_data, breakdown)

        # Total score should reflect good content (> 70), not 26!
        self.assertGreaterEqual(breakdown["total_score"], 70.0, "Score is unrealistically low")
        self.assertIn(breakdown["grade"], ["Very Good", "Excellent"])

        # Strengths and suggestions check
        self.assertTrue(any("LinkedIn profile reference" in s for s in strengths))
        self.assertTrue(any("Education, Technical Skills, and Projects" in s for s in strengths))

    def test_02_heading_variations(self):
        """Test realistic heading variations in capitalization, spacing, and punctuation."""
        variations = [
            ("SUMMARY", "Career Objective"),
            ("Professional Summary", "Career Objective"),
            ("Executive Summary", "Career Objective"),
            ("Career Objective", "Career Objective"),
            ("About Me", "Career Objective"),
            ("EDUCATION", "Education"),
            ("Academic Background", "Education"),
            ("Educational Qualifications", "Education"),
            ("1. Education:", "Education"),
            ("• Technical Skills:", "Technical Skills"),
            ("SKILLS & EXPERTISE", "Technical Skills"),
            ("Core Competencies", "Technical Skills"),
            ("Tools & Technologies", "Technical Skills"),
            ("Development Skills:", "Technical Skills"),
            ("Work Experience", "Work Experience"),
            ("PROFESSIONAL EXPERIENCE", "Work Experience"),
            ("Employment History", "Work Experience"),
            ("Experience", "Work Experience"),
            ("KEY PROJECTS", "Projects"),
            ("Technical Projects", "Projects"),
            ("Academic Projects", "Projects"),
            ("Certifications & Internships", "Certifications"),
            ("Certifications & Internships", "Internships"),
            ("Certifications and Internships", "Certifications"),
            ("Certifications and Internships", "Internships"),
            ("Internships", "Internships"),
            ("Virtual Internships", "Internships"),
            ("Achievements", "Achievements"),
            ("Awards & Honors", "Achievements"),
            ("Languages Known", "Languages"),
            ("Hobbies & Interests", "Interests")
        ]

        for text_sample, expected_section in variations:
            detected = detect_sections(text_sample)
            self.assertTrue(
                detected.get(expected_section),
                f"Failed to detect section '{expected_section}' from text '{text_sample}'"
            )

    def test_03_contact_detection_variations(self):
        """Test contact detection for email, Indian numbers, international numbers, and URLs/references."""
        # 1. Emails
        t1 = "Contact: john.doe@sub.company.co.in"
        self.assertEqual(extract_contact_details(t1)["email"], "john.doe@sub.company.co.in")

        t2 = "Email: mailto:aryan_jadhav.1@gmail.com."
        self.assertEqual(extract_contact_details(t2)["email"], "aryan_jadhav.1@gmail.com")

        # 2. Indian Phone numbers
        t_in1 = "Call me at 8432705339 for details."
        self.assertEqual(extract_contact_details(t_in1)["phone"], "8432705339")

        t_in2 = "Phone: +91 98765 43210"
        self.assertEqual(extract_contact_details(t_in2)["phone"], "+91 98765 43210")

        t_in3 = "📞+91-9876543210 | India"
        self.assertIn("9876543210", extract_contact_details(t_in3)["phone"])

        # 3. International Phone numbers
        t_intl = "Tel: +1 (987) 654-3210"
        self.assertIn("987", extract_contact_details(t_intl)["phone"])

        # 4. LinkedIn verified URL vs reference
        t_li_url = "Portfolio: https://www.linkedin.com/in/johndoe-dev/"
        c_li_url = extract_contact_details(t_li_url)
        self.assertTrue(c_li_url["linkedin_is_url"])
        self.assertIn("linkedin.com/in/johndoe-dev", c_li_url["linkedin"])

        t_li_ref = "John Doe | LinkedIn\nBangalore, India"
        c_li_ref = extract_contact_details(t_li_ref)
        self.assertFalse(c_li_ref["linkedin_is_url"])
        self.assertIn("LinkedIn", c_li_ref["linkedin"])

        # 5. GitHub verified URL vs reference
        t_gh_url = "Code: https://github.com/johndoe"
        c_gh_url = extract_contact_details(t_gh_url)
        self.assertTrue(c_gh_url["github_is_url"])
        self.assertEqual(c_gh_url["github"], "https://github.com/johndoe")

        t_gh_ref = "Git-Hub: johndoe_99"
        c_gh_ref = extract_contact_details(t_gh_ref)
        self.assertFalse(c_gh_ref["github_is_url"])
        self.assertIn("johndoe_99", c_gh_ref["github"])

    def test_04_skill_detection_precision(self):
        """Test skill detection accuracy and prevention of false positives (C++, C, R, Go)."""
        # C++ detection
        text_cpp = "Proficient in C++, Python, and Java."
        _, skills_cpp = detect_skills(text_cpp)
        self.assertIn("C++", skills_cpp)
        self.assertNotIn("C", skills_cpp, "C must not match inside 'C++' when C is not listed")

        # C programming language in proper context
        text_c = "Languages: C, C++, Python, Java."
        _, skills_c = detect_skills(text_c)
        self.assertIn("C", skills_c)
        self.assertIn("C++", skills_c)

        # C programming with / separator
        text_c_slash = "Core expertise in C/C++ development."
        _, skills_c_slash = detect_skills(text_c_slash)
        self.assertIn("C", skills_c_slash)
        self.assertIn("C++", skills_c_slash)

        # False positive tests for C: Should NOT match in arbitrary text
        arbitrary_texts = [
            "Completed Grade C in Chemistry.",
            "Section C: Additional Observations",
            "Report by Dr. C. Johnson",
            "High vitamin c content",
            "c/o Mumbai Office"
        ]
        for arb in arbitrary_texts:
            _, skills_arb = detect_skills(arb)
            self.assertNotIn("C", skills_arb, f"False positive: 'C' matched in '{arb}'")

        # Go language: should match when in programming context, NOT in 'Google'
        text_google = "Worked with Google Developer Groups on Campus."
        _, skills_google = detect_skills(text_google)
        self.assertNotIn("Go", skills_google, "'Go' should not match inside 'Google'")

        text_golang = "Programming: Go, Python, Docker"
        _, skills_golang = detect_skills(text_golang)
        self.assertIn("Go", skills_golang)

        # Skill aliases: JS, ReactJS, Express.js, Git-Hub
        text_aliases = "Tech: HTML5, CSS3, JS, ReactJS, Express.js, Git-Hub, DSA"
        _, skills_aliases = detect_skills(text_aliases)
        self.assertIn("JavaScript", skills_aliases)
        self.assertIn("React", skills_aliases)
        self.assertIn("Express", skills_aliases)
        self.assertIn("GitHub", skills_aliases)
        self.assertIn("DSA", skills_aliases)

    def test_05_genuinely_missing_information(self):
        """Test that genuinely missing information is properly reported and penalized without crashing."""
        sparse_text = "Just a short paragraph without contact information or section headers."
        contact = extract_contact_details(sparse_text)
        sections = detect_sections(sparse_text)
        _, skills_set = detect_skills(sparse_text)

        self.assertIsNone(contact["email"])
        self.assertIsNone(contact["phone"])
        self.assertIsNone(contact["linkedin"])
        self.assertIsNone(contact["github"])

        self.assertFalse(sections["Career Objective"])
        self.assertFalse(sections["Education"])
        self.assertFalse(sections["Technical Skills"])
        self.assertFalse(sections["Projects"])
        self.assertFalse(sections["Work Experience"])

        analysis_data = {
            "filename": "empty.pdf",
            "sections": sections,
            "skills_set": skills_set,
            "skills_by_category": {},
            "contact": contact,
            "action_count": 0,
            "found_action_words": [],
            "word_count": 10,
            "char_count": len(sparse_text),
            "skills_count": 0,
            "career_field": "Other / Undetermined"
        }

        breakdown, df_breakdown = compute_overall_score(analysis_data)
        strengths, suggestions = generate_strengths_and_suggestions(analysis_data, breakdown)

        # Score must be low
        self.assertLess(breakdown["total_score"], 40.0)
        self.assertEqual(breakdown["grade"], "Needs Improvement")

        # Suggestions must clearly guide adding the missing sections and contact details
        suggestion_text = " ".join(suggestions)
        self.assertIn("email", suggestion_text.lower())
        self.assertIn("phone", suggestion_text.lower())
        self.assertIn("Education", suggestion_text)

    def test_06_docx_extraction_and_relationships(self):
        """Test DOCX extraction and hyperlink relationship discovery."""
        test_docx_path = os.path.abspath("test_docx_regression.docx")
        doc = docx.Document()
        doc.add_heading("Jane Doe", level=1)
        doc.add_paragraph("Email: jane.doe@example.com | Phone: +91 9988776655")
        doc.add_paragraph("LinkedIn: linkedin.com/in/janedoe")
        doc.add_heading("Professional Summary", level=2)
        doc.add_paragraph("Experienced Software Engineer.")
        doc.add_heading("Education", level=2)
        doc.add_paragraph("Bachelor of Technology in Computer Science.")
        doc.add_heading("Technical Skills", level=2)
        doc.add_paragraph("Python, C++, Java, React, SQL")
        doc.add_heading("Projects", level=2)
        doc.add_paragraph("AI Resume Parser: Developed full-stack tool.")
        doc.add_heading("Certifications & Internships", level=2)
        doc.add_paragraph("Cloud Architecture Intern at TechCorp.")
        doc.save(test_docx_path)

        try:
            extractor = get_extractor(test_docx_path)
            raw = extractor.extract_text()
            self.assertIn("Professional Summary", raw)
            self.assertIn("jane.doe@example.com", raw)

            contact = extract_contact_details(raw)
            self.assertEqual(contact["email"], "jane.doe@example.com")
            self.assertIn("9988776655", contact["phone"])
            self.assertTrue(contact["linkedin_is_url"])

            sections = detect_sections(raw)
            self.assertTrue(sections["Career Objective"])
            self.assertTrue(sections["Education"])
            self.assertTrue(sections["Technical Skills"])
            self.assertTrue(sections["Projects"])
            self.assertTrue(sections["Certifications"])
            self.assertTrue(sections["Internships"])

        finally:
            if os.path.exists(test_docx_path):
                os.remove(test_docx_path)


if __name__ == "__main__":
    unittest.main()
