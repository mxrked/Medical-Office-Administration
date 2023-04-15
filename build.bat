:: Creates dist
python -m PyInstaller --noconfirm --onedir --windowed --debug "all" --paths "%cd%" --add-data "%cd%/backend;backend/" --add-data "%cd%/frontend;frontend/" --hidden-import "greenlet" --hidden-import "pyodbc" --hidden-import "PyQt5" --hidden-import "PyQt5-Qt5" --hidden-import "PyQt5-sip" --hidden-import "SQLAlchemy" --hidden-import "typing_extensions"  "%cd%/run.py"
:: Creates Link to the .exe
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%cd%\main.lnk');$s.TargetPath='%cd%\dist\main\main.exe';$s.Save()"
