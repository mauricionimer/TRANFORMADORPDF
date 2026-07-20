@echo off
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
    echo ERRO: Python nao foi encontrado neste computador.
    echo Rode primeiro o 0_Instalar.bat.
    pause
    exit /b 1
)

python app_gui.py
if errorlevel 1 (
    echo.
    echo Algo deu errado. Se for a primeira vez usando neste computador,
    echo rode o 0_Instalar.bat antes.
    pause
)
