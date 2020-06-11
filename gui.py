# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from tensorflow.keras.models import Sequential, Model, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Input
from tensorflow.nn import relu, sigmoid
from tensorflow.keras.optimizers import Adam
from tensorflow.train import latest_checkpoint
import numpy as np
import os
from PIL import Image

width = 224
height = 224

# MODEL
model = Sequential([
    Conv2D(32, (3,3), activation=relu, input_shape=(width, height, 1)),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(64, (3,3), activation=relu),  
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(128, (3,3), activation=relu), 
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(128, (3,3), activation=relu), 
    MaxPooling2D(pool_size=(2,2)),
    Flatten(),
#     Dropout(0.4),
    Dense(512, activation=relu),
    Dropout(0.3),
    Dense(256, activation=relu),
    Dense(1, activation=sigmoid)
])
model.compile(
    optimizer=Adam(),
    loss='binary_crossentropy',
    metrics=['accuracy']
)
model.summary()

checkpoint_filepath = './Model_checkpoint/ckpt{epoch}.ckpt'
checkpoint_dir = os.path.dirname(checkpoint_filepath)
latest = latest_checkpoint(checkpoint_dir)
print(latest)
model.load_weights(latest)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(533, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.citra = QtWidgets.QLabel(self.centralwidget)
        self.citra.setGeometry(QtCore.QRect(150, 100, 224, 224))
        self.citra.setStyleSheet("")
        self.citra.setText("")
        self.citra.setPixmap(QtGui.QPixmap("noimage.png"))
        self.citra.setScaledContents(True)
        self.citra.setObjectName("citra")
        self.bPredict = QtWidgets.QPushButton(self.centralwidget)
        self.bPredict.setGeometry(QtCore.QRect(220, 390, 75, 23))
        self.bPredict.setStyleSheet("font-size:15px;")
        self.bPredict.setObjectName("bPredict")
        self.bOpen = QtWidgets.QPushButton(self.centralwidget)
        self.bOpen.setGeometry(QtCore.QRect(220, 340, 75, 23))
        self.bOpen.setObjectName("bOpen")
        self.judul = QtWidgets.QLabel(self.centralwidget)
        self.judul.setGeometry(QtCore.QRect(100, 20, 311, 31))
        self.judul.setStyleSheet("font-size: 20px;")
        self.judul.setAlignment(QtCore.Qt.AlignCenter)
        self.judul.setObjectName("judul")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 80, 491, 291))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("border: 1px solid #aaaaaa;\n"
"background-color:#dddddd;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 379, 491, 81))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("border: 1px solid #aaaaaa;\n"
"background-color:#dddddd;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.hasil = QtWidgets.QLabel(self.frame_2)
        self.hasil.setGeometry(QtCore.QRect(190, 50, 95, 16))
        self.hasil.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hasil.setStyleSheet("font-size:15px;")
        self.hasil.setAlignment(QtCore.Qt.AlignCenter)
        self.hasil.setObjectName("hasil")
        self.frame.raise_()
        self.frame_2.raise_()
        self.citra.raise_()
        self.bPredict.raise_()
        self.bOpen.raise_()
        self.judul.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 533, 21))
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
        self.judul.setText(_translate("MainWindow", "KLASIFIKASI PNEUMONIA"))
        self.hasil.setText(_translate("MainWindow", "HASIL"))

    def openF(self):
        self.fname,_ = QtWidgets.QFileDialog.getOpenFileName()
        print(self.fname)
        self.citra.setPixmap(QtGui.QPixmap(self.fname))

    def predict(self):
        image = Image.open(self.fname).convert('L')
        print(image)
        color = False
        width = 224
        height = 224
        # if color:
        #     image = image.convert("RGB")
        data = np.array(image.resize((width,height), Image.ANTIALIAS)).reshape(1, width, height, 3 if color else 1)/255
        jwb = ("PNEUMONIA" if model.predict(data) > 0.5 else "NORMAL")
        print("predict: "+ self.fname)
        print(jwb)
        _translate = QtCore.QCoreApplication.translate 
        self.hasil.setText(_translate("MainWindow", jwb)) # ubah label hasil dg hasil predict
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
