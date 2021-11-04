import sys
import os
from trust import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.compfacts)
     self.ui.pushButton_2.clicked.connect(self.qfacts)
     self.ui.pushButton_3.clicked.connect(self.mlpc)
     self.ui.pushButton_4.clicked.connect(self.qdac)
     self.ui.pushButton_5.clicked.connect(self.shfacts)
     self.ui.pushButton_6.clicked.connect(self.compr)
     

  def compfacts(self):
    os.system("python comp1.py")

  def qfacts(self):
    os.system("python qlty1.py")

  def mlpc(self):
    os.system("python mlpc1.py")

  def qdac(self):
    os.system("python qda1.py")

  def shfacts(self):
    os.system("python scale1.py")
	
  def compr(self):
    os.system("python -W ignore piechart1.py")
	


          
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
