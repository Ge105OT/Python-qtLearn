# -*- coding:utf-8 -*-

import platform
import os, re
import sys
def GetWinipAddrInfo():
	dictIpAddr = {};
	try:
		import netifaces
	except ImportError:
		try:
			command_to_execute = "pip install netifaces || easy_install netifaces"
			os.system(command_to_execute)
		except OSError:
			print "Can NOT install netifaces, Aborted!"
			sys.exit(1)
		import netifaces

	routingGateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
	routingNicName = netifaces.gateways()['default'][netifaces.AF_INET][1]
	dictIpAddr['R-Gateway'] = routingGateway
	dictIpAddr['R-NIC-Name'] = routingGateway

	for interface in netifaces.interfaces():
		if interface == routingNicName:
			# print netifaces.ifaddresses(interface)
			dictIpAddr['R-NIC-MAC-Address'] = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
			try:
				dictIpAddr['R-IP-Address'] = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
				# TODO(Guodong Ding) Note: On Windows, netmask maybe give a wrong result in 'netifaces' module.
				dictIpAddr['R-IP-Netmask'] = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']
			except KeyError:
				pass
	return dictIpAddr

def GetPlatForm():
	SysInfo = {};
	SysInfo['SysTem'] = platform.system()
	SysInfo['SysVer'] = platform.version()
	return SysInfo

def ipConfigGetIp():  
	SysInfo = GetPlatForm()
	match_ip_dict = ''
	patten = r''
	if re.search(r'5\.\d\.\d{4}', SysInfo['SysVer']) != None:
		patten = r'IP Address'
	else:
		patten = r'IPv4'
	bIsVm = False
	ipconfig_result_list = os.popen('ipconfig').readlines()	#执行cmd命令ipconfig，并将结果存于ipconfig_result_list
	for data in ipconfig_result_list:
		# print data
		if re.search(r'VMware', data) != None:
			bIsVm = True
		if re.search(patten, data) != None:
			if bIsVm is False:
				match_ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', data)  #由正则表达式获取ip地址
				if match_ip:
					match_ip_dict = match_ip.group()
			bIsVm = False
	return match_ip_dict

def GetMac():
	dictIp = GetWinipAddrInfo()
	return dictIp['R-NIC-MAC-Address'];

if __name__ == '__main__':
	dictIp = GetWinipAddrInfo()
	display_format = '%-30s %-20s'
	print display_format % ("R-Gateway:", dictIp['R-Gateway'])
	print display_format % ("R-NIC-Name:", dictIp['R-NIC-Name'])
	print display_format % ("R-NIC-MAC-Address:", dictIp['R-NIC-MAC-Address'])
	print display_format % ("R-IP-Address:", dictIp['R-IP-Address'])
	print display_format % ("R-IP-Netmask:", dictIp['R-IP-Netmask'])
	print ipConfigGetIp()