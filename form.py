# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(508, 222)
        MainWindow.setMinimumSize(QtCore.QSize(508, 222))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnScanDir = QtWidgets.QPushButton(self.centralwidget)
        self.btnScanDir.setMinimumSize(QtCore.QSize(241, 26))
        self.btnScanDir.setObjectName("btnScanDir")
        self.verticalLayout.addWidget(self.btnScanDir)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(241, 26))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditSetDirPermissions = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSetDirPermissions.setMinimumSize(QtCore.QSize(151, 26))
        self.lineEditSetDirPermissions.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditSetDirPermissions.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditSetDirPermissions.setReadOnly(True)
        self.lineEditSetDirPermissions.setObjectName("lineEditSetDirPermissions")
        self.horizontalLayout_2.addWidget(self.lineEditSetDirPermissions)
        self.lineEditDirPermissions = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDirPermissions.setMinimumSize(QtCore.QSize(41, 26))
        self.lineEditDirPermissions.setMaximumSize(QtCore.QSize(41, 26))
        self.lineEditDirPermissions.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditDirPermissions.setObjectName("lineEditDirPermissions")
        self.horizontalLayout_2.addWidget(self.lineEditDirPermissions)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEditSetFilePermissions = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSetFilePermissions.setMinimumSize(QtCore.QSize(151, 26))
        self.lineEditSetFilePermissions.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditSetFilePermissions.setReadOnly(True)
        self.lineEditSetFilePermissions.setObjectName("lineEditSetFilePermissions")
        self.horizontalLayout_3.addWidget(self.lineEditSetFilePermissions)
        self.lineEditFilePermissions = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFilePermissions.setMinimumSize(QtCore.QSize(41, 26))
        self.lineEditFilePermissions.setMaximumSize(QtCore.QSize(41, 26))
        self.lineEditFilePermissions.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditFilePermissions.setObjectName("lineEditFilePermissions")
        self.horizontalLayout_3.addWidget(self.lineEditFilePermissions)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.checkBoxSudo = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxSudo.setObjectName("checkBoxSudo")
        self.horizontalLayout.addWidget(self.checkBoxSudo)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.btnChangePermissions = QtWidgets.QPushButton(self.centralwidget)
        self.btnChangePermissions.setMinimumSize(QtCore.QSize(171, 26))
        self.btnChangePermissions.setObjectName("btnChangePermissions")
        self.horizontalLayout_4.addWidget(self.btnChangePermissions)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnScanDir.setText(_translate("MainWindow", "Open directory to change permissions"))
        self.lineEditSetDirPermissions.setText(_translate("MainWindow", "Set Directory permissions"))
        self.lineEditDirPermissions.setPlaceholderText(_translate("MainWindow", "755"))
        self.lineEditSetFilePermissions.setText(_translate("MainWindow", "Set File permissions"))
        self.lineEditFilePermissions.setPlaceholderText(_translate("MainWindow", "644"))
        self.checkBoxSudo.setText(_translate("MainWindow", "I need sudo privileges"))
        self.btnChangePermissions.setText(_translate("MainWindow", "Start changing permissions"))
