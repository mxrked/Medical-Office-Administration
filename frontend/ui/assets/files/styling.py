'''

    This holds all the different styling variables

'''

# Navigation
greyOutBtn_Style = "QPushButton {\n" \
              "    border-image: none;\n" \
              "    background-color: rgba(110, 204, 175, .2);\n" \
              "    color: rgba(0, 0, 0, .2);\n" \
              "    border: 2px solid rgba(0, 0, 0, .2);\n" \
              "}\n" \
              "\n" \
              "QPushButton::hover {\n" \
              "    background-color: rgb(139, 231, 100);\n" \
              "    color: white;\n" \
              "}"

# Start Window
validEnterLE_Style = """
            
                QLineEdit {
                    border-image: none;
                    border: none;
                    min-width: 200px;
                    height: 30px;
                    background-color: #F3ECB0;
                    color: #344D67;
                    font-family: "MS Shell Dlg 2";
                    font-size: 11;
                    padding-left: 10px;
                    
                }
            
            """
invalidEnterLE_Style = """
            
                QLineEdit {
                    border-image: none;
                    border: 2px solid red;
                    min-width: 200px;
                    height: 30px;
                    background-color: #F3ECB0;
                    color: #344D67;
                    font-family: "MS Shell Dlg 2";
                    font-size: 11;
                    padding-left: 10px;
                    
                }
            
            """
infoDialog_Style = "QDialog {background-color: #344D67; border: 2px solid white}"
infoDialogName_Style = "QLabel {color: white}"
infoDialogCloseBtn_Style = """
        
        QPushButton {
            background-color: #ADE792; 
            border: none; 
            color: #344D67; 
            height: 44px; 
            width: 69px; 
            margin-bottom: 20px;
            font-weight: bold;
        }
        
        QPushButton::hover {
            color: white;
            background-color: rgb(139, 231, 100);
        }
        
        """

# Scheduling Appointments Window
disableCustomTime_Style = "QTimeEdit {\n" \
              "    border-image: none;\n" \
              "    background-color: rgba(243, 236, 176, 133);\n" \
              "    font-family: 'MS Shell Dlg 2';\n" \
              "    color: #344D67;;\n" \
              "    border: none;\n" \
              "    font-size: 15;\n" \
              "    padding-left: 10px;\n" \
              "}\n"
enableCustomTime_Style = "QTimeEdit {\n" \
              "    border-image: none;\n" \
              "    background-color: rgb(243, 236, 176);\n" \
              "    font-family: 'MS Shell Dlg 2';\n" \
              "    color: #344D67;;\n" \
              "    border: none;\n" \
              "    font-size: 15;\n" \
              "    padding-left: 10px;\n" \
              "}\n"
enableFrameBtn_Style = "QPushButton {\n" \
              "    border-image: none;\n" \
              "    background-color: #6ECCAF;\n" \
              "    color: black;\n" \
              "    border: 2px solid black;\n" \
              "}\n" \
              "\n" \
              "QPushButton::hover {\n" \
              "    background-color: rgb(139, 231, 100);\n" \
              "    color: white;\n" \
              "}"
disableFrameBtn_Style = "QPushButton {\n" \
              "    border-image: none;\n" \
              "    background-color: rgba(110, 204, 175, .2);\n" \
              "    color: rgba(0, 0, 0, .2);\n" \
              "    border: 2px solid rgba(0, 0, 0, .2);\n" \
              "}\n" \
              "\n" \
              "QPushButton::hover {\n" \
              "    background-color: rgb(139, 231, 100);\n" \
              "    color: white;\n" \
              "}"
selectedBtn_Style = """

QPushButton { 
    border-image: none;
    background-color: #344D67;
    color: black;
    border: 2px solid black;
    color: white;
    }
"""