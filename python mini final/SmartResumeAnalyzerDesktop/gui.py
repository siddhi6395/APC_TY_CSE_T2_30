"""
gui.py - Tkinter Desktop Application Interface Module
Contains main GUI window layout, navigation sidebar, canvas circular score indicator,
embedded Matplotlib charts, thread worker, dialogs, and results presentation.
(SYLLABUS CONCEPT: Unit 4 - Tkinter GUI Programming)
"""

import os
import re
import threading
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np
import pandas as pd

# Matplotlib integration with Tkinter
# (SYLLABUS CONCEPT: Unit 3 - Matplotlib & Tkinter Integration)
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from extractor import get_extractor
from analyzer import (
    clean_text, analyze_text_nltk, extract_contact_details,
    detect_sections, detect_skills, analyze_action_words, estimate_career_field
)
from scorer import compute_overall_score, generate_strengths_and_suggestions
import database
import report

# App Color Palette & Theme Definitions (White, Black & Grayscale)
COLOR_BG = "#f4f4f5"              # Clean neutral zinc light gray background
COLOR_SIDEBAR = "#09090b"         # Deep modern black sidebar
COLOR_SIDEBAR_ACTIVE = "#27272a"  # Dark zinc gray active item background
COLOR_SIDEBAR_TEXT = "#a1a1aa"    # Muted zinc gray text for sidebar items
COLOR_SIDEBAR_TEXT_ACTIVE = "#ffffff"  # Crisp white text for active item
COLOR_CARD_BG = "#ffffff"         # Pure white cards
COLOR_BORDER = "#e4e4e7"          # Subtle zinc border
COLOR_PRIMARY = "#18181b"         # Solid black/charcoal primary action color
COLOR_PRIMARY_HOVER = "#27272a"   # Dark charcoal hover state
COLOR_TEXT_DARK = "#09090b"       # Deep black text
COLOR_TEXT_MUTED = "#71717a"      # Neutral gray secondary text
COLOR_SUCCESS = "#18181b"         # Monochrome dark accent
COLOR_WARNING = "#52525b"         # Monochrome mid gray accent
COLOR_DANGER = "#09090b"          # Monochrome dark accent


class CircularScoreCanvas(tk.Canvas):
    """
    Custom Tkinter Canvas widget drawing a smooth circular score indicator.
    """
    def __init__(self, parent, size=150, score=0, **kwargs):
        super().__init__(parent, width=size, height=size, bg=COLOR_CARD_BG, highlightthickness=0, **kwargs)
        self.size = size
        self.score = score
        self.draw_score(score)

    def draw_score(self, score):
        self.delete("all")
        padding = 15
        width = 12
        x0 = padding
        y0 = padding
        x1 = self.size - padding
        y1 = self.size - padding
        
        # Background arc
        self.create_arc(x0, y0, x1, y1, start=0, extent=359.9, style=tk.ARC, outline="#e4e4e7", width=width)
        
        # Monochrome arc shade based on score
        if score >= 90:
            arc_color = "#09090b" # Deep black
        elif score >= 75:
            arc_color = "#27272a" # Dark charcoal
        elif score >= 60:
            arc_color = "#52525b" # Mid zinc gray
        else:
            arc_color = "#71717a" # Neutral gray
            
        # Filled score arc (start at 90 deg top, rotate clockwise)
        extent = -(score / 100.0) * 360.0
        self.create_arc(x0, y0, x1, y1, start=90, extent=extent, style=tk.ARC, outline=arc_color, width=width)
        
        # Score Text
        self.create_text(self.size/2, self.size/2 - 8, text=f"{score:.0f}", font=("Helvetica", 26, "bold"), fill=COLOR_TEXT_DARK)
        self.create_text(self.size/2, self.size/2 + 18, text="out of 100", font=("Helvetica", 9), fill=COLOR_TEXT_MUTED)


class SmartResumeApp:
    """
    Main Application Window Controller Class.
    (SYLLABUS CONCEPT: Unit 3 & 4 - OOP & Tkinter GUI Application)
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Resume Analyzer & Score Calculator")
        self.root.geometry("1150x750")
        self.root.minsize(950, 620)
        self.root.configure(bg=COLOR_BG)

        # Initialize SQLite database schema
        database.init_db()

        # State Variables
        self.selected_file_path = None
        self.current_analysis_record = None
        self.nav_buttons = {}

        # Setup TTK Styles
        self._setup_styles()

        # Main Layout Structure: Left Sidebar + Right Content Area
        self.main_container = tk.Frame(self.root, bg=COLOR_BG)
        self.main_container.pack(fill=tk.BOTH, expand=True)

        self._build_sidebar()
        
        # Content Container
        self.content_frame = tk.Frame(self.main_container, bg=COLOR_BG)
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Active Navigation View
        self.show_dashboard()

    def _setup_styles(self):
        """Configures clean TTK styling (SYLLABUS CONCEPT: Unit 4 - Tkinter ttk styling)"""
        style = ttk.Style()
        style.theme_use("clam")

        # Frame background
        style.configure("TFrame", background=COLOR_BG)
        style.configure("Card.TFrame", background=COLOR_CARD_BG, relief="flat")

        # Label styling
        style.configure("TLabel", background=COLOR_BG, foreground=COLOR_TEXT_DARK, font=("Helvetica", 10))
        style.configure("Header.TLabel", font=("Helvetica", 18, "bold"), foreground=COLOR_TEXT_DARK, background=COLOR_BG)
        style.configure("SubHeader.TLabel", font=("Helvetica", 12, "bold"), foreground=COLOR_TEXT_DARK, background=COLOR_BG)
        style.configure("Muted.TLabel", font=("Helvetica", 9), foreground=COLOR_TEXT_MUTED, background=COLOR_BG)

        # Progressbar
        style.configure("TProgressbar", thickness=10, troughcolor="#e4e4e7", background=COLOR_PRIMARY)

        # Buttons
        style.configure("Primary.TButton", font=("Helvetica", 10, "bold"), background=COLOR_PRIMARY, foreground="#ffffff", padding=8)
        style.map("Primary.TButton", background=[("active", COLOR_PRIMARY_HOVER)])
        
        # Treeview styling
        style.configure("Treeview", font=("Helvetica", 10), rowheight=26, background="#ffffff", fieldbackground="#ffffff", foreground=COLOR_TEXT_DARK)
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"), background="#f4f4f5", foreground=COLOR_TEXT_DARK)

    def _build_sidebar(self):
        """Builds navigation sidebar frame."""
        sidebar = tk.Frame(self.main_container, bg=COLOR_SIDEBAR, width=220)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)

        # Brand Header
        brand_frame = tk.Frame(sidebar, bg=COLOR_SIDEBAR, pady=20)
        brand_frame.pack(fill=tk.X)
        tk.Label(brand_frame, text="Smart Resume", font=("Helvetica", 15, "bold"), fg="#ffffff", bg=COLOR_SIDEBAR).pack()
        tk.Label(brand_frame, text="Analyzer & Scorer", font=("Helvetica", 10), fg="#a1a1aa", bg=COLOR_SIDEBAR).pack()

        tk.Frame(sidebar, bg="#27272a", height=1).pack(fill=tk.X, pady=10)

        # Navigation Items
        nav_items = [
            ("Dashboard", "dashboard", self.show_dashboard),
            ("Analyze Resume", "analyze", self.show_analyze_resume),
            ("Analysis History", "history", self.show_history)
        ]

        for label, key, cmd in nav_items:
            btn = tk.Button(
                sidebar,
                text=f"  {label}",
                font=("Helvetica", 11),
                anchor="w",
                bg=COLOR_SIDEBAR,
                fg=COLOR_SIDEBAR_TEXT,
                activebackground="#18181b",
                activeforeground="#ffffff",
                bd=0,
                padx=15,
                pady=10,
                command=cmd
            )
            btn.pack(fill=tk.X, pady=2)
            self.nav_buttons[key] = btn

    def _set_active_nav(self, active_key):
        """Highlights the active sidebar button (SYLLABUS CONCEPT: Unit 1 - Dictionary Iteration)"""
        for key, btn in self.nav_buttons.items():
            if key == active_key:
                btn.config(bg=COLOR_SIDEBAR_ACTIVE, fg=COLOR_SIDEBAR_TEXT_ACTIVE, font=("Helvetica", 11, "bold"))
            else:
                btn.config(bg=COLOR_SIDEBAR, fg=COLOR_SIDEBAR_TEXT, font=("Helvetica", 11))

    def clear_content_frame(self):
        """Removes existing content widgets before switching views."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    # =========================================================================
    # VIEW 1: DASHBOARD
    # =========================================================================
    def show_dashboard(self):
        self._set_active_nav("dashboard")
        self.clear_content_frame()

        # Dashboard Header
        header = tk.Frame(self.content_frame, bg=COLOR_BG)
        header.pack(fill=tk.X, pady=(0, 15))
        tk.Label(header, text="Dashboard", font=("Helvetica", 20, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_BG).pack(anchor="w")
        tk.Label(header, text="Welcome to Smart Resume Analyzer. Extract insights, calculate scores, and optimize resumes.", font=("Helvetica", 10), fg=COLOR_TEXT_MUTED, bg=COLOR_BG).pack(anchor="w")

        # Fetch SQLite Stats
        history_list = database.fetch_all_history()
        total_analyses = len(history_list)
        avg_score = np.mean([r["overall_score"] for r in history_list]) if total_analyses > 0 else 0.0
        
        # Most frequent field using Pandas / Counter (SYLLABUS CONCEPT: Unit 1 & 3 - Counter)
        fields = [r["career_field"] for r in history_list if r["career_field"] != "Other / Undetermined"]
        top_field = pd.Series(fields).mode()[0] if len(fields) > 0 else "N/A"

        # Stat Cards Container
        stats_frame = tk.Frame(self.content_frame, bg=COLOR_BG)
        stats_frame.pack(fill=tk.X, pady=(0, 20))

        # Helper function for stat cards
        def make_stat_card(parent, title, val_str, sub_text, color):
            card = tk.Frame(parent, bg=COLOR_CARD_BG, highlightbackground=COLOR_BORDER, highlightthickness=1, padx=20, pady=15)
            card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
            tk.Label(card, text=title, font=("Helvetica", 10, "bold"), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG).pack(anchor="w")
            tk.Label(card, text=val_str, font=("Helvetica", 22, "bold"), fg=color, bg=COLOR_CARD_BG).pack(anchor="w", pady=4)
            tk.Label(card, text=sub_text, font=("Helvetica", 8), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG).pack(anchor="w")

        make_stat_card(stats_frame, "Total Analyses", str(total_analyses), "Completed resume evaluations", COLOR_PRIMARY)
        make_stat_card(stats_frame, "Average Score", f"{avg_score:.1f} / 100", "Across all evaluated resumes", "#27272a")
        make_stat_card(stats_frame, "Top Career Field", top_field, "Most frequently detected field", "#52525b")

        # Quick Action Banner
        action_card = tk.Frame(self.content_frame, bg=COLOR_CARD_BG, highlightbackground=COLOR_BORDER, highlightthickness=1, padx=20, pady=15)
        action_card.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(action_card, text="Ready to evaluate a new resume?", font=("Helvetica", 12, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG).pack(side=tk.LEFT)
        btn_start = tk.Button(action_card, text="Analyze Resume Now", font=("Helvetica", 10, "bold"), bg=COLOR_PRIMARY, fg="#ffffff", activebackground=COLOR_PRIMARY_HOVER, bd=0, padx=15, pady=6, command=self.show_analyze_resume)
        btn_start.pack(side=tk.RIGHT)

        # Recent Analyses Table
        recent_frame = tk.Frame(self.content_frame, bg=COLOR_CARD_BG, highlightbackground=COLOR_BORDER, highlightthickness=1, padx=15, pady=15)
        recent_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(recent_frame, text="Recent Analysis Records", font=("Helvetica", 12, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG).pack(anchor="w", pady=(0, 10))

        if total_analyses == 0:
            empty_lbl = tk.Label(recent_frame, text="No resume analyses recorded yet.\nClick 'Analyze Resume Now' to evaluate your first resume file.", font=("Helvetica", 10), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG, pady=30)
            empty_lbl.pack()
        else:
            cols = ("ID", "Filename", "Date", "Score", "Grade", "Career Field")
            tree = ttk.Treeview(recent_frame, columns=cols, show="headings", height=6)
            for c in cols:
                tree.heading(c, text=c)
            tree.column("ID", width=40, anchor="center")
            tree.column("Filename", width=220, anchor="w")
            tree.column("Date", width=140, anchor="center")
            tree.column("Score", width=80, anchor="center")
            tree.column("Grade", width=110, anchor="center")
            tree.column("Career Field", width=180, anchor="w")

            for r in history_list[:5]:
                tree.insert("", tk.END, values=(r["id"], r["filename"], r["analysis_date"], f"{r['overall_score']:.1f}", r["grade"], r["career_field"]))
            tree.pack(fill=tk.BOTH, expand=True)

    # =========================================================================
    # VIEW 2: ANALYZE RESUME (UPLOAD)
    # =========================================================================
    def show_analyze_resume(self):
        self._set_active_nav("analyze")
        self.clear_content_frame()

        header = tk.Frame(self.content_frame, bg=COLOR_BG)
        header.pack(fill=tk.X, pady=(0, 15))
        tk.Label(header, text="Analyze Resume", font=("Helvetica", 20, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_BG).pack(anchor="w")
        tk.Label(header, text="Select a PDF, Word DOCX, or Image resume file to analyze.", font=("Helvetica", 10), fg=COLOR_TEXT_MUTED, bg=COLOR_BG).pack(anchor="w")

        # File Selection Card
        card = tk.Frame(self.content_frame, bg=COLOR_CARD_BG, highlightbackground=COLOR_BORDER, highlightthickness=1, padx=30, pady=30)
        card.pack(fill=tk.X, pady=10)

        tk.Label(card, text="Select Resume File", font=("Helvetica", 14, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG).pack(anchor="w")
        tk.Label(card, text="Supported Formats: PDF, DOCX, JPG, JPEG, PNG (Max File Size: 5 MB)", font=("Helvetica", 9), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG).pack(anchor="w", pady=(2, 15))

        btn_select = tk.Button(
            card,
            text="📁  Choose Resume File",
            font=("Helvetica", 11, "bold"),
            bg="#ffffff",
            fg=COLOR_TEXT_DARK,
            activebackground="#f4f4f5",
            bd=1,
            relief="solid",
            padx=20,
            pady=10,
            command=self._on_choose_file
        )
        btn_select.pack(anchor="w", pady=(0, 15))

        # File Info Label Frame
        self.file_info_frame = tk.Frame(card, bg="#fafafa", highlightbackground=COLOR_BORDER, highlightthickness=1, padx=15, pady=12)
        
        self.lbl_filename = tk.Label(self.file_info_frame, text="No file selected", font=("Helvetica", 10, "bold"), fg=COLOR_TEXT_DARK, bg="#fafafa")
        self.lbl_filename.pack(anchor="w")
        
        self.lbl_filedetails = tk.Label(self.file_info_frame, text="Please select a valid resume document to begin.", font=("Helvetica", 9), fg=COLOR_TEXT_MUTED, bg="#fafafa")
        self.lbl_filedetails.pack(anchor="w")

        # Status & Action Buttons
        self.action_frame = tk.Frame(card, bg=COLOR_CARD_BG)
        self.action_frame.pack(fill=tk.X, pady=(20, 0))

        self.btn_analyze = tk.Button(
            self.action_frame,
            text="⚡ Start Resume Analysis",
            font=("Helvetica", 11, "bold"),
            bg=COLOR_PRIMARY,
            fg="#ffffff",
            activebackground=COLOR_PRIMARY_HOVER,
            bd=0,
            padx=25,
            pady=10,
            state=tk.DISABLED,
            command=self._start_analysis_thread
        )
        self.btn_analyze.pack(side=tk.LEFT)

        self.btn_clear_file = tk.Button(
            self.action_frame,
            text="Remove File",
            font=("Helvetica", 10),
            bg=COLOR_CARD_BG,
            fg=COLOR_TEXT_MUTED,
            bd=0,
            padx=15,
            command=self._clear_selected_file
        )

        # Loading / Progress Indicator
        self.progress_frame = tk.Frame(card, bg=COLOR_CARD_BG)
        self.lbl_progress = tk.Label(self.progress_frame, text="Extracting and analyzing resume text...", font=("Helvetica", 10, "bold"), fg=COLOR_PRIMARY, bg=COLOR_CARD_BG)
        self.lbl_progress.pack(anchor="w", pady=(0, 5))
        self.progressbar = ttk.Progressbar(self.progress_frame, mode="indeterminate", length=400)
        self.progressbar.pack(anchor="w")

    def _on_choose_file(self):
        """Native file dialog picker (SYLLABUS CONCEPT: Unit 4 - Native Dialogs)"""
        filetypes = [
            ("All Supported Resumes", "*.pdf;*.docx;*.doc;*.jpg;*.jpeg;*.png"),
            ("PDF Documents (*.pdf)", "*.pdf"),
            ("Word Documents (*.docx)", "*.docx"),
            ("Image Files (*.jpg, *.png)", "*.jpg;*.jpeg;*.png")
        ]
        chosen = filedialog.askopenfilename(title="Select Resume File", filetypes=filetypes)
        if chosen:
            # Validate File Size (Max 5 MB)
            file_size_mb = os.path.getsize(chosen) / (1024 * 1024)
            if file_size_mb > 5.0:
                messagebox.showerror("File Size Error", f"The selected file size ({file_size_mb:.2f} MB) exceeds the maximum allowed limit of 5.0 MB.")
                return

            self.selected_file_path = chosen
            ext = Path(chosen).suffix.upper().replace('.', '')
            self.file_info_frame.pack(fill=tk.X, pady=(0, 15))
            self.lbl_filename.config(text=os.path.basename(chosen))
            self.lbl_filedetails.config(text=f"Format: {ext}  •  File Size: {file_size_mb:.2f} MB  •  Status: Ready to Analyze")
            
            self.btn_analyze.config(state=tk.NORMAL)
            self.btn_clear_file.pack(side=tk.LEFT, padx=10)

    def _clear_selected_file(self):
        """Clears current selection."""
        self.selected_file_path = None
        self.file_info_frame.pack_forget()
        self.btn_analyze.config(state=tk.DISABLED)
        self.btn_clear_file.pack_forget()

    def _start_analysis_thread(self):
        """
        Launches background thread for non-blocking extraction and processing.
        (SYLLABUS CONCEPT: Unit 4 - Threading in GUI Applications)
        """
        if not self.selected_file_path:
            return

        self.btn_analyze.config(state=tk.DISABLED)
        self.progress_frame.pack(fill=tk.X, pady=15)
        self.progressbar.start(10)

        # Worker thread execution
        thread = threading.Thread(target=self._run_resume_analysis, daemon=True)
        thread.start()

    def _run_resume_analysis(self):
        """Core analysis pipeline execution in background thread."""
        try:
            file_path = self.selected_file_path
            filename = os.path.basename(file_path)

            # Step 1: Text Extraction (Polymorphism)
            extractor = get_extractor(file_path)
            raw_text = extractor.extract_text()
            cleaned = clean_text(raw_text)

            if not cleaned or len(cleaned.strip()) < 15:
                raise ValueError("No readable text could be extracted from the selected resume file.\nEnsure the document is not empty or password-protected.")

            # Step 2: NLTK Tokenization & Word Frequency
            tokens, words, freq_dist, top_words = analyze_text_nltk(cleaned)
            word_count = len(re.findall(r'\b\w+\b', cleaned))
            char_count = len(cleaned)

            # Step 3: Feature Detection
            contact = extract_contact_details(cleaned)
            sections = detect_sections(cleaned)
            skills_by_category, skills_set = detect_skills(cleaned)
            found_action_words, action_count = analyze_action_words(cleaned)
            career_field, field_scores = estimate_career_field(cleaned, skills_set)

            analysis_data = {
                "filename": filename,
                "sections": sections,
                "skills_set": skills_set,
                "skills_by_category": skills_by_category,
                "contact": contact,
                "action_count": action_count,
                "found_action_words": found_action_words,
                "word_count": word_count,
                "char_count": char_count,
                "skills_count": len(skills_set),
                "career_field": career_field
            }

            # Step 4: Transparent Score Calculation & Suggestions
            breakdown, df_breakdown = compute_overall_score(analysis_data)
            strengths, suggestions = generate_strengths_and_suggestions(analysis_data, breakdown)

            record_data = {
                "filename": filename,
                "overall_score": breakdown["total_score"],
                "grade": breakdown["grade"],
                "career_field": career_field,
                "word_count": word_count,
                "char_count": char_count,
                "skills_count": len(skills_set),
                "sections": sections,
                "skills_by_category": skills_by_category,
                "contact": contact,
                "breakdown": breakdown,
                "strengths": strengths,
                "suggestions": suggestions
            }

            # Step 5: Save record to SQLite
            record_id = database.save_analysis_record(record_data)
            full_record = database.fetch_record_by_id(record_id)

            # Thread-safe GUI callback update
            target_record = full_record
            self.root.after(0, lambda r=target_record: self._on_analysis_complete(r))

        except Exception as err:
            err_msg = str(err)
            self.root.after(0, lambda msg=err_msg: self._on_analysis_error(msg))

    def _on_analysis_complete(self, record):
        """Callback executed on main thread after analysis finishes."""
        self.progressbar.stop()
        self.progress_frame.pack_forget()
        self.current_analysis_record = record
        self.show_results_view(record)

    def _on_analysis_error(self, error_msg):
        """Callback executed on main thread if error occurs."""
        self.progressbar.stop()
        self.progress_frame.pack_forget()
        self.btn_analyze.config(state=tk.NORMAL)
        messagebox.showerror("Analysis Error", f"An error occurred during resume processing:\n\n{error_msg}")

    # =========================================================================
    # VIEW 3: RESULTS PRESENTATION SCREEN
    # =========================================================================
    def show_results_view(self, record):
        self._set_active_nav("analyze")
        self.clear_content_frame()

        # Canvas Scrollable Container for Results Screen
        canvas = tk.Canvas(self.content_frame, bg=COLOR_BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.content_frame, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg=COLOR_BG)

        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas_window = canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(canvas_window, width=e.width))
        canvas.configure(yscrollcommand=scrollbar.set)

        def _on_results_mw(event):
            try:
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            except Exception:
                pass

        canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_results_mw))
        canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Header Bar
        header = tk.Frame(scroll_frame, bg=COLOR_BG)
        header.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(header, text="Resume Analysis Results", font=("Helvetica", 18, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_BG).pack(anchor="w")
        tk.Label(
            header,
            text=f"Filename: {record['filename']}  •  Evaluated: {record['analysis_date']}  •  Estimated Field: {record['career_field']}",
            font=("Helvetica", 10),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_BG
        ).pack(anchor="w")

        # Top Split Row: Score Indicator & Embedded Matplotlib Chart
        top_row = tk.Frame(scroll_frame, bg=COLOR_BG)
        top_row.pack(fill=tk.X, pady=(0, 15))

        # Left Score Card
        score_card = tk.Frame(top_row, bg=COLOR_CARD_BG, highlightbackground=COLOR_BORDER, highlightthickness=1, padx=20, pady=15)
        score_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        tk.Label(score_card, text="Overall Score", font=("Helvetica", 12, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG).pack()
        
        # Circular Score Canvas Widget
        score_canvas = CircularScoreCanvas(score_card, size=140, score=record['overall_score'])
        score_canvas.pack(pady=5)

        # Grade Tag
        grade_lbl = tk.Label(score_card, text=f"Rating: {record['grade']}", font=("Helvetica", 11, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG)
        grade_lbl.pack()
        
        disclaimer_lbl = tk.Label(
            score_card,
            text="* Disclaimer: Rule-based score out of 100\nestimating content quality & structure.",
            font=("Helvetica", 8),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG,
            justify="center"
        )
        disclaimer_lbl.pack(pady=(5, 0))

        # Right Chart Card (Matplotlib Integration - Colorful Donut / Pie Chart)
        chart_card = tk.Frame(top_row, bg=COLOR_CARD_BG, highlightbackground=COLOR_BORDER, highlightthickness=1, padx=10, pady=10)
        chart_card.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        breakdown = record['breakdown']
        categories = breakdown['categories']
        earned = breakdown['earned']
        max_pts = breakdown['max']

        # Embed Matplotlib Pie Chart with distinct vibrant colors
        try:
            fig = Figure(figsize=(5.4, 2.7), dpi=90, facecolor=COLOR_CARD_BG)
            ax = fig.add_subplot(111)
            
            short_cats = ["Structure", "Skills", "Proj & Exp", "Contact", "Action Wds", "Keywords", "Readability"]
            pie_colors = ['#2563eb', '#10b981', '#f59e0b', '#8b5cf6', '#ec4899', '#06b6d4', '#f97316']
            
            plot_labels = []
            plot_values = []
            plot_colors = []
            
            for cat, val, col in zip(short_cats, earned, pie_colors):
                if val > 0:
                    plot_labels.append(f"{cat} ({val:.1f} pts)")
                    plot_values.append(val)
                    plot_colors.append(col)

            if not plot_values or sum(plot_values) == 0:
                plot_labels = [f"{cat} ({m:.0f} pts)" for cat, m in zip(short_cats, max_pts)]
                plot_values = max_pts
                plot_colors = pie_colors

            wedges, texts, autotexts = ax.pie(
                plot_values,
                autopct='%1.0f%%',
                pctdistance=0.75,
                colors=plot_colors,
                startangle=140,
                wedgeprops=dict(width=0.55, edgecolor='white', linewidth=2)
            )
            
            for at in autotexts:
                at.set_fontsize(7.5)
                at.set_color('white')
                at.set_weight('bold')

            ax.legend(
                wedges,
                plot_labels,
                title="Categories",
                loc="center left",
                bbox_to_anchor=(1, 0, 0.5, 1),
                fontsize=7.5,
                title_fontsize=8
            )
            ax.set_title('Category Points Distribution', fontsize=9.5, fontweight='bold', color=COLOR_TEXT_DARK)
            fig.subplots_adjust(left=0.05, right=0.60, top=0.88, bottom=0.08)

            chart_widget = FigureCanvasTkAgg(fig, master=chart_card).get_tk_widget()
            chart_widget.pack(fill=tk.BOTH, expand=True)
        except Exception:
            tk.Label(chart_card, text="[Score breakdown chart display unavailable]", bg=COLOR_CARD_BG, fg=COLOR_TEXT_MUTED).pack()

        # Quick Statistics Strip
        stats_strip = tk.Frame(scroll_frame, bg=COLOR_CARD_BG, highlightbackground=COLOR_BORDER, highlightthickness=1, padx=15, pady=10)
        stats_strip.pack(fill=tk.X, pady=(0, 15))

        stat_items = [
            ("Word Count", record['word_count']),
            ("Character Count", record['char_count']),
            ("Technical Skills", record['skills_count']),
            ("Sections Detected", f"{sum(1 for v in record['sections'].values() if v)} / {len(record['sections'])}")
        ]

        for label, val in stat_items:
            f = tk.Frame(stats_strip, bg=COLOR_CARD_BG)
            f.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            tk.Label(f, text=label, font=("Helvetica", 8), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG).pack()
            tk.Label(f, text=str(val), font=("Helvetica", 12, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG).pack()

        # Middle Row: Score Breakdown Table & Contact Information
        mid_row = tk.Frame(scroll_frame, bg=COLOR_BG)
        mid_row.pack(fill=tk.X, pady=(0, 15))

        # Table Breakdown Card
        table_card = tk.Frame(mid_row, bg=COLOR_CARD_BG, highlightbackground=COLOR_BORDER, highlightthickness=1, padx=15, pady=15)
        table_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        tk.Label(table_card, text="Category Score Table", font=("Helvetica", 11, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG).pack(anchor="w", pady=(0, 10))

        tree_cols = ("Category", "Earned", "Max", "Percentage")
        tbl = ttk.Treeview(table_card, columns=tree_cols, show="headings", height=7)
        for c in tree_cols:
            tbl.heading(c, text=c)
        tbl.column("Category", width=170, anchor="w")
        tbl.column("Earned", width=65, anchor="center")
        tbl.column("Max", width=65, anchor="center")
        tbl.column("Percentage", width=85, anchor="center")

        percentages = breakdown['percentage']
        for cat, e, m, p in zip(categories, earned, max_pts, percentages):
            tbl.insert("", tk.END, values=(cat, f"{e:.1f}", f"{m:.1f}", f"{p}%"))
        tbl.pack(fill=tk.BOTH, expand=True)

        # Contact Details Status Card
        contact_card = tk.Frame(mid_row, bg=COLOR_CARD_BG, highlightbackground=COLOR_BORDER, highlightthickness=1, padx=15, pady=15, width=280)
        contact_card.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(contact_card, text="Contact Details Status", font=("Helvetica", 11, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG).pack(anchor="w", pady=(0, 10))

        contact = record['contact']
        c_items = [
            ("Email", contact.get("email")),
            ("Phone", contact.get("phone")),
            ("LinkedIn", contact.get("linkedin")),
            ("GitHub", contact.get("github"))
        ]

        for lbl_name, val in c_items:
            cf = tk.Frame(contact_card, bg=COLOR_CARD_BG, pady=4)
            cf.pack(fill=tk.X)
            tk.Label(cf, text=f"{lbl_name}:", font=("Helvetica", 10, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG).pack(side=tk.LEFT)
            if val:
                if lbl_name == "LinkedIn":
                    tag = "  [VERIFIED URL]" if contact.get("linkedin_is_url") else "  [PROFILE REF]"
                elif lbl_name == "GitHub":
                    tag = "  [VERIFIED URL]" if contact.get("github_is_url") else "  [PROFILE REF]"
                else:
                    tag = "  [FOUND]"
                tk.Label(cf, text=tag, font=("Helvetica", 9, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG).pack(side=tk.RIGHT)
            else:
                tk.Label(cf, text="  [MISSING]", font=("Helvetica", 9, "bold"), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG).pack(side=tk.RIGHT)

        # Technical Skills & Resume Sections Row
        sec_row = tk.Frame(scroll_frame, bg=COLOR_BG)
        sec_row.pack(fill=tk.X, pady=(0, 15))

        # Detected Skills Box
        skills_card = tk.Frame(sec_row, bg=COLOR_CARD_BG, highlightbackground=COLOR_BORDER, highlightthickness=1, padx=15, pady=15)
        skills_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        tk.Label(skills_card, text="Detected Technical Skills", font=("Helvetica", 11, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG).pack(anchor="w", pady=(0, 8))

        skills_by_cat = record['skills_by_category']
        has_any_skills = False
        for cat_name, s_list in skills_by_cat.items():
            if s_list:
                has_any_skills = True
                f = tk.Frame(skills_card, bg=COLOR_CARD_BG, pady=2)
                f.pack(fill=tk.X, anchor="w")
                tk.Label(f, text=f"{cat_name}: ", font=("Helvetica", 9, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG).pack(side=tk.LEFT)
                tk.Label(f, text=", ".join(s_list), font=("Helvetica", 9), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG, wraplength=350, justify="left").pack(side=tk.LEFT)

        if not has_any_skills:
            tk.Label(skills_card, text="No standard technical skills detected.", font=("Helvetica", 9), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG).pack(anchor="w")

        # Sections Status Box
        sections_card = tk.Frame(sec_row, bg=COLOR_CARD_BG, highlightbackground=COLOR_BORDER, highlightthickness=1, padx=15, pady=15, width=280)
        sections_card.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(sections_card, text="Resume Sections Grid", font=("Helvetica", 11, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG).pack(anchor="w", pady=(0, 8))

        sections = record['sections']
        for sec_name, present in sections.items():
            f = tk.Frame(sections_card, bg=COLOR_CARD_BG, pady=1)
            f.pack(fill=tk.X)
            tk.Label(f, text=sec_name, font=("Helvetica", 8), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG).pack(side=tk.LEFT)
            tag_color = COLOR_TEXT_DARK if present else COLOR_TEXT_MUTED
            tag_text = "✓" if present else "✗"
            tk.Label(f, text=tag_text, font=("Helvetica", 8, "bold"), fg=tag_color, bg=COLOR_CARD_BG).pack(side=tk.RIGHT)

        # Strengths & Suggestions Cards
        feedback_row = tk.Frame(scroll_frame, bg=COLOR_BG)
        feedback_row.pack(fill=tk.X, pady=(0, 20))

        # Strengths Card
        str_card = tk.Frame(feedback_row, bg=COLOR_CARD_BG, highlightbackground=COLOR_BORDER, highlightthickness=1, padx=15, pady=15)
        str_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        tk.Label(str_card, text="Key Strengths", font=("Helvetica", 11, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG).pack(anchor="w", pady=(0, 5))
        for item in record['strengths']:
            tk.Label(str_card, text=f"•  {item}", font=("Helvetica", 9), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG, wraplength=400, justify="left").pack(anchor="w", pady=2)

        # Suggestions Card
        sug_card = tk.Frame(feedback_row, bg=COLOR_CARD_BG, highlightbackground=COLOR_BORDER, highlightthickness=1, padx=15, pady=15)
        sug_card.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tk.Label(sug_card, text="Actionable Suggestions", font=("Helvetica", 11, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG).pack(anchor="w", pady=(0, 5))
        for item in record['suggestions']:
            tk.Label(sug_card, text=f"•  {item}", font=("Helvetica", 9), fg=COLOR_TEXT_DARK, bg=COLOR_CARD_BG, wraplength=400, justify="left").pack(anchor="w", pady=2)

        # Bottom Action Bar
        btn_bar = tk.Frame(scroll_frame, bg=COLOR_BG, pady=10)
        btn_bar.pack(fill=tk.X)

        btn_export = tk.Button(
            btn_bar,
            text="💾 Export Full Report (.txt)",
            font=("Helvetica", 10, "bold"),
            bg=COLOR_PRIMARY,
            fg="#ffffff",
            activebackground=COLOR_PRIMARY_HOVER,
            bd=0,
            padx=15,
            pady=8,
            command=lambda r=record: self._export_report(r)
        )
        btn_export.pack(side=tk.LEFT, padx=(0, 10))

        btn_another = tk.Button(
            btn_bar,
            text="Analyze Another Resume",
            font=("Helvetica", 10),
            bg="#ffffff",
            fg=COLOR_TEXT_DARK,
            bd=1,
            relief="solid",
            padx=15,
            pady=8,
            command=self.show_analyze_resume
        )
        btn_another.pack(side=tk.LEFT)

        btn_dash = tk.Button(
            btn_bar,
            text="Return to Dashboard",
            font=("Helvetica", 10),
            bg=COLOR_BG,
            fg=COLOR_TEXT_MUTED,
            bd=0,
            padx=15,
            command=self.show_dashboard
        )
        btn_dash.pack(side=tk.RIGHT)

    def _export_report(self, record):
        """Native Save As Dialog to export report (SYLLABUS CONCEPT: Unit 2 & 4 - File Dialog Export)"""
        default_name = f"Resume_Report_{Path(record['filename']).stem}.txt"
        save_path = filedialog.asksaveasfilename(
            title="Save Resume Analysis Report",
            initialfile=default_name,
            defaultextension=".txt",
            filetypes=[("Text Files (*.txt)", "*.txt"), ("All Files", "*.*")]
        )
        if save_path:
            try:
                report.save_report_to_file(record, save_path)
                messagebox.showinfo("Export Successful", f"Analysis report exported successfully to:\n\n{save_path}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to save report file:\n{str(e)}")

    # =========================================================================
    # VIEW 4: ANALYSIS HISTORY
    # =========================================================================
    def show_history(self):
        self._set_active_nav("history")
        self.clear_content_frame()

        header = tk.Frame(self.content_frame, bg=COLOR_BG)
        header.pack(fill=tk.X, pady=(0, 15))
        tk.Label(header, text="Analysis History", font=("Helvetica", 20, "bold"), fg=COLOR_TEXT_DARK, bg=COLOR_BG).pack(anchor="w")
        tk.Label(header, text="View and manage previously evaluated resume reports stored in SQLite.", font=("Helvetica", 10), fg=COLOR_TEXT_MUTED, bg=COLOR_BG).pack(anchor="w")

        # History Table Container
        table_card = tk.Frame(self.content_frame, bg=COLOR_CARD_BG, highlightbackground=COLOR_BORDER, highlightthickness=1, padx=15, pady=15)
        table_card.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        history_list = database.fetch_all_history()

        if not history_list:
            tk.Label(table_card, text="No analysis records found in database history.", font=("Helvetica", 11), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG, pady=40).pack()
        else:
            cols = ("ID", "Filename", "Date & Time", "Overall Score", "Grade", "Career Field", "Skills Found")
            tree = ttk.Treeview(table_card, columns=cols, show="headings")
            for c in cols:
                tree.heading(c, text=c)
            tree.column("ID", width=45, anchor="center")
            tree.column("Filename", width=200, anchor="w")
            tree.column("Date & Time", width=140, anchor="center")
            tree.column("Overall Score", width=95, anchor="center")
            tree.column("Grade", width=110, anchor="center")
            tree.column("Career Field", width=170, anchor="w")
            tree.column("Skills Found", width=90, anchor="center")

            for r in history_list:
                tree.insert("", tk.END, values=(r["id"], r["filename"], r["analysis_date"], f"{r['overall_score']:.1f}", r["grade"], r["career_field"], r["skills_count"]))
            
            scrollbar = ttk.Scrollbar(table_card, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)
            
            tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            # Action Buttons Bar
            action_bar = tk.Frame(self.content_frame, bg=COLOR_BG)
            action_bar.pack(fill=tk.X)

            btn_view = tk.Button(
                action_bar,
                text="👁️ View Selected Report",
                font=("Helvetica", 10, "bold"),
                bg=COLOR_PRIMARY,
                fg="#ffffff",
                activebackground=COLOR_PRIMARY_HOVER,
                bd=0,
                padx=15,
                pady=8,
                command=lambda t=tree: self._view_selected_history(t)
            )
            btn_view.pack(side=tk.LEFT, padx=(0, 10))

            btn_delete = tk.Button(
                action_bar,
                text="🗑️ Delete Record",
                font=("Helvetica", 10),
                bg="#ffffff",
                fg=COLOR_TEXT_DARK,
                bd=1,
                relief="solid",
                padx=15,
                pady=8,
                command=lambda t=tree: self._delete_selected_history(t)
            )
            btn_delete.pack(side=tk.LEFT)

            btn_clear = tk.Button(
                action_bar,
                text="Clear All History",
                font=("Helvetica", 10),
                bg=COLOR_BG,
                fg=COLOR_TEXT_MUTED,
                bd=0,
                padx=15,
                command=self._clear_all_history_dialog
            )
            btn_clear.pack(side=tk.RIGHT)

    def _view_selected_history(self, tree):
        """Reopens full analysis report from SQLite (SYLLABUS CONCEPT: Unit 2 - SQLite Select)"""
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Select Record", "Please select a record from the history table to view.")
            return

        item = tree.item(selected[0])
        record_id = item["values"][0]
        full_record = database.fetch_record_by_id(record_id)
        if full_record:
            self.show_results_view(full_record)

    def _delete_selected_history(self, tree):
        """Deletes single record from database."""
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Select Record", "Please select a record from the history table to delete.")
            return

        item = tree.item(selected[0])
        record_id = item["values"][0]
        database.delete_record_by_id(record_id)
        self.show_history()

    def _clear_all_history_dialog(self):
        """Confirmation dialog before clearing all history."""
        confirm = messagebox.askyesno("Confirm Clear History", "Are you sure you want to delete ALL past analysis records from the SQLite database?\nThis action cannot be undone.")
        if confirm:
            database.clear_all_history()
            self.show_history()

