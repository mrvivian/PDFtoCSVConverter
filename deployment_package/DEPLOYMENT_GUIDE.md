# PDF to CSV Converter Deployment Guide

## System Requirements
- Windows 10 or later
- .NET Framework 4.7.2 or later
- 4GB RAM minimum
- 500MB free disk space

## Installation Steps

1. Create a new directory on the target server where you want to install the application
2. Copy all files from this deployment package to the target directory
3. Ensure the target directory has write permissions for the application

## Available Applications

### PDF to CSV Converter (Command Line)
- Executable: `pdf_to_csv_converter.exe`
- Usage: Run from command line with appropriate parameters
- Example: `pdf_to_csv_converter.exe --input "path/to/pdf" --output "path/to/csv"`

### PDF to CSV Converter (GUI)
- Executable: `gui_converter.exe`
- Usage: Double-click to launch the graphical user interface
- Features:
  - Drag and drop PDF files
  - Select output directory
  - View conversion progress
  - Error logging

## Troubleshooting

### Common Issues
1. If the application fails to start:
   - Verify .NET Framework is installed
   - Check system requirements
   - Ensure all files are copied correctly

2. If conversion fails:
   - Check PDF file integrity
   - Verify sufficient disk space
   - Check file permissions

### Support
For additional support, please contact:
- Email: support@example.com
- Phone: +1 (555) 123-4567

## Security Notes
- The application requires read access to PDF files
- The application requires write access to the output directory
- No internet connection is required for operation
- All processing is done locally on the machine

## Updates
To update the application:
1. Backup your existing installation
2. Copy new files from the deployment package
3. Replace existing files
4. Test the application with sample files 