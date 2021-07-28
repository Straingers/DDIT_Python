import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import random

form_class = uic.loadUiType("myqt07.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb.clicked.connect(self.btnClick)
    
    def btnClick(self):
        mine = self.le_mine.text()
        rnd = random.random()
        com = ""
        if rnd > 0.66:
            com = "가위"
        elif rnd > 0.33:
            com = "바위"
        else:
            com = "보"
        self.le_com.setText(com)
        result = ""
        if mine == "가위" and com == "보":
            result = "승리"
        elif mine == "바위" and com == "가위":
            result = "승리"
        elif mine == "보" and com == "바위":
            result = "승리"
        elif mine == "가위" and com == "바위":
            result = "패배"
        elif mine == "바위" and com == "보":
            result = "패배"
        elif mine == "보" and com == "가위":
            result = "패배"
        else :
            result = "무승부"
        self.le_result.setText(result)    
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())