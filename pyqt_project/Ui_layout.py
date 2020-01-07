# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Owner\pyqt_project\layout.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(395, 125)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.output_label.setFont(font)
        self.output_label.setObjectName("output_label")
        self.gridLayout.addWidget(self.output_label, 1, 0, 1, 1)
        self.path_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.path_label.setFont(font)
        self.path_label.setObjectName("path_label")
        self.gridLayout.addWidget(self.path_label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.browse.setFont(font)
        self.browse.setObjectName("browse")
        self.gridLayout.addWidget(self.browse, 0, 2, 1, 1)
        self.path = QtWidgets.QLineEdit(self.centralwidget)
        self.path.setObjectName("path")
        self.gridLayout.addWidget(self.path, 0, 1, 1, 1)
        self.output = QtWidgets.QLineEdit(self.centralwidget)
        self.output.setObjectName("output")
        self.gridLayout.addWidget(self.output, 1, 1, 1, 1)
        self.browse2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.browse2.setFont(font)
        self.browse2.setObjectName("browse2")
        self.gridLayout.addWidget(self.browse2, 1, 2, 1, 1)
        self.status = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.status.setFont(font)
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 2, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Html to Eml"))
        self.output_label.setText(_translate("MainWindow", "Save path"))
        self.path_label.setText(_translate("MainWindow", "File path"))
        self.pushButton.setText(_translate("MainWindow", "Confirm"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.browse2.setText(_translate("MainWindow", "Browse"))
        self.status.setText(_translate("MainWindow", "Enter Html file path and outputl Eml path."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

