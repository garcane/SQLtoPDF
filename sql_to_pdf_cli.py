import os
import chardet
from tkinter import Tk, filedialog
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def detect_encoding(file_path):
    """Detect file encoding automatically."""
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding'] or 'utf-8'


def sql_to_pdf(sql_file, pdf_file, encoding="utf-8"):
    """Convert a single SQL file to PDF."""
    with open(sql_file, 'r', encoding=encoding, errors='ignore') as f:
        sql_content = f.read()

    doc = SimpleDocTemplate(pdf_file, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    for line in sql_content.split("\n"):
        story.append(Paragraph(line.replace(" ", "&nbsp;"), styles['Normal']))
        story.append(Spacer(1, 4))

    doc.build(story)


def merge_sql_to_pdf(sql_files, output_pdf, encoding="utf-8"):
    """Merge multiple SQL files into one PDF."""
    doc = SimpleDocTemplate(output_pdf, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    for sql_file in sql_files:
        enc = encoding if encoding != "auto" else detect_encoding(sql_file)
        with open(sql_file, 'r', encoding=enc, errors='ignore') as f:
            sql_content = f.read()

        story.append(Paragraph(f"File: {os.path.basename(sql_file)}", styles['Heading2']))
        story.append(Spacer(1, 8))

        for line in sql_content.split("\n"):
            story.append(Paragraph(line.replace(" ", "&nbsp;"), styles['Normal']))
            story.append(Spacer(1, 4))

        story.append(Spacer(1, 20))

    doc.build(story)


if __name__ == "__main__":
    root = Tk()
    root.withdraw()

    print("Select SQL files to convert:")
    sql_files = filedialog.askopenfilenames(filetypes=[("SQL Files", "*.sql")])

    if not sql_files:
        print("No files selected.")
        exit()

    merge_choice = input("Do you want to merge all into one PDF? (y/n): ").strip().lower()
    encoding_choice = input("Enter encoding (or type 'auto' to auto-detect): ").strip()

    if merge_choice == 'y':
        output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if output_pdf:
            merge_sql_to_pdf(sql_files, output_pdf, encoding=encoding_choice)
            print(f"Merged PDF saved as: {output_pdf}")
    else:
        for sql_file in sql_files:
            output_pdf = os.path.splitext(sql_file)[0] + ".pdf"
            enc = encoding_choice if encoding_choice != "auto" else detect_encoding(sql_file)
            sql_to_pdf(sql_file, output_pdf, encoding=enc)
            print(f"Converted: {sql_file} -> {output_pdf}")
