import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.Qt import QPushButton, QRect, QSize

form_class = uic.loadUiType("myomok20.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.flag_ing = True
        self.pb_reset.clicked.connect(self.myreset)
        self.arr2D = []
        self.cnt = 0
        for i in range(20):
            tmp = []
            for j in range(20):
                tmp.append(0)
            self.arr2D.append(tmp)
        self.pb2D = []
        self.cnt = 0
        
        for i in range(20):
            pb_line = []
            for j in range(20):
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
        self.cnt = 0
        self.flag_ing = True
        for i in range(20):
            for j in range(20):
                self.arr2D[i][j] = 0
        self.myrender()
        
    def myrender(self):
        for i in range(20):
            for j in range(20):
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
        bk_i = int(arr_ij[0])
        bk_j = int(arr_ij[1])
        wh_i = 0
        wh_j = self.cnt
        
        if self.arr2D[bk_i][bk_j] > 0:
            return
        
        self.arr2D[bk_i][bk_j] = 1
        stone_bk = 1
            
        bk_up = self.getUp(bk_i, bk_j, stone_bk)
        bk_dw = self.getDw(bk_i, bk_j, stone_bk)
        bk_le = self.getLe(bk_i, bk_j, stone_bk)
        bk_ri = self.getRi(bk_i, bk_j, stone_bk)
        bk_ur = self.getUR(bk_i, bk_j, stone_bk)
        bk_dl = self.getDL(bk_i, bk_j, stone_bk)
        bk_ul = self.getUL(bk_i, bk_j, stone_bk)
        bk_dr = self.getDR(bk_i, bk_j, stone_bk)
        
        arr_bk = [bk_up+bk_dw+1, bk_le+bk_ri+1, bk_ur+bk_dl+1, bk_ul+bk_dr+1]
        
        for dol in arr_bk:
            if dol == 5:
                result = "흑돌"
                self.flag_ing = False
                self.myrender()
                QtWidgets.QMessageBox.about(self, "오목", result + " 승리!")
                return
                
        self.arr2D[wh_i][wh_j] = 2
        self.cnt += 1
        stone_wh = 2
        
        wh_up = self.getUp(wh_i, wh_j, stone_wh)
        wh_dw = self.getDw(wh_i, wh_j, stone_wh)
        wh_le = self.getLe(wh_i, wh_j, stone_wh)
        wh_ri = self.getRi(wh_i, wh_j, stone_wh)
        wh_ur = self.getUR(wh_i, wh_j, stone_wh)
        wh_dl = self.getDL(wh_i, wh_j, stone_wh)
        wh_ul = self.getUL(wh_i, wh_j, stone_wh)
        wh_dr = self.getDR(wh_i, wh_j, stone_wh)

        arr_wh = [wh_up+wh_dw+1, wh_le+wh_ri+1, wh_ur+wh_dl+1, wh_ul+wh_dr+1]
        
        for dol in arr_wh:
            if dol == 5:
                result = "백돌"
                self.flag_ing = False
                self.myrender()
                QtWidgets.QMessageBox.about(self, "오목", result + " 승리!")
                return
                
        self.myrender()
        
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