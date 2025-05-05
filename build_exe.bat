@echo off
echo Installing required packages...
pip install -r requirements.txt
pip install pyinstaller

echo Building GUI executable...
pyinstaller --onefile --noconsole ^
    --add-data "deployment_package/config.json;deployment_package" ^
    --add-data "deployment_package/sample_data;deployment_package/sample_data" ^
    --name "PDF Converter" ^
    --windowed ^
    gui_converter.py

echo Build complete! The executable is in the dist folder.
pause 