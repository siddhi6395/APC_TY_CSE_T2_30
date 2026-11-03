"""
scorer.py - Resume Transparent Score Calculator & Suggestion Generator
Demonstrates numerical calculations with NumPy and tabular formatting with Pandas.
(SYLLABUS CONCEPT: Unit 3 - NumPy & Pandas Libraries)
"""

import numpy as np
import pandas as pd


def calculate_structure_score(sections: dict) -> float:
    """Calculates structure score out of 20 points based on section presence."""
    core_sections = ["Career Objective", "Education", "Technical Skills", "Projects"]
    score = 0.0
    for sec in core_sections:
        if sections.get(sec, False):
            score += 3.0  # 4 * 3 = 12 points max
            
    # Experience component (either Work Experience or Internships fulfills experience for students/professionals)
    has_experience = sections.get("Work Experience", False) or sections.get("Internships", False)
    if has_experience:
        score += 3.0  # 15 points total for core structure
        
    # Bonus sections for comprehensive profiles
    bonus_sections = ["Certifications", "Achievements", "Languages", "Interests"]
    # If candidate has both Work Experience and Internships, grant bonus credit
    if sections.get("Work Experience", False) and sections.get("Internships", False):
        score += 1.25

    for sec in bonus_sections:
        if sections.get(sec, False):
            score += 1.25 # 4 * 1.25 = 5 points max
            
    return float(np.clip(score, 0, 20))


def calculate_skills_score(skills_set: set) -> float:
    """Calculates skills score out of 20 points based on detected technical skills count."""
    num_skills = len(skills_set)
    if num_skills == 0:
        score = 0.0
    elif num_skills <= 3:
        score = 6.0 + (num_skills * 1.5)
    elif num_skills <= 7:
        score = 11.0 + ((num_skills - 3) * 1.25)
    elif num_skills <= 11:
        score = 16.0 + ((num_skills - 7) * 0.75)
    else:
        score = 20.0
        
    return float(np.clip(score, 0, 20))


def calculate_projects_exp_score(sections: dict, word_count: int) -> float:
    """Calculates Projects and Experience score out of 20 points."""
    score = 0.0
    if sections.get("Projects", False):
        score += 8.0
    if sections.get("Work Experience", False) or sections.get("Internships", False):
        score += 8.0
        
    if word_count >= 300:
        score += 4.0
    elif word_count >= 150:
        score += 2.0
        
    return float(np.clip(score, 0, 20))


def calculate_contact_score(contact: dict) -> float:
    """Calculates Contact Details score out of 10 points."""
    score = 0.0
    if contact.get("email"):
        score += 3.0
    if contact.get("phone"):
        score += 3.0

    # LinkedIn: 2.0 pts for verified clickable URL, 1.5 pts for detected profile reference
    if contact.get("linkedin"):
        score += 2.0 if contact.get("linkedin_is_url", False) else 1.5

    # GitHub: 2.0 pts for verified clickable URL, 1.5 pts for detected profile reference
    if contact.get("github"):
        score += 2.0 if contact.get("github_is_url", False) else 1.5
        
    return float(np.clip(score, 0, 10))


def calculate_action_words_score(action_word_count: int) -> float:
    """Calculates Professional Action Words score out of 10 points."""
    score = float(action_word_count) * 1.0
    return float(np.clip(score, 0, 10))


def calculate_relevant_content_score(word_count: int, skills_count: int) -> float:
    """Calculates Relevant Content & Keyword Depth score out of 10 points."""
    score = 0.0
    if word_count >= 250:
        score += 4.0
    elif word_count >= 100:
        score += 2.0
        
    if skills_count >= 5:
        score += 6.0
    elif skills_count >= 2:
        score += 3.0
        
    return float(np.clip(score, 0, 10))


def calculate_readability_score(word_count: int, char_count: int) -> float:
    """Calculates Readability & Text Quality score out of 10 points."""
    if word_count == 0:
        return 0.0
        
    avg_word_length = char_count / word_count
    score = 5.0
    
    # Word count evaluation
    if 250 <= word_count <= 800:
        score += 3.0
    elif 150 <= word_count <= 1000:
        score += 1.5
        
    # Vocabulary evaluation
    if 4.5 <= avg_word_length <= 7.0:
        score += 2.0
    else:
        score += 1.0
        
    return float(np.clip(score, 0, 10))


def compute_overall_score(analysis_data: dict) -> tuple[dict, pd.DataFrame]:
    """
    Computes total resume score out of 100 using NumPy array operations.
    Returns breakdown dictionary and Pandas DataFrame.
    (SYLLABUS CONCEPT: Unit 3 - NumPy & Pandas Libraries)
    """
    sections = analysis_data.get("sections", {})
    skills_set = analysis_data.get("skills_set", set())
    contact = analysis_data.get("contact", {})
    action_count = analysis_data.get("action_count", 0)
    word_count = analysis_data.get("word_count", 0)
    char_count = analysis_data.get("char_count", 0)
    
    # Calculate category scores
    s_struct = calculate_structure_score(sections)
    s_skills = calculate_skills_score(skills_set)
    s_proj = calculate_projects_exp_score(sections, word_count)
    s_contact = calculate_contact_score(contact)
    s_action = calculate_action_words_score(action_count)
    s_rel = calculate_relevant_content_score(word_count, len(skills_set))
    s_read = calculate_readability_score(word_count, char_count)
    
    # Store numerical scores in NumPy arrays (SYLLABUS CONCEPT: Unit 3 - NumPy Arrays)
    category_names = [
        "Resume structure",
        "Skills",
        "Projects and experience",
        "Contact information",
        "Professional action words",
        "Relevant keywords & content",
        "Readability & text quality"
    ]
    
    earned_points = np.array([s_struct, s_skills, s_proj, s_contact, s_action, s_rel, s_read], dtype=float)
    max_points = np.array([20.0, 20.0, 20.0, 10.0, 10.0, 10.0, 10.0], dtype=float)
    
    # Vectorized percentage calculation with NumPy
    percentages = np.round((earned_points / max_points) * 100, 1)
    
    # Calculate total score using np.sum
    total_earned = float(np.sum(earned_points))
    total_earned = float(np.clip(total_earned, 0, 100))
    
    # Score classification
    if total_earned >= 90:
        grade = "Excellent"
    elif total_earned >= 75:
        grade = "Very Good"
    elif total_earned >= 60:
        grade = "Good"
    else:
        grade = "Needs Improvement"
        
    breakdown_dict = {
        "categories": category_names,
        "earned": earned_points.tolist(),
        "max": max_points.tolist(),
        "percentage": percentages.tolist(),
        "total_score": round(total_earned, 1),
        "grade": grade
    }
    
    # Construct Pandas DataFrame (SYLLABUS CONCEPT: Unit 3 - Pandas DataFrame)
    df_breakdown = pd.DataFrame({
        "Category": category_names,
        "Earned Points": earned_points,
        "Max Points": max_points,
        "Percentage (%)": percentages
    })
    
    return breakdown_dict, df_breakdown


def generate_strengths_and_suggestions(analysis_data: dict, breakdown: dict) -> tuple[list, list]:
    """
    Generates genuine strengths and actionable improvement suggestions based on actual resume data.
    Avoids penalizing the same missing information multiple times.
    (SYLLABUS CONCEPT: Unit 1 - Control Flow & Strings)
    """
    strengths = []
    suggestions = []
    
    sections = analysis_data.get("sections", {})
    skills_set = analysis_data.get("skills_set", set())
    contact = analysis_data.get("contact", {})
    action_count = analysis_data.get("action_count", 0)
    word_count = analysis_data.get("word_count", 0)
    
    # Evaluate Strengths
    has_core_sections = sections.get("Education") and sections.get("Projects") and sections.get("Technical Skills")
    if has_core_sections:
        strengths.append("Strong resume foundation with Education, Technical Skills, and Projects sections present.")
    if sections.get("Certifications") or sections.get("Internships"):
        strengths.append("Demonstrated professional initiative with Certifications and Internship experience.")

    if len(skills_set) >= 8:
        strengths.append(f"Broad technical skill set with {len(skills_set)} detected technical skills.")
    elif len(skills_set) >= 4:
        strengths.append(f"Good range of {len(skills_set)} technical skills identified.")
        
    if contact.get("email") and contact.get("phone"):
        strengths.append("Essential contact details (Email address and Phone number) are clearly provided.")
    elif contact.get("email"):
        strengths.append("Valid email address is clearly provided.")
    elif contact.get("phone"):
        strengths.append("Contact phone number is clearly provided.")

    if contact.get("linkedin"):
        if contact.get("linkedin_is_url"):
            strengths.append("Professional LinkedIn profile link included for recruiter networking.")
        else:
            strengths.append("LinkedIn profile reference identified in resume header.")

    if contact.get("github"):
        if contact.get("github_is_url"):
            strengths.append("GitHub profile link included to showcase software repositories.")
        else:
            strengths.append("GitHub profile reference identified in resume.")
        
    if action_count >= 5:
        strengths.append(f"Effective use of professional action verbs ({action_count} occurrences found).")
    if word_count >= 300:
        strengths.append("Sufficient text length and detail to describe achievements and technical experience.")
        
    if not strengths:
        strengths.append("Resume file parsed successfully and basic text content extracted.")

    # Evaluate Improvement Suggestions (avoid duplicate penalties)
    missing_core = []
    if not sections.get("Education"):
        missing_core.append("Education")
    if not sections.get("Technical Skills"):
        missing_core.append("Technical Skills")
    if not sections.get("Projects"):
        missing_core.append("Projects")
    if not (sections.get("Work Experience") or sections.get("Internships")):
        missing_core.append("Experience / Internships")
    if not sections.get("Career Objective"):
        missing_core.append("Professional Summary / Objective")

    if missing_core:
        suggestions.append(f"Add missing core sections: {', '.join(missing_core)}.")
        
    if len(skills_set) < 5:
        suggestions.append("Expand the Technical Skills section by listing specific programming languages, frameworks, or databases.")
        
    # Contact Suggestions
    if not contact.get("email"):
        suggestions.append("Ensure your email address is clearly present at the top of the resume.")
    if not contact.get("phone"):
        suggestions.append("Include a valid contact phone number in the header.")

    if not contact.get("linkedin"):
        suggestions.append("Include your LinkedIn profile URL in the contact header for recruiter networking.")
    elif not contact.get("linkedin_is_url"):
        suggestions.append("Convert your LinkedIn reference into a full clickable URL (e.g. https://linkedin.com/in/username) so recruiters can easily open it.")

    if not contact.get("github"):
        suggestions.append("Include your GitHub profile URL to showcase projects and code samples.")
    elif not contact.get("github_is_url"):
        suggestions.append("Include the full clickable URL for your GitHub profile (e.g. https://github.com/username).")
        
    if action_count < 5:
        suggestions.append("Begin project bullet points with strong action verbs like 'Developed', 'Designed', 'Automated', or 'Implemented'.")
        
    if word_count < 250:
        suggestions.append("Resume text is concise (under 250 words). Add details about project features, tools used, and measurable results.")
    elif word_count > 900:
        suggestions.append("Resume is long (over 900 words). Consider streamlining bullet points to highlight key achievements.")
        
    if not suggestions:
        suggestions.append("Resume structure and skill coverage look solid! Keep updating project outcomes regularly.")
        
    return strengths, suggestions
