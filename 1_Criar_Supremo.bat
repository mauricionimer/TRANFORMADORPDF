@echo off
color 0A
echo ==============================================================
echo        A CRIAR A VERSAO SUPREMA DO ROBO (FILTROS INCLUSOS)
echo ==============================================================
echo.
pip install pymupdf pyinstaller openpyxl pandas

echo.
echo A compilar o executavel...
pyinstaller --onefile --windowed --icon=NONE --name "Robo_Supremo_Filtros" robo_supremo.py

echo.
echo ==============================================================
echo SUCESSO!
echo O "Robo_Supremo_Filtros.exe" foi gerado na pasta "dist".
echo ==============================================================
pause > nul
