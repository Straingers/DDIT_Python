import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.Qt import QPushButton, QRect, QSize

form_class = uic.loadUiType("myomok01.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.flag_wb = True
        self.flag_ing = True
        self.pb_reset.clicked.connect(self.myreset)
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
        
    def myreset(self):
        self.flag_wb = True
        self.flag_ing = True
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
        self.myrender()
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("0.png"))
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("1.png"))
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("2.png"))

    def btnClick(self):
        if not self.flag_ing:
            return
        
        arr_ij = self.sender().toolTip().split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2D[i][j] > 0:
            return
        
        stone = 0
        if self.flag_wb:
            self.arr2D[i][j] = 1
            stone = 1
        else:
            self.arr2D[i][j] = 2
            stone = 2
            
        up = self.getUp(i, j, stone)
        dw = self.getDw(i, j, stone)
        le = self.getLe(i, j, stone)
        ri = self.getRi(i, j, stone)
        ur = self.getUR(i, j, stone)
        dl = self.getDL(i, j, stone)
        ul = self.getUL(i, j, stone)
        dr = self.getDR(i, j, stone)
        
        arr = [up+dw+1, le+ri+1, ur+dl+1, ul+dr+1]
        for dol in arr:
            if dol == 5:
                result = ""
                if self.flag_wb:
                    result = "흑돌"
                else:
                    result = "백돌"
                self.flag_ing = False
                self.myrender()
                QtWidgets.QMessageBox.about(self, "오목", result + " 승리!")
        self.myrender()
        self.flag_wb = not self.flag_wb
        
    def getUp(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
            
    def getDw(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getLe(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getRi(self, i, j, stone):  
        cnt = 0
        try:
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt 
        
    def getUR(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt 
        
    def getDL(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt 
        
    def getUL(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt 
        
    def getDR(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt 
    
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass()
    myWindow.show()

    sys.exit(app.exec_())