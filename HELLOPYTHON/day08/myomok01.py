import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtGui
from PyQt5.Qt import QPushButton, QRect, QSize

form_class = uic.loadUiType("myomok01.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.arr2D = [
                 [0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
            ]
        self.pb2D = []
        self.cnt = 0
        
        for i in range(10):
            pb_line = []
            for j in range(10):
                tmp = QPushButton(self)
                tmp.setIconSize(QSize(40, 40))
                tmp.setGeometry(QRect(40 * j, 40 * i, 40, 40))
                tmp.setToolTip(str(i) + "," + str(j))
                tmp.setIcon(QtGui.QIcon("0.png"))
                tmp.clicked.connect(self.btnClick)
                pb_line.append(tmp)
            self.pb2D.append(pb_line)
        
        self.myrender()    
        
    def myrender(self):
        for i in range(len(self.pb2D)):
            x = self.pb2D[i].split(",")[0]
            y = self.pb2D[i].split(",")[1]
            
                    
        for i in range(len(self.arr2D)):
            for j in range(len(self.arr2D[i])):
                self.pb2D[i][j].setIcon(QtGui.QIcon(str(self.arr2D[i][j]) + ".png"))
                
        #for i in range(10):
        #    for j in range(10):
        #        if self.arr2D[i][j] == 0:
        #            self.pb2D[i][j].setIcon(QtGui.QIcon("0.png"))
        #        if self.arr2D[i][j] == 1:
        #            self.pb2D[i][j].setIcon(QtGui.QIcon("1.png"))
        #        if self.arr2D[i][j] == 2:
        #            self.pb2D[i][j].setIcon(QtGui.QIcon("2.png"))
    def btnClick(self):
        tt = self.sender().toolTip().split(",")
        x = int(tt[0])
        y = int(tt[1])
        if self.cnt % 2 == 0:
            if self.arr2D[x][y] == 1 or self.arr2D[x][y] == 2:
                return
            self.arr2D[x][y] = 1
        elif self.cnt % 2 == 1:
            if self.arr2D[x][y] == 1 or self.arr2D[x][y] == 2:
                return
            self.arr2D[x][y] = 2    
        self.cnt += 1
        self.myrender()
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())