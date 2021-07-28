import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic

form_class = uic.loadUiType("myqt09.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb0.clicked.connect(self.btnClick)
        self.pb1.clicked.connect(self.btnClick)
        self.pb2.clicked.connect(self.btnClick)
        self.pb3.clicked.connect(self.btnClick)
        self.pb4.clicked.connect(self.btnClick)
        self.pb5.clicked.connect(self.btnClick)
        self.pb6.clicked.connect(self.btnClick)
        self.pb7.clicked.connect(self.btnClick)
        self.pb8.clicked.connect(self.btnClick)
        self.pb9.clicked.connect(self.btnClick)
        self.pbCall.clicked.connect(self.btnCallClick)
    
    def btnClick(self):
        num = self.sender().text()
        tel = self.le.text()
        tel += num
        if len(tel) == 3 or len(tel) == 8:
            tel += "-"
        if len(tel) == 14:
            return
        self.le.setText(tel)
        
    def btnCallClick(self):
        QMessageBox.question(self, 'Calling', "Call : " + self.le.text(),
                                    QMessageBox.Yes)
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())