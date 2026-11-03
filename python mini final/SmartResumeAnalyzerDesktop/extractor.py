"""
extractor.py - Resume File Text Extraction Module
Demonstrates OOP concepts: Abstract Base Classes, Inheritance, and Polymorphism.
(SYLLABUS CONCEPT: Unit 3 - OOP in Python)
"""

import os
from abc import ABC, abstractmethod
from pathlib import Path
import pypdf
import docx
from PIL import Image
import pytesseract

# Configure common default installation paths for Tesseract OCR on Windows
TESSERACT_COMMON_PATHS = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    os.path.expanduser(r"~\AppData\Local\Programs\Tesseract-OCR\tesseract.exe")
]

for tpath in TESSERACT_COMMON_PATHS:
    if os.path.exists(tpath):
        pytesseract.pytesseract.tesseract_cmd = tpath
        break


class ResumeExtractor(ABC):
    """
    Abstract Base Class for all resume text extractors.
    (SYLLABUS CONCEPT: Unit 3 - OOP Abstraction & Base Class)
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.file_ext = Path(file_path).suffix.lower()

    @abstractmethod
    def extract_text(self) -> str:
        """
        Abstract method to extract text from a file. Must be overridden by subclasses.
        (SYLLABUS CONCEPT: Unit 3 - Polymorphism)
        """
        pass


class PDFExtractor(ResumeExtractor):
    """
    PDF file text extractor using pypdf library.
    Extracts text using layout-aware mode to prevent character splitting
    and inspects hyperlink annotations for profile URLs.
    (SYLLABUS CONCEPT: Unit 3 - Inheritance & Module Usage)
    """
    @staticmethod
    def _repair_spaced_chars(text: str) -> str:
        """
        Repairs text where characters were erroneously extracted one per line.
        """
        lines = text.splitlines()
        non_empty = [l.strip() for l in lines if l.strip()]
        if len(non_empty) > 15 and (sum(1 for l in non_empty if len(l) == 1) / len(non_empty)) > 0.45:
            reconstructed_lines = []
            curr_tokens = []
            for line in lines:
                stripped = line.strip()
                if len(stripped) == 1:
                    curr_tokens.append(stripped)
                elif len(stripped) == 0:
                    if curr_tokens:
                        reconstructed_lines.append("".join(curr_tokens))
                        curr_tokens = []
                    reconstructed_lines.append("")
                else:
                    if curr_tokens:
                        reconstructed_lines.append("".join(curr_tokens))
                        curr_tokens = []
                    reconstructed_lines.append(stripped)
            if curr_tokens:
                reconstructed_lines.append("".join(curr_tokens))
            return "\n".join(reconstructed_lines)
        return text

    def extract_text(self) -> str:
        text = ""
        hyperlinks = []
        try:
            reader = pypdf.PdfReader(self.file_path)
            for page in reader.pages:
                # 1. Inspect PDF hyperlink annotations for profile URLs
                if "/Annots" in page:
                    try:
                        annots = page["/Annots"]
                        for annot in annots:
                            obj = annot.get_object() if hasattr(annot, "get_object") else annot
                            if obj and obj.get("/Subtype") == "/Link":
                                action = obj.get("/A")
                                if action and "/URI" in action:
                                    uri = str(action["/URI"]).strip()
                                    if uri and uri not in hyperlinks:
                                        hyperlinks.append(uri)
                    except Exception:
                        pass

                # 2. Extract page text using layout mode (preserves lines and spaces)
                page_text = ""
                try:
                    page_text = page.extract_text(extraction_mode="layout") or ""
                except Exception:
                    page_text = ""

                # Fallback to standard plain extraction if layout mode yielded nothing
                if not page_text or not page_text.strip():
                    try:
                        page_text = page.extract_text() or ""
                    except Exception:
                        page_text = ""

                # Repair single-character-per-line artifact if present
                page_text = self._repair_spaced_chars(page_text)

                if page_text:
                    text += page_text + "\n"

            # 3. Append discovered hyperlinks if not already in extracted text
            if hyperlinks:
                missing_links = [link for link in hyperlinks if link.lower() not in text.lower()]
                if missing_links:
                    text += "\n\nDetected Hyperlinks:\n" + "\n".join(missing_links)

        except Exception as e:
            raise ValueError(f"Failed to extract text from PDF file: {str(e)}")

        return text.strip()


class DOCXExtractor(ResumeExtractor):
    """
    Word document extractor using python-docx library.
    Extracts paragraphs, table cells, and document hyperlink relationships.
    (SYLLABUS CONCEPT: Unit 3 - Inheritance)
    """
    def extract_text(self) -> str:
        text_lines = []
        doc_links = []
        try:
            doc = docx.Document(self.file_path)
            # Extract paragraph text
            for paragraph in doc.paragraphs:
                if paragraph.text.strip():
                    text_lines.append(paragraph.text.strip())
            # Extract table cell text
            for table in doc.tables:
                for row in table.rows:
                    row_text = " | ".join(cell.text.strip() for cell in row.cells if cell.text.strip())
                    if row_text:
                        text_lines.append(row_text)
            # Extract embedded hyperlink URLs
            try:
                for rel in doc.part.rels.values():
                    if "hyperlink" in getattr(rel, "reltype", ""):
                        target = getattr(rel, "target_ref", "")
                        if target and target.startswith(("http://", "https://", "mailto:")):
                            if target not in doc_links:
                                doc_links.append(target)
            except Exception:
                pass

            if doc_links:
                combined_text = "\n".join(text_lines)
                missing_docx_links = [l for l in doc_links if l.lower() not in combined_text.lower()]
                if missing_docx_links:
                    text_lines.append("\nDetected Hyperlinks:")
                    text_lines.extend(missing_docx_links)

        except Exception as e:
            raise ValueError(f"Failed to extract text from Word DOCX file: {str(e)}")

        return "\n".join(text_lines)


class ImageExtractor(ResumeExtractor):
    """
    Image file OCR extractor using Pillow and pytesseract.
    (SYLLABUS CONCEPT: Unit 3 - Inheritance & Error Handling)
    """
    def extract_text(self) -> str:
        try:
            image = Image.open(self.file_path)
            text = pytesseract.image_to_string(image)
            return text.strip()
        except pytesseract.TesseractNotFoundError:
            raise RuntimeError(
                "Tesseract OCR engine is not installed or not found on system PATH.\n"
                "To enable image OCR, please install Tesseract OCR on Windows\n"
                "or analyze a PDF / Word DOCX resume file."
            )
        except Exception as e:
            raise ValueError(f"Failed to perform OCR on image file: {str(e)}")


def get_extractor(file_path: str) -> ResumeExtractor:
    """
    Factory function demonstrating polymorphism. Returns appropriate subclass instance based on file extension.
    (SYLLABUS CONCEPT: Unit 1 & 3 - Functions & Polymorphism)
    """
    ext = Path(file_path).suffix.lower()
    if ext == '.pdf':
        return PDFExtractor(file_path)
    elif ext in ['.docx', '.doc']:
        return DOCXExtractor(file_path)
    elif ext in ['.jpg', '.jpeg', '.png']:
        return ImageExtractor(file_path)
    else:
        raise ValueError(f"Unsupported file format '{ext}'. Supported formats: PDF, DOCX, JPG, JPEG, PNG.")
