# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.citra = QtWidgets.QLabel(self.centralwidget)
        self.citra.setGeometry(QtCore.QRect(70, 70, 224, 224))
        self.citra.setText("")
        self.citra.setPixmap(QtGui.QPixmap("noimage.png"))
        self.citra.setScaledContents(True)
        self.citra.setObjectName("citra")
        self.bPredict = QtWidgets.QPushButton(self.centralwidget)
        self.bPredict.setGeometry(QtCore.QRect(70, 340, 75, 23))
        self.bPredict.setObjectName("bPredict")
        self.bOpen = QtWidgets.QPushButton(self.centralwidget)
        self.bOpen.setGeometry(QtCore.QRect(70, 300, 75, 23))
        self.bOpen.setObjectName("bOpen")
        self.hasil = QtWidgets.QLabel(self.centralwidget)
        self.hasil.setGeometry(QtCore.QRect(70, 380, 81, 16))
        self.hasil.setObjectName("hasil")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.fname = ""
        self.bOpen.clicked.connect(self.openF) #event buat klik open file
        self.bPredict.clicked.connect(self.predict)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bPredict.setText(_translate("MainWindow", "Predict"))
        self.bOpen.setText(_translate("MainWindow", "Pilih Gambar"))
        self.hasil.setText(_translate("MainWindow", "HASIL"))
    
    def openF(self):
        self.fname,_ = QtWidgets.QFileDialog.getOpenFileName()
        print(self.fname)
        self.citra.setPixmap(QtGui.QPixmap(self.fname))

    def predict(self):
        print("predict: "+ self.fname)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
