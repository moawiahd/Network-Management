#!/usr/bin/python3

#Moawiah AL-Doum - 139912
#Aya AL-Antari - 133124

from easysnmp import Session
import sys


if len(sys.argv) != 3:
    print("Please enter vaild argument")
    sys.exit(1)

com = sys.argv[1]
ip = sys.argv[2]
a = Session(hostname=ip, community=com, version=2, use_numeric = True, use_sprint_value = True)

print("{:15}{:19}{:17}{:12}".format("IP Address","MAC Address","Interface","Mapping Type"))
print("-"*12+"  "+"-"*17+"  "+"-"*16+"  "+"-"*12)

ipAddr= []
macAddr = []
interface = []
mappingType = []

oid = '1.3.6.1.2.1.2.1'

s=a.get_next(oid)
i=int(s.value)

for j in range(i):

	s = a.get_next('1.3.6.1.2.1.2.2.1.2')
	oid = s.oid+'.'+s.oid_index
	interface.append(s.value)
	s = a.get_next('1.3.6.1.2.1.4.35.1.4')
	oid = s.oid+'.'+s.oid_index
	macAddr.append(s.value)
	s = a.get_next('1.3.6.1.2.1.4.22.1.3')
	oid = s.oid+'.'+s.oid_index
	ipAddr.append(s.value)
	s = a.get_next('1.3.6.1.2.1.4.35.1.6')
	oid = s.oid+'.'+s.oid_index
	mappingType.append(s.value)
	
	print("{:16}{:20}{:20}{:18}".format(ipAddr[j],macAddr[j],interface[j],mappingType[j]))
	
	
