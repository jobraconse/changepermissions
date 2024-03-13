import sys
import form
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QFileDialog, QCheckBox


class Window(QMainWindow, form.Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.center()
        self.btnScanDir.clicked.connect(self.openDirectory)
        self.btnChangePermissions.clicked.connect(self.setPermissions)
        self.checkBoxSudo.toggled.connect(self.onClicked)
        self.dir_mode = ""
        self.file_mode = ""
        self.startpath = ""
        self.needSudo = False
        

    def onClicked(self):
        if self.checkBoxSudo.isChecked():
            self.needSudo = True
        else:
            self.needSudo = False

    def list_files_and_directories(self):
        for root, dirs, files in os.walk(self.startpath, topdown=False):
            for name in files:
                f = (os.path.join(root, name))
                if self.needSudo:
                    cmd = 'sudo chmod ' + self.file_mode + ' ' + f
                else:
                    cmd = 'chmod ' + self.file_mode + ' ' + f
                os.system(cmd)
            for name in dirs:
                d = (os.path.join(root, name))
                if self.needSudo:
                    cmd = 'sudo chmod ' + self.dir_mode + ' ' + d
                else:
                    cmd = 'chmod ' + self.dir_mode + ' ' + d

        print("Done !")
        exit(0)

    def setPermissions(self):
        self.dir_mode = self.lineEditDirPermissions.text()
        self.file_mode = self.lineEditFilePermissions.text()
        self.list_files_and_directories()

    def openDirectory(self):
        file = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.lineEdit.setText(file)
        self.startpath = file

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeApp(self):
        exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())