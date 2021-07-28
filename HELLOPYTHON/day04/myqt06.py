import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

form_class = uic.loadUiType("myqt06.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb.clicked.connect(self.btnClick)
    
    def btnClick(self):
        fst = int(self.le1.text())
        snd = int(self.le2.text())
        result = 0;
        for i in range(fst, snd + 1):
            if i % 2 == 0:
                result += i
        self.le3.setText(str(result))
    
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())