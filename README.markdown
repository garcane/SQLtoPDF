# SQL to PDF Converter

## Overview
This Python script converts SQL files into PDF format, either individually or merged into a single PDF. It uses a graphical file selection interface and supports automatic encoding detection for input files. The script is a work in progress and designed to handle SQL files with customizable encoding options.

## Features
- Convert a single SQL file to a PDF with formatted text.
- Merge multiple SQL files into one PDF, with each file's content separated and labeled.
- Automatically detect file encoding or use a user-specified encoding.
- Uses `tkinter` for a user-friendly file selection dialog.
- Preserves SQL file formatting in the PDF output with proper spacing.

## Requirements
- Python 3.x
- Required Python libraries:
  - `chardet` (for encoding detection)
  - `reportlab` (for PDF generation)
  - `tkinter` (included with standard Python installation for GUI file dialogs)

Install the required libraries using:
```bash
pip install chardet reportlab
```

## Usage
1. Run the script:
   ```bash
   python sql_to_pdf.py
   ```
2. A file dialog will open to select one or more SQL files (`.sql` extension).
3. Choose whether to merge all selected files into a single PDF (`y`) or convert each file to its own PDF (`n`).
4. Specify the encoding for the SQL files (e.g., `utf-8`, `latin-1`, or `auto` for automatic detection).
5. If merging, select an output location for the combined PDF. If not merging, individual PDFs will be created in the same directory as the input files with the same name but a `.pdf` extension.
6. The script will generate the PDF(s) and print the output file paths.

## Example
```bash
Select SQL files to convert:
Do you want to merge all into one PDF? (y/n): y
Enter encoding (or type 'auto' to auto-detect): auto
```
- Select `script1.sql` and `script2.sql`.
- Choose to merge (`y`) and save as `output.pdf`.
- The script creates `output.pdf` containing the contents of both SQL files, with each file's name as a heading.

## File Structure
- **Input**: SQL files (`.sql`) selected via the file dialog.
- **Output**:
  - Merged mode: A single PDF file at the user-specified location.
  - Individual mode: One PDF per SQL file, saved in the same directory as the input file (e.g., `script1.sql` → `script1.pdf`).

## Limitations
- This is a work-in-progress script and may have bugs or incomplete features.
- Large SQL files may result in large PDFs due to line-by-line processing.
- The script replaces spaces with `&nbsp;` for PDF rendering, which may not handle all formatting cases perfectly.
- Error handling for invalid encodings or corrupted files is minimal (`errors='ignore'` is used).

## Future Improvements
- Add syntax highlighting for SQL code in the generated PDFs.
- Improve error handling for file reading and encoding issues.
- Support additional file formats or customization options (e.g., fonts, page sizes).
- Optimize PDF generation for large files by batching content.

## License
This project is unlicensed and provided as-is for personal use. Feel free to modify and extend it as needed.