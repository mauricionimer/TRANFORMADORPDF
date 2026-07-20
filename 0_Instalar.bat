@echo off
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
    echo ERRO: Python nao foi encontrado neste computador.
    echo Instale o Python em https://www.python.org/downloads/ ^(marque a opcao
    echo "Add Python to PATH" durante a instalacao^) e rode este arquivo de novo.
    pause
    exit /b 1
)

echo ============================================
echo  Instalando dependencias do gerador de PDF...
echo  ^(isso pode levar alguns minutos na primeira vez^)
echo ============================================
echo.

python -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERRO ao instalar as bibliotecas Python. Veja a mensagem acima.
    pause
    exit /b 1
)

python -m playwright install chromium
if errorlevel 1 (
    echo.
    echo ERRO ao instalar o Chromium. Veja a mensagem acima.
    pause
    exit /b 1
)

echo.
echo ============================================
echo  Instalacao concluida com sucesso!
echo  Agora use o arquivo 1_Gerar_PDF.bat sempre que
echo  precisar gerar um PDF novo.
echo ============================================
pause
