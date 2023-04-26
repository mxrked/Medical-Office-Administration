"""
run.py - The main file for running the Medical Office Administration program for 
    Forsyth Family Center
Project Structure:

C:.. run.py, requirements.txt, build.bat
│
├───backend (Contains Models, Data managers & handlers)
│   └───private (Contains abstract and subclasses)
│   
└───frontend (Our main frontend screens)
    │.. main_window.py, start_window.py
    │ 
    ├───dialog  (Simple dialog windows)
    │   
    ├───private (Superclasses of all windows)
    │   
    ├───screens (individual screens for main_window.py)
    │   
    └───ui
        └───assets (Frontend assets)
            │
            ├───files (Globals, Settings, Styling etc.)
            │   
            ├───imgs (Images)
            │
            └───qrc (Converted image assets)
                
All import paths are relative to the root of the project.
"""
from frontend.start_window import main

if __name__ == "__main__":
    main()
