# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\data\Desktop\pyqt_project\layout.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 771, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.browse = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.browse.setObjectName("browse")
        self.gridLayout.addWidget(self.browse, 0, 2, 1, 1)
        self.output_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.output_label.setObjectName("output_label")
        self.gridLayout.addWidget(self.output_label, 1, 0, 1, 1)
        self.path = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.path.setObjectName("path")
        self.gridLayout.addWidget(self.path, 0, 1, 1, 1)
        self.path_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.path_label.setObjectName("path_label")
        self.gridLayout.addWidget(self.path_label, 0, 0, 1, 1)
        self.browse2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.browse2.setObjectName("browse2")
        self.gridLayout.addWidget(self.browse2, 1, 2, 1, 1)
        self.output = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.output.setObjectName("output")
        self.gridLayout.addWidget(self.output, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        self.status_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.status_label.setText("")
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName("status_label")
        self.gridLayout.addWidget(self.status_label, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Html to Eml"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.output_label.setText(_translate("MainWindow", "Save path"))
        self.path_label.setText(_translate("MainWindow", "File path"))
        self.browse2.setText(_translate("MainWindow", "Browse"))
        self.pushButton.setText(_translate("MainWindow", "Confirm"))
