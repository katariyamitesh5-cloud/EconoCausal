@echo off
cd /d C:\Projects\EconoCausal
call venv\Scripts\activate.bat
start "" http://127.0.0.1:8000
uvicorn App.main:app
pause
