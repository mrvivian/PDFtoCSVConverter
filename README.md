# PDF to CSV Converter

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful tool that converts bank statement PDFs into CSV format with specific formatting requirements. This application provides both a GUI and command-line interface for easy conversion of PDF bank statements.

## Contact
For any questions, support, or collaboration opportunities, please contact: **hello@mrvivian.com**

## Download
The latest executable version can be downloaded from the [Releases](https://github.com/mrvivian/pdf-to-csv-converter/releases) page.

## Features

- 🖥️ User-friendly GUI interface
- 📝 Command-line support for automation
- 🔄 Drag-and-drop functionality
- 📊 Maintains original date and amount formatting
- 💾 Automatic CSV generation
- 🛡️ Error handling and validation

## Requirements

### For End Users
- Windows operating system
- No additional software installation required

### For Developers
- Python 3.8 or higher
- Required Python packages (see `requirements.txt`):
  - PyPDF2
  - pandas
  - tkinter (usually comes with Python)

## Installation

### For End Users
1. Download the latest release from the releases page
2. Extract the ZIP file
3. Run `pdf_to_csv_converter.exe`

### For Developers
1. Clone the repository:
   ```bash
   git clone https://github.com/mrvivian/pdf-to-csv-converter.git
   cd pdf-to-csv-converter
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions

### Method 1: Drag and Drop (Recommended)
1. Double-click the `pdf_to_csv_converter.exe` file to open it
2. When the console window appears, drag and drop your PDF file directly onto the window
3. Press Enter
4. The converter will create an `output.csv` file in the same directory

### Method 2: Command Line
1. Open Command Prompt
2. Navigate to the directory containing the converter
3. Run the following command:
   ```
   pdf_to_csv_converter.exe "path\to\your\bank_statement.pdf"
   ```

## Output Format
The generated CSV file will have the following columns:
- Posting Date
- Value Date
- Narrative
- Debit Amount
- Credit Amount
- Balance

## Development

### Building from Source
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Run the build script:
   ```bash
   build_exe.bat
   ```
3. The executable will be created in the `deployment_package` directory

### Running Tests
1. Create a virtual environment
2. Install dependencies
3. Run the test script:
   ```bash
   python create_sample_pdf.py
   ```

## Notes
- The output CSV file will be named `output.csv` and will be created in the same directory as the executable
- The converter maintains the original formatting of dates and amounts
- All amounts are formatted to 2 decimal places
- Commas in the narrative are replaced with spaces to avoid CSV formatting issues

## Troubleshooting
If you encounter any issues:
1. Make sure you're using the correct PDF file path
2. Check that the PDF file is not open in another program
3. Verify that the PDF contains table data that can be extracted
4. Make sure you have write permissions in the directory

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request. Before contributing, please contact hello@mrvivian.com to discuss the changes you'd like to make.

## Support
For any issues, questions, or feature requests, please contact: **hello@mrvivian.com**

## License
This project is licensed under the MIT License - see the LICENSE file for details. 