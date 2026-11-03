"""
main.py - Smart Resume Analyzer & Score Calculator Entry Point
Initializes Tkinter root window and launches the desktop application.
(SYLLABUS CONCEPT: Unit 4 - Application Entry Point)
"""

import sys
import os
import tkinter as tk
from gui import SmartResumeApp


def main():
    """Main application execution function."""
    root = tk.Tk()
    
    # Configure high-DPI scaling awareness on Windows if available
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass

    app = SmartResumeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
