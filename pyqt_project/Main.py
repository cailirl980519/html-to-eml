from Ui_layout import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from Generate import Gen_Emails

class Action(QtWidgets.QMainWindow):
    def __init__(self):
        super(Action, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.browse.clicked.connect(self.action1)
        self.ui.browse2.clicked.connect(self.action2)
        self.ui.pushButton.clicked.connect(self.action3)

    def action1(self):
        files = QFileDialog.getOpenFileNames(None,"Select Files", "","HTML (*.html;*.htm;*.shtml;*xhtml);;All Files (*)")
        if files:
            self.file_list = files[0]
        self.ui.path.setText(';'.join(self.file_list))

    def action2(self):
        self.output = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.ui.output.setText(self.output)

    def action3(self):
        if(self.ui.path.text()=='' or self.ui.output.text()==''):
            q = QMessageBox(QMessageBox.Warning, "Warning!",  'Please select path.')
            q.setStandardButtons(QMessageBox.Ok)
            i = QIcon()
            i.addPixmap(QPixmap("..."), QIcon.Normal)
            q.setWindowIcon(i)
            q.exec_()
        else:
            files = self.ui.path.text().split(';')
            output = self.ui.output.text()
            gen = Gen_Emails()
            gen.FindFiles(files, output)
            self.Finish()

    def Finish(self):
        q = QMessageBox(QMessageBox.Information, "Finish!",  'Transfer Compelte!')
        q.setStandardButtons(QMessageBox.Ok)
        i = QIcon()
        i.addPixmap(QPixmap("..."), QIcon.Normal)
        q.setWindowIcon(i)
        q.exec_()
        self.ui.path.setText("")
        self.ui.output.setText("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = Action()
    window.show()
    sys.exit(app.exec_())