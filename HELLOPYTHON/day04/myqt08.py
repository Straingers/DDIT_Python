import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

form_class = uic.loadUiType("myqt08.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb.clicked.connect(self.btnClick)
    
    def btnClick(self):
        dan = self.le.text()
        result = ""
        for i in range(1, 10):
            result += dan + " X " + str(i) + " = " + str(int(dan)*i) + "\n"
        self.tb.setText(result)
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())