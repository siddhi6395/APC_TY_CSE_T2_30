"""
report.py - Plain Text Report Export Module
Demonstrates File I/O operations and String Formatting in Python.
(SYLLABUS CONCEPT: Unit 2 - File Handling & Input/Output)
"""

import os
from datetime import datetime


def generate_report_text(record: dict) -> str:
    """
    Formats the complete analysis record into a structured plain-text report.
    (SYLLABUS CONCEPT: Unit 1 & 2 - String Formatting & File Content Generation)
    """
    filename = record.get("filename", "Resume.pdf")
    date_str = record.get("analysis_date", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    overall_score = record.get("overall_score", 0.0)
    grade = record.get("grade", "N/A")
    career_field = record.get("career_field", "Undetermined")
    word_count = record.get("word_count", 0)
    char_count = record.get("char_count", 0)
    skills_count = record.get("skills_count", 0)
    
    breakdown = record.get("breakdown", {})
    categories = breakdown.get("categories", [])
    earned = breakdown.get("earned", [])
    max_pts = breakdown.get("max", [])
    percentages = breakdown.get("percentage", [])
    
    contact = record.get("contact", {})
    sections = record.get("sections", {})
    skills_cat = record.get("skills_by_category", {})
    strengths = record.get("strengths", [])
    suggestions = record.get("suggestions", [])

    lines = []
    lines.append("================================================================================")
    lines.append("                 SMART RESUME ANALYZER & SCORE REPORT                           ")
    lines.append("================================================================================")
    lines.append(f"Resume Filename : {filename}")
    lines.append(f"Analysis Date   : {date_str}")
    lines.append(f"Estimated Field : {career_field}")
    lines.append(f"Overall Score   : {overall_score} / 100 ({grade})")
    lines.append("--------------------------------------------------------------------------------\n")
    
    lines.append("1. QUICK STATISTICS")
    lines.append("--------------------------------------------------------------------------------")
    lines.append(f" - Word Count           : {word_count}")
    lines.append(f" - Character Count      : {char_count}")
    lines.append(f" - Technical Skills     : {skills_count}")
    lines.append(f" - Sections Detected    : {sum(1 for v in sections.values() if v)} / {len(sections)}\n")

    lines.append("2. SCORE BREAKDOWN BY CATEGORY")
    lines.append("--------------------------------------------------------------------------------")
    lines.append(f"{'Category':<32} | {'Earned':<8} | {'Max':<8} | {'Percentage'}")
    lines.append("-" * 68)
    for cat, e, m, p in zip(categories, earned, max_pts, percentages):
        lines.append(f"{cat:<32} | {e:<8.1f} | {m:<8.1f} | {p}%")
    lines.append("-" * 68)
    lines.append(f"{'TOTAL SCORE':<32} | {overall_score:<8.1f} | 100.0    | {overall_score}%\n")

    lines.append("3. CONTACT DETAILS DETECTED")
    lines.append("--------------------------------------------------------------------------------")
    li_val = contact.get('linkedin')
    if li_val:
        li_label = f"{li_val} [Verified URL]" if contact.get('linkedin_is_url') else f"{li_val} [Profile Reference]"
    else:
        li_label = "Not Detected"

    gh_val = contact.get('github')
    if gh_val:
        gh_label = f"{gh_val} [Verified URL]" if contact.get('github_is_url') else f"{gh_val} [Profile Reference]"
    else:
        gh_label = "Not Detected"

    lines.append(f" - Email    : {contact.get('email') or 'Not Detected'}")
    lines.append(f" - Phone    : {contact.get('phone') or 'Not Detected'}")
    lines.append(f" - LinkedIn : {li_label}")
    lines.append(f" - GitHub   : {gh_label}\n")

    lines.append("4. RESUME SECTIONS STATUS")
    lines.append("--------------------------------------------------------------------------------")
    for sec, status in sections.items():
        symbol = "[PRESENT]" if status else "[MISSING]"
        lines.append(f" - {sec:<28} : {symbol}")
    lines.append("")

    lines.append("5. DETECTED TECHNICAL SKILLS")
    lines.append("--------------------------------------------------------------------------------")
    has_skills = False
    for cat, skills_list in skills_cat.items():
        if skills_list:
            has_skills = True
            lines.append(f" [{cat}]")
            lines.append(f"   {', '.join(skills_list)}")
    if not has_skills:
        lines.append(" - No standard technical skills detected.")
    lines.append("")

    lines.append("6. STRENGTHS IDENTIFIED")
    lines.append("--------------------------------------------------------------------------------")
    for idx, s in enumerate(strengths, 1):
        lines.append(f" {idx}. {s}")
    lines.append("")

    lines.append("7. ACTIONABLE IMPROVEMENT SUGGESTIONS")
    lines.append("--------------------------------------------------------------------------------")
    for idx, s in enumerate(suggestions, 1):
        lines.append(f" {idx}. {s}")
    lines.append("")
    
    lines.append("================================================================================")
    lines.append("Disclaimer: This score is a rule-based offline assessment of structure, content,")
    lines.append("and technical skill coverage generated by Smart Resume Analyzer.")
    lines.append("================================================================================")

    return "\n".join(lines)


def save_report_to_file(record: dict, output_filepath: str):
    """
    Writes generated report text to specified output file.
    (SYLLABUS CONCEPT: Unit 2 - Writing Files)
    """
    report_content = generate_report_text(record)
    output_dir = os.path.dirname(os.path.abspath(output_filepath))
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(output_filepath, "w", encoding="utf-8") as f:
        f.write(report_content)
