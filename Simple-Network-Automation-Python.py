#!/usr/local/bin/python3


# Aya Al-Antari - 133124
# Moawiah Al-Doum - 139912

import sys, re
from time import sleep
from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': sys.argv[1],
    'username': 'nes470user',
    'password': 'nes470passwd',
}


arpHeader = []
arpCache = []


connection = ConnectHandler(**device)

output = connection.send_command("show arp\n") 


output = list(output)
output = "".join(output)


o1 = re.findall(r'[a-zA-Z0-9_\-.]+', output)


for i in output.splitlines()[:1]:
	h = i.split()
	for j in h:
		arpHeader.append(j)

del arpHeader[0]
del arpHeader[2]
del arpHeader[3]

arpHeader[0] = "IP Address"
arpHeader[3] = "MAC Address"
arpHeader[2] = "Mapping Type"


for i in range(1):
	print("{:17}{:20}{:19}{:5}{}".format(arpHeader[0], arpHeader[3], arpHeader[4], arpHeader[1], arpHeader[2]))

print("--------------   -----------------   ----------------   ---  ------------")


for x in range(8, len(o1)):

    if(o1[x].count('.') == 3 and o1[x+1] == '-'):
        MAC = re.sub("[.]","",o1[x+2])
        l = [2,5,8,11,14]
        for i in l:
            MAC = MAC[:i] + ':' + MAC[i:]
        
        print("{:17}{:19}{:18}{:5}{:14}".format(o1[x], MAC, o1[x+4],o1[x+1], 'Static'))


    elif (o1[x].count('.') == 3):
        MAC = re.sub("[.]","",o1[x+2])
        l = [2,5,8,11,14]
        for i in l:
            MAC = MAC[:i] + ':' + MAC[i:]
            
        print("{:17}{:19}{:18}{:5}{:14}".format(o1[x], MAC, o1[x+4],o1[x+1], 'Dynamic'))    


