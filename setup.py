from cx_Freeze import setup, Executable
import sys
import os

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os", "tkinter", "pandas", "tabula", "pdfplumber"],
    "excludes": [],
    "include_files": ["sample_statement.pdf"]
}

# GUI applications require a different base on Windows
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="PDF to CSV Converter",
    version="1.0",
    description="Convert PDF bank statements to CSV format",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "gui_converter.py",
            base=base,
            target_name="PDFtoCSVConverter.exe",
            icon=None
        )
    ]
) 