# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IpClient.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_IpClient(object):
    def setupUi(self, IpClient):
        IpClient.setObjectName(_fromUtf8("IpClient"))
        IpClient.resize(280, 212)
        self.ConnectBox = QtGui.QPushButton(IpClient)
        self.ConnectBox.setGeometry(QtCore.QRect(200, 158, 71, 24))
        self.ConnectBox.setMaximumSize(QtCore.QSize(16777215, 24))
        self.ConnectBox.setObjectName(_fromUtf8("ConnectBox"))
        self.ServerTitle = QtGui.QLabel(IpClient)
        self.ServerTitle.setGeometry(QtCore.QRect(40, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ServerTitle.setFont(font)
        self.ServerTitle.setObjectName(_fromUtf8("ServerTitle"))
        self.LocalGroup = QtGui.QGroupBox(IpClient)
        self.LocalGroup.setGeometry(QtCore.QRect(10, 40, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LocalGroup.setFont(font)
        self.LocalGroup.setObjectName(_fromUtf8("LocalGroup"))
        self.IPaddrTitle = QtGui.QLabel(self.LocalGroup)
        self.IPaddrTitle.setGeometry(QtCore.QRect(30, 70, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.IPaddrTitle.setFont(font)
        self.IPaddrTitle.setObjectName(_fromUtf8("IPaddrTitle"))
        self.MACTitle = QtGui.QLabel(self.LocalGroup)
        self.MACTitle.setGeometry(QtCore.QRect(30, 30, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.MACTitle.setFont(font)
        self.MACTitle.setObjectName(_fromUtf8("MACTitle"))
        self.macButton = QtGui.QPushButton(self.LocalGroup)
        self.macButton.setGeometry(QtCore.QRect(10, 30, 16, 16))
        self.macButton.setText(_fromUtf8(""))
        self.macButton.setObjectName(_fromUtf8("macButton"))
        self.ipButton = QtGui.QPushButton(self.LocalGroup)
        self.ipButton.setGeometry(QtCore.QRect(10, 70, 16, 16))
        self.ipButton.setText(_fromUtf8(""))
        self.ipButton.setObjectName(_fromUtf8("ipButton"))
        self.MACEdit = QtGui.QLineEdit(self.LocalGroup)
        self.MACEdit.setGeometry(QtCore.QRect(80, 30, 141, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.MACEdit.setFont(font)
        self.MACEdit.setObjectName(_fromUtf8("MACEdit"))
        self.IPaddrEdit = QtGui.QLineEdit(self.LocalGroup)
        self.IPaddrEdit.setGeometry(QtCore.QRect(100, 70, 121, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.IPaddrEdit.setFont(font)
        self.IPaddrEdit.setObjectName(_fromUtf8("IPaddrEdit"))
        self.MethodBox = QtGui.QComboBox(IpClient)
        self.MethodBox.setGeometry(QtCore.QRect(60, 160, 71, 21))
        self.MethodBox.setObjectName(_fromUtf8("MethodBox"))
        self.ISPTitle = QtGui.QLabel(IpClient)
        self.ISPTitle.setGeometry(QtCore.QRect(10, 160, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ISPTitle.setFont(font)
        self.ISPTitle.setObjectName(_fromUtf8("ISPTitle"))
        self.VersionEdit = QtGui.QTextEdit(IpClient)
        self.VersionEdit.setGeometry(QtCore.QRect(0, 190, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VersionEdit.setFont(font)
        self.VersionEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.VersionEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.VersionEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.VersionEdit.setReadOnly(True)
        self.VersionEdit.setObjectName(_fromUtf8("VersionEdit"))
        self.ConnectEdit = QtGui.QTextEdit(IpClient)
        self.ConnectEdit.setGeometry(QtCore.QRect(140, 190, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ConnectEdit.setFont(font)
        self.ConnectEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ConnectEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ConnectEdit.setReadOnly(True)
        self.ConnectEdit.setObjectName(_fromUtf8("ConnectEdit"))
        self.ServerEdit = QtGui.QLineEdit(IpClient)
        self.ServerEdit.setGeometry(QtCore.QRect(110, 10, 121, 21))
        self.ServerEdit.setObjectName(_fromUtf8("ServerEdit"))

        self.retranslateUi(IpClient)
        QtCore.QMetaObject.connectSlotsByName(IpClient)

    def retranslateUi(self, IpClient):
        IpClient.setWindowTitle(_translate("IpClient", "IPClient", None))
        self.ConnectBox.setText(_translate("IpClient", "Connect", None))
        self.ServerTitle.setText(_translate("IpClient", "Server:", None))
        self.LocalGroup.setTitle(_translate("IpClient", "Local:", None))
        self.IPaddrTitle.setText(_translate("IpClient", "IPaddr:", None))
        self.MACTitle.setText(_translate("IpClient", "MAC:", None))
        self.ISPTitle.setText(_translate("IpClient", "ISP:", None))

