@echo off
cd "C:\Users\VivianFerguson\OneDrive - JTec IT Ltd\Converter"
python create_sample_pdf.py
python pdf_to_csv_converter.py sample_statement.pdf -o converted_statement.csv
pause 