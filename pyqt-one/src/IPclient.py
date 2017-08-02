# -*- coding:UTF-8 -*-
# date: 2017.5.25

import socket, numpy

def send_handshake(mac, ip, isp, server):
	localInfo = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
						   0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
						   0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
						   0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
						   0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
						   0xac, 0x10, 0x40, 0x12, 0x30, 0x30,
						   0x3a, 0x31, 0x46, 0x3a, 0x31, 0x36,
						   0x3a, 0x32, 0x32, 0x3a, 0x42, 0x38,
						   0x3a, 0x45, 0x43, 0x00, 0x00, 0x00,
						   0x03, 0x00, 0x00, 0x00, 0x00, 0x00])
	s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	addr = (server, 20015)
	s1.connect(addr)
	ispKey = 0x4e67c6a7
	localInfo[0] = '1'
	nmac = len(mac)
	nInfo = len(localInfo)
	ipaddress = [0, 0, 0, 0]
	fff = ip.split('.')
	for k in range(0, 4):
		ipaddress[k] = int(fff[k])
	print(ipaddress)

	for i in range(0, 4):
		localInfo[i + 30] = ipaddress[i]
	# print(nInfo)
	print "connect success!"

	for i in range(0, nmac):
		localInfo[i + 34] = mac[i]
		localInfo[54] = isp

	#----------------
	ESI = int(0)
	EBX = int(0)
	ECX = int(0)
	ESI2 = int(0)
	ECX = int(ispKey)
	for i in range(0, nInfo - 4):
		ESI = ECX
		ESI = numpy.int64(ECX << 5)
		if (ECX > 0):
			EBX = ECX
			EBX = ECX >> 2
		else:
			EBX = ECX
			EBX = ECX >> 2
			EBX = EBX | (0xC0000000)
		ESI = ESI + int(localInfo[i])
		EBX = numpy.int64(EBX + ESI)
		ECX = ECX ^ EBX
	ECX = ECX & (0x7FFFFFFF)

	for i in range(0,4):
		keypart = ((ECX >>( i * 8)) &0x000000FF)
		localInfo[nInfo - (4 - i)] = keypart
	s1.send(localInfo)

	for i in range(0,4):
		keypart = ((ECX >>( i * 8)) &0x000000FF)
		localInfo[nInfo - (4 - i)] = keypart
	s1.send(localInfo)

if __name__=="__main__":
    mac = "B0:25:AA:16:B5:8F"
    ip = "10.21.124.136" ##!!!!ip is local machine's ip address but not router's ip
    isp = 0x01
    ###isp  0x01(China Unicom)  0x02(China Telecom)  0x03(China Mobile) ###
    server = '172.16.1.1'
    send_handshake(mac, ip, isp, server)
    exit