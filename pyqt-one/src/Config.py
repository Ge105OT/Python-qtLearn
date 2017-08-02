# -* - coding: UTF-8 -* -
# date: 2017.5.26

import ConfigParser

# 配置文件读取类
class CConfig(object):
	"""docstring for CConfig"""
	def __init__(self, confFile):
		super(CConfig, self).__init__()
		self.confFile = confFile
		self.conf = ConfigParser.ConfigParser()
		self.conf.read(confFile)

	def GetValue(self, Sectrion, key):
		return self.conf.get(Sectrion, key)

	def UpdateValue(self, Sectrion, key, value):
		self.conf.set(Sectrion, key, value)

	def AddSection(self, Sectrion):
		self.conf.add_section(Sectrion)

	def UpdateConfigFile(self):
		self.conf.write(open(self.confFile, "w"))

	def UpdateNewConfigFile(self, NewFile):
		self.conf.write(open(NewFile ,"w"))
		