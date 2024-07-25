@echo off
set /p project_name=Enter the name of your project: 

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing Requirements...
pip install -r requirements.txt

echo To activate the virtual environment, run: venv\Scripts\activate