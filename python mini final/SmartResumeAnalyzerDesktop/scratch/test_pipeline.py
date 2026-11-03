"""
scratch/test_pipeline.py - Automated verification test script for backend components.
"""

import os
import sys
import docx
import pypdf

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from extractor import get_extractor, DOCXExtractor, PDFExtractor
from analyzer import (
    clean_text, analyze_text_nltk, extract_contact_details,
    detect_sections, detect_skills, analyze_action_words, estimate_career_field
)
from scorer import compute_overall_score, generate_strengths_and_suggestions
import database
import report

def run_tests():
    print("=== STARTING BACKEND PIPELINE VERIFICATION TESTS ===")

    # Test 1: Create a synthetic DOCX resume file
    test_docx_path = os.path.abspath("test_resume.docx")
    doc = docx.Document()
    doc.add_heading("John Doe - Software Engineer", level=1)
    doc.add_paragraph("Email: john.doe@example.com | Phone: +1 987-654-3210")
    doc.add_paragraph("LinkedIn: linkedin.com/in/johndoe | GitHub: github.com/johndoe")
    
    doc.add_heading("Career Objective", level=2)
    doc.add_paragraph("Passionate Software Engineer seeking to develop scalable web applications and data pipelines.")
    
    doc.add_heading("Education", level=2)
    doc.add_paragraph("B.Tech in Computer Science and Engineering, 2024")
    
    doc.add_heading("Technical Skills", level=2)
    doc.add_paragraph("Programming: Python, Java, C++, JavaScript")
    doc.add_paragraph("Web Development: HTML, CSS, React, Django, REST API")
    doc.add_paragraph("Databases: SQL, PostgreSQL, MongoDB")
    doc.add_paragraph("Data Science & Tools: NumPy, Pandas, Matplotlib, Git, AWS, Docker")
    
    doc.add_heading("Projects", level=2)
    doc.add_paragraph("Smart Resume Analyzer: Developed an offline desktop application in Python using Tkinter, NumPy, and Pandas to evaluate resume completeness.")
    doc.add_paragraph("E-Commerce Web Portal: Designed and implemented a full-stack platform using React and Django REST framework.")
    
    doc.add_heading("Work Experience", level=2)
    doc.add_paragraph("Software Engineering Intern: Automated data extraction pipelines and optimized backend queries.")

    doc.save(test_docx_path)
    print(f"[OK] Synthetic test DOCX created: {test_docx_path}")

    # Test 2: Extraction test
    extractor = get_extractor(test_docx_path)
    text = extractor.extract_text()
    assert len(text) > 100, "Extracted text is empty or too short!"
    print("[OK] Text extraction successful!")

    # Test 3: NLTK Analysis
    tokens, words, freq_dist, top_words = analyze_text_nltk(text)
    print(f"[OK] NLTK tokenization: {len(tokens)} tokens, {len(words)} words.")

    # Test 4: Contact Extraction
    contact = extract_contact_details(text)
    assert contact["email"] == "john.doe@example.com", "Email regex extraction failed!"
    assert "johndoe" in contact["github"], "GitHub regex extraction failed!"
    print(f"[OK] Contact extraction successful: {contact}")

    # Test 5: Section Detection
    sections = detect_sections(text)
    assert sections["Education"] is True, "Education section missing!"
    assert sections["Projects"] is True, "Projects section missing!"
    print(f"[OK] Section detection successful: {sum(1 for v in sections.values() if v)} present.")

    # Test 6: Skill Detection
    skills_by_cat, skills_set = detect_skills(text)
    assert "Python" in skills_set, "Skill Python not detected!"
    assert "Django" in skills_set, "Skill Django not detected!"
    print(f"[OK] Skill detection successful: {len(skills_set)} skills found ({skills_set}).")

    # Test 7: Action Words & Career Field
    found_actions, action_count = analyze_action_words(text)
    field, field_scores = estimate_career_field(text, skills_set)
    print(f"[OK] Action words found: {action_count}, Estimated Career Field: {field}")

    # Test 8: Scoring & DataFrame
    analysis_data = {
        "filename": "test_resume.docx",
        "sections": sections,
        "skills_set": skills_set,
        "skills_by_category": skills_by_cat,
        "contact": contact,
        "action_count": action_count,
        "found_action_words": found_actions,
        "word_count": len(words),
        "char_count": len(text),
        "skills_count": len(skills_set),
        "career_field": field
    }
    breakdown, df_breakdown = compute_overall_score(analysis_data)
    strengths, suggestions = generate_strengths_and_suggestions(analysis_data, breakdown)
    print(f"[OK] Score computation successful! Total Score: {breakdown['total_score']} / 100 ({breakdown['grade']})")

    # Test 9: SQLite Database
    database.init_db("test_history.db")
    rec_data = {
        "filename": "test_resume.docx",
        "overall_score": breakdown["total_score"],
        "grade": breakdown["grade"],
        "career_field": field,
        "word_count": len(words),
        "char_count": len(text),
        "skills_count": len(skills_set),
        "sections": sections,
        "skills_by_category": skills_by_cat,
        "contact": contact,
        "breakdown": breakdown,
        "strengths": strengths,
        "suggestions": suggestions
    }
    rec_id = database.save_analysis_record(rec_data, "test_history.db")
    fetched = database.fetch_record_by_id(rec_id, "test_history.db")
    assert fetched["overall_score"] == breakdown["total_score"], "Database record mismatch!"
    print("[OK] SQLite database insert and fetch successful!")

    # Test 10: Report Generation
    rep_text = report.generate_report_text(fetched)
    assert "SMART RESUME ANALYZER & SCORE REPORT" in rep_text, "Report header missing!"
    print("[OK] Report generation successful!")

    # Clean up test artifacts
    if os.path.exists(test_docx_path):
        os.remove(test_docx_path)
    if os.path.exists("test_history.db"):
        os.remove("test_history.db")

    print("\nALL BACKEND PIPELINE VERIFICATION TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_tests()
