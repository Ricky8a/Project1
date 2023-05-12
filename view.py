# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(260, 600)
        MainWindow.setMinimumSize(QtCore.QSize(260, 600))
        MainWindow.setMaximumSize(QtCore.QSize(260, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.on_offButton = QtWidgets.QPushButton(self.centralwidget)
        self.on_offButton.setGeometry(QtCore.QRect(90, 220, 91, 91))
        self.on_offButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 0, 4);\n"
"    border-radius: 25px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.on_offButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/tv remote.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.on_offButton.setIcon(icon)
        self.on_offButton.setIconSize(QtCore.QSize(100, 100))
        self.on_offButton.setObjectName("on_offButton")
        self.volumeUp = QtWidgets.QPushButton(self.centralwidget)
        self.volumeUp.setGeometry(QtCore.QRect(10, 430, 81, 51))
        self.volumeUp.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 255, 17);\n"
"    border-radius: 25px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.volumeUp.setObjectName("volumeUp")
        self.volumeDown = QtWidgets.QPushButton(self.centralwidget)
        self.volumeDown.setGeometry(QtCore.QRect(10, 500, 81, 51))
        self.volumeDown.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 0, 4);\n"
"    border-radius: 25px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.volumeDown.setObjectName("volumeDown")
        self.mute = QtWidgets.QPushButton(self.centralwidget)
        self.mute.setGeometry(QtCore.QRect(100, 450, 61, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mute.setFont(font)
        self.mute.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(86, 86, 86);\n"
"    border-radius: 25px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.mute.setObjectName("mute")
        self.channelUp = QtWidgets.QPushButton(self.centralwidget)
        self.channelUp.setGeometry(QtCore.QRect(170, 430, 81, 51))
        self.channelUp.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 255, 17);\n"
"    border-radius: 25px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.channelUp.setObjectName("channelUp")
        self.channelDown = QtWidgets.QPushButton(self.centralwidget)
        self.channelDown.setGeometry(QtCore.QRect(170, 500, 81, 51))
        self.channelDown.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 0, 4);\n"
"    border-radius: 25px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.channelDown.setObjectName("channelDown")
        self.volumeLabel = QtWidgets.QLabel(self.centralwidget)
        self.volumeLabel.setGeometry(QtCore.QRect(10, 390, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.volumeLabel.setFont(font)
        self.volumeLabel.setObjectName("volumeLabel")
        self.channelLabel = QtWidgets.QLabel(self.centralwidget)
        self.channelLabel.setGeometry(QtCore.QRect(170, 390, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.channelLabel.setFont(font)
        self.channelLabel.setObjectName("channelLabel")
        self.tvDisplay = QtWidgets.QLabel(self.centralwidget)
        self.tvDisplay.setGeometry(QtCore.QRect(0, -8, 271, 221))
        self.tvDisplay.setAutoFillBackground(False)
        self.tvDisplay.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.tvDisplay.setText("")
        self.tvDisplay.setObjectName("tvDisplay")
        self.volumeDisplay = QtWidgets.QLabel(self.centralwidget)
        self.volumeDisplay.setGeometry(QtCore.QRect(10, -10, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.volumeDisplay.setFont(font)
        self.volumeDisplay.setStyleSheet("color: rgb(255, 255, 255);")
        self.volumeDisplay.setText("")
        self.volumeDisplay.setObjectName("volumeDisplay")
        self.channelDisplay = QtWidgets.QLabel(self.centralwidget)
        self.channelDisplay.setGeometry(QtCore.QRect(160, -10, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.channelDisplay.setFont(font)
        self.channelDisplay.setStyleSheet("color: rgb(255, 255, 255);")
        self.channelDisplay.setText("")
        self.channelDisplay.setObjectName("channelDisplay")
        self.channel0 = QtWidgets.QPushButton(self.centralwidget)
        self.channel0.setGeometry(QtCore.QRect(30, 330, 51, 51))
        self.channel0.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(80, 80, 80);\n"
"    border-radius: 25px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.channel0.setObjectName("channel0")
        self.channel1 = QtWidgets.QPushButton(self.centralwidget)
        self.channel1.setGeometry(QtCore.QRect(110, 330, 51, 51))
        self.channel1.setStyleSheet("QPushButton {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-radius: 25px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.channel1.setObjectName("channel1")
        self.channel2 = QtWidgets.QPushButton(self.centralwidget)
        self.channel2.setGeometry(QtCore.QRect(190, 330, 51, 51))
        self.channel2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-radius: 25px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.channel2.setObjectName("channel2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 260, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.volumeUp.setText(_translate("MainWindow", "+"))
        self.volumeDown.setText(_translate("MainWindow", "-"))
        self.mute.setText(_translate("MainWindow", "MUTE"))
        self.channelUp.setText(_translate("MainWindow", "+"))
        self.channelDown.setText(_translate("MainWindow", "-"))
        self.volumeLabel.setText(_translate("MainWindow", "VOLUME"))
        self.channelLabel.setText(_translate("MainWindow", "CHANNEL"))
        self.channel0.setText(_translate("MainWindow", "0"))
        self.channel1.setText(_translate("MainWindow", "1"))
        self.channel2.setText(_translate("MainWindow", "2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
