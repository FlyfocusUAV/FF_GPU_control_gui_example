# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FF_GPU_control_gui_example.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(926, 555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TensionSetButton = QtWidgets.QPushButton(self.centralwidget)
        self.TensionSetButton.setGeometry(QtCore.QRect(260, 170, 211, 71))
        self.TensionSetButton.setObjectName("TensionSetButton")
        self.TensionSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.TensionSpinBox.setGeometry(QtCore.QRect(20, 170, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.TensionSpinBox.setFont(font)
        self.TensionSpinBox.setMaximum(4000)
        self.TensionSpinBox.setSingleStep(100)
        self.TensionSpinBox.setObjectName("TensionSpinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.OffSetButton = QtWidgets.QPushButton(self.centralwidget)
        self.OffSetButton.setGeometry(QtCore.QRect(260, 60, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.OffSetButton.setFont(font)
        self.OffSetButton.setObjectName("OffSetButton")
        self.OnSetButton = QtWidgets.QPushButton(self.centralwidget)
        self.OnSetButton.setGeometry(QtCore.QRect(20, 60, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.OnSetButton.setFont(font)
        self.OnSetButton.setObjectName("OnSetButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(550, 60, 271, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.StatusHrtbtLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.StatusHrtbtLabel.setFont(font)
        self.StatusHrtbtLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.StatusHrtbtLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.StatusHrtbtLabel.setTextFormat(QtCore.Qt.AutoText)
        self.StatusHrtbtLabel.setObjectName("StatusHrtbtLabel")
        self.verticalLayout.addWidget(self.StatusHrtbtLabel)
        self.StatusOutputStateLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.StatusOutputStateLabel.setFont(font)
        self.StatusOutputStateLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.StatusOutputStateLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.StatusOutputStateLabel.setTextFormat(QtCore.Qt.AutoText)
        self.StatusOutputStateLabel.setObjectName("StatusOutputStateLabel")
        self.verticalLayout.addWidget(self.StatusOutputStateLabel)
        self.StatusTensionLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.StatusTensionLabel.setFont(font)
        self.StatusTensionLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.StatusTensionLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.StatusTensionLabel.setTextFormat(QtCore.Qt.AutoText)
        self.StatusTensionLabel.setObjectName("StatusTensionLabel")
        self.verticalLayout.addWidget(self.StatusTensionLabel)
        self.StatusCableLenLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.StatusCableLenLabel.setFont(font)
        self.StatusCableLenLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.StatusCableLenLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.StatusCableLenLabel.setTextFormat(QtCore.Qt.AutoText)
        self.StatusCableLenLabel.setObjectName("StatusCableLenLabel")
        self.verticalLayout.addWidget(self.StatusCableLenLabel)
        self.StatusPwrLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.StatusPwrLabel.setFont(font)
        self.StatusPwrLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.StatusPwrLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.StatusPwrLabel.setTextFormat(QtCore.Qt.AutoText)
        self.StatusPwrLabel.setObjectName("StatusPwrLabel")
        self.verticalLayout.addWidget(self.StatusPwrLabel)
        self.StatusMainsLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.StatusMainsLabel.setFont(font)
        self.StatusMainsLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.StatusMainsLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.StatusMainsLabel.setTextFormat(QtCore.Qt.AutoText)
        self.StatusMainsLabel.setObjectName("StatusMainsLabel")
        self.verticalLayout.addWidget(self.StatusMainsLabel)
        self.TensionZeroButton = QtWidgets.QPushButton(self.centralwidget)
        self.TensionZeroButton.setGeometry(QtCore.QRect(260, 270, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.TensionZeroButton.setFont(font)
        self.TensionZeroButton.setObjectName("TensionZeroButton")
        self.BrakeOnButton = QtWidgets.QPushButton(self.centralwidget)
        self.BrakeOnButton.setGeometry(QtCore.QRect(20, 380, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.BrakeOnButton.setFont(font)
        self.BrakeOnButton.setObjectName("BrakeOnButton")
        self.BrakeOffButton = QtWidgets.QPushButton(self.centralwidget)
        self.BrakeOffButton.setGeometry(QtCore.QRect(260, 380, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.BrakeOffButton.setFont(font)
        self.BrakeOffButton.setObjectName("BrakeOffButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FF Tethered Ground Power Unit GUI example"))
        self.TensionSetButton.setText(_translate("MainWindow", "Cable Tension SET [g]"))
        self.label.setText(_translate("MainWindow", "SETTINGS"))
        self.label_2.setText(_translate("MainWindow", "STATUS"))
        self.OffSetButton.setText(_translate("MainWindow", "OUTPUT OFF"))
        self.OnSetButton.setText(_translate("MainWindow", "OUTPUT ON"))
        self.StatusHrtbtLabel.setText(_translate("MainWindow", "HEARTBEAT:"))
        self.StatusOutputStateLabel.setText(_translate("MainWindow", "OUTPUT: "))
        self.StatusTensionLabel.setText(_translate("MainWindow", "TENSION [g]: "))
        self.StatusCableLenLabel.setText(_translate("MainWindow", "CABLE LEN [m]: "))
        self.StatusPwrLabel.setText(_translate("MainWindow", "POWER[W]: "))
        self.StatusMainsLabel.setText(_translate("MainWindow", "MAINS: "))
        self.TensionZeroButton.setText(_translate("MainWindow", "Tension Zero"))
        self.BrakeOnButton.setText(_translate("MainWindow", "BRAKE ON"))
        self.BrakeOffButton.setText(_translate("MainWindow", "BRAKE OFF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
