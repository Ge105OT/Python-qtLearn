# -*- coding:UTF-8 -*-
# date: 2017.5.25

import sys, os
from PyQt4 import QtCore, QtGui, uic
import Gui
from getIp import GetMac, ipConfigGetIp
from IPclient import send_handshake
from Config import CConfig
import ctypes

class IpClientGui(QtGui.QMainWindow, Gui.Ui_IpClient):
	def __init__(self, configFile, parent = None):
		super(IpClientGui, self).__init__(parent)
		self.setupUi(self)
		self.Cconf = CConfig(configFile)

		# member init
		self.configFile = configFile
		self.count = 0

		# config var
		self.IpLock = 0
		self.macLock = 0
		self.lockImage = ''
		self.unLockImage = ''

		# ctrl init
		self.ConnectEdit.setText("Not Connect!")
		self.MethodBox.addItems([u"联通", u"电信", u"移动"])
		self.sysIcon = QtGui.QSystemTrayIcon(self)

		# init config
		self.ReadConfig()

		self.ConnectBox.clicked.connect(self.Connect)
		self.macButton.clicked.connect(self.MacLockMsg)
		self.ipButton.clicked.connect(self.IpLockMsg)
		self.sysIcon.activated.connect(self.ClickSysIcon)

		self.createContextMenu()

	# replace ctrl regtion
	def MacLocadIcon(self, imagePath):
		macLockIcon = QtGui.QIcon(imagePath)
		self.macButton.setIcon(macLockIcon)

	def IpLocadIcon(self, imagePath):
		ipLockIcon = QtGui.QIcon(imagePath)
		self.ipButton.setIcon(ipLockIcon)

	# ctrl message regtion
	def Connect(self):
		mac = str(self.MACEdit.text())
		ip = str(self.IPaddrEdit.text())
		server = str(self.ServerEdit.text())
		isp = self.MethodBox.currentIndex() + 1 	#读取选项栏编号：
		send_handshake(mac, ip, isp, server)
		self.ConnectEdit.clear()
		self.ConnectEdit.setText("Connect Success!")
		# self.sysIconSet('..\\icon\\network.png')

	def MacLockMsg(self):
		if self.macLock == 1:
			self.macLock = 0
			self.MacLocadIcon(self.unLockImage)
		else:
			self.macLock = 1
			self.MacLocadIcon(self.lockImage)

	def IpLockMsg(self):
		if self.IpLock == 1:
			self.IpLock = 0
			self.IpLocadIcon(self.unLockImage)
		else:
			self.IpLock = 1
			self.IpLocadIcon(self.lockImage)

	def ClickSysIcon(self):
		self.sysIcon.showMessage("haha", "content", icon=2)

	# config regtion
	def ReadConfig(self):
		# print self.configFile
		# icon locad
		self.sysIconSet(self.Cconf.GetValue('IconFile', 'sysIcon'))
		self.WindowIconSet(self.Cconf.GetValue('IconFile', 'windowIcon'))
		self.lockImage = self.Cconf.GetValue('IconFile', 'lockIcon')
		self.unLockImage = self.Cconf.GetValue('IconFile', 'unLockIcon')

		# base seting
		self.VersionEdit.setText('Version:' + self.Cconf.GetValue('Version', 'Release'))
		self.ServerEdit.setText(self.Cconf.GetValue('LocadEdit', 'serverIP'))
		self.IpLock = int(self.Cconf.GetValue('Setting', 'iplock'))
		self.macLock = int(self.Cconf.GetValue('Setting', 'maclock'))

		# ip locad
		if self.IpLock == 1:
			self.IPaddrEdit.setText(self.Cconf.GetValue('LocadEdit', 'localIP'))
			self.IpLocadIcon(self.lockImage)
		else:	
			self.IPaddrEdit.setText(ipConfigGetIp())
			self.IpLocadIcon(self.unLockImage)

		# mac locad
		if self.macLock:
			self.MACEdit.setText(self.Cconf.GetValue('LocadEdit', 'localmac'))
			self.MacLocadIcon(self.lockImage)
		else:
			self.MACEdit.setText(GetMac().upper())
			self.MacLocadIcon(self.unLockImage)
		
		# combo box
		self.MethodBox.setCurrentIndex(int(self.Cconf.GetValue('LocadCombo', 'Method')))

	def UpdateConfige(self):
		self.Cconf.UpdateValue('Setting', 'iplock', str(self.IpLock))
		self.Cconf.UpdateValue('Setting', 'maclock', str(self.macLock))

		self.Cconf.UpdateValue('LocadEdit', 'serverIP', str(self.ServerEdit.text()))
		self.Cconf.UpdateValue('LocadEdit', 'localIP', str(self.IPaddrEdit.text()))
		self.Cconf.UpdateValue('LocadEdit', 'localmac', str(self.MACEdit.text()))

		self.Cconf.UpdateValue('LocadCombo', 'Method', str(self.MethodBox.currentIndex()))
		self.Cconf.UpdateConfigFile()

	# local sys icon
	def sysIconSet(self, imageFile):
		icon = QtGui.QIcon(imageFile)
		self.sysIcon.setIcon(icon)
		self.sysIcon.show()
		pass

	# local sys icon
	def WindowIconSet(self, imageFile):
		icon = QtGui.QIcon(imageFile)
		self.setWindowIcon(icon)
		pass

	def closeEvent(self, QCloseEvent):
		self.UpdateConfige()

	def createContextMenu(self):
		'''
			创建右键菜单
		'''
		# 必须将ContextMenuPolicy设置为Qt.CustomContextMenu
		# 否则无法使用customContextMenuRequested信号
		self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.customContextMenuRequested.connect(self.showContextMenu)
		   
		# 创建QMenu
		self.contextMenu = 	QtGui.QMenu(self)
		self.actionA = self.contextMenu.addAction(QtGui.QIcon("images/0.png"),u'|  动作A')

		# 将动作与处理函数相关联
		# 这里为了简单，将所有action与同一个处理函数相关联，
		# 当然也可以将他们分别与不同函数关联，实现不同的功能
		self.actionA.triggered.connect(self.actionHandler)

	def showContextMenu(self, pos):    
		'''
		右键点击时调用的函数  
		'''    
		self.count += 1  
		# 菜单显示前，将它移动到鼠标点击的位置    
		self.contextMenu.exec_(QtGui.QCursor.pos()) #在鼠标位置显示

	def actionHandler(self):
		print 2

# init config
def InitConfig(configFile, PrePath = ''):
	bExit = True
	file_dir = os.path.split(configFile)[0]
	# print configFile
	if not os.path.isdir(file_dir):
		os.makedirs(file_dir)
	if not os.path.exists(configFile):
		fp = open(configFile, 'w')
		fp.close()
		bExit = False

	if not bExit:
		Cconf = CConfig(configFile)
		Cconf.AddSection('Version')
		Cconf.UpdateValue('Version', 'Release', '1.0')

		Cconf.AddSection('IconFile')
		Cconf.UpdateValue('IconFile', 'windowIcon', PrePath + 'icon\\network.png')
		Cconf.UpdateValue('IconFile', 'sysIcon', PrePath + 'icon\\network.ico')
		Cconf.UpdateValue('IconFile', 'lockicon', PrePath + 'icon\\lock.png')
		Cconf.UpdateValue('IconFile', 'unlockicon', PrePath + 'icon\\unlock.png')

		Cconf.AddSection('Setting')
		Cconf.UpdateValue('Setting', 'iplock', '0')
		Cconf.UpdateValue('Setting', 'maclock', '0')

		Cconf.AddSection('LocadEdit')
		Cconf.UpdateValue('LocadEdit', 'serverIP', '172.16.1.1')
		Cconf.UpdateValue('LocadEdit', 'localIP', ipConfigGetIp())
		Cconf.UpdateValue('LocadEdit', 'localmac', GetMac().upper())
		
		Cconf.AddSection('LocadCombo')
		Cconf.UpdateValue('LocadCombo', 'Method', '0')
		Cconf.UpdateConfigFile()

# get file path
def MyFilePath():
	application_path = ''
	if getattr(sys, 'frozen', False):
		application_path = os.path.dirname(sys.executable)
	elif __file__:
		application_path = os.path.dirname(__file__)
	return application_path

def RetPreNpath(filePath, retN):
	file_dir = filePath
	while retN > 0:
		file_dir = os.path.split(file_dir)[0]
		retN = retN - 1
	return file_dir


if __name__ == '__main__':
	app = None
	app = QtGui.QApplication([])

	retivelyConfFile = 'config\\Config.conf'
	# py
	configFile = RetPreNpath(MyFilePath(), 1) + '\\' + retivelyConfFile
	InitConfig(configFile, '..\\')
	window = IpClientGui('..\\' + retivelyConfFile)
	# exe
	# configFile = MyFilePath() + '\\' + retivelyConfFile
	# InitConfig(configFile)
	# window = IpClientGui(retivelyConfFile)
	window.show()
	# print os.getpid()
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(str(os.getpid()))
	sys.exit(app.exec_())