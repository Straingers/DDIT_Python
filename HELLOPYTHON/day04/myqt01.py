import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

form_class = uic.loadUiType("myqt01.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb.clicked.connect(self.btnClick)
    
    def btnClick(self):
        self.lbl.setText("GoodEvening")
    
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())