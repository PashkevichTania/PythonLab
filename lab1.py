#3.1
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
NewNAT = NAT.replace('Fast','Gigabit')
print(NewNAT)
#3.2
MAC = 'AAAA:BBBB:CCCC'
NewMAC = MAC.replace(':','.',2)
print(NewMAC)
#3.3
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
commands = CONFIG.strip().split()
Vlans = commands[-1].split(',')
print(Vlans)
#3.4
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
commands1 = command1.strip().split()
commands2 = command2.strip().split()
vlans1 = set(commands1[-1].split(','))
vlans2 = set(commands2[-1].split(','))
vlans = vlans1.intersection(vlans2)
print('vlans=',vlans)
#3.5
VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
NewVLANS = sorted(list(set(VLANS)))
print(NewVLANS)
#3.6
ospf_route = 'OSPF        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
string = ospf_route.strip().split()
string.remove('via')
string[2].strip('[]')
string[3].rstrip(',')
string[4].rstrip(',')

keys = ['Protocol','Prefix','AD/Metric' ,'Next-Hop','Last update','Outbound Interface']
ospf = dict(zip(keys,string))
print(ospf)
#3.7
MAC = 'AAAA:BBBB:CCCC'
print(''.join(format(ord(i),'b')for i in MAC.replace(':','')))
#3.8
IP = '192.168.3.1'
IP = IP.split('.')
for i in IP:
    print(i, end="         ")
print('')
for i in IP:
   print((bin(int(i)+256)).replace('0b',''),end="  ")
#3.9
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
print('')
el = input('Enter element ')
try:
    if el.isdigit():
        print(num_list.index(int(el)))
    else:
        print(word_list.index(el))
except ValueError:
    print('There is no such thing in the lists')

