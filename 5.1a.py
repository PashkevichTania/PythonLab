while True:
    try:
        a = input('Enter ip address in format 10.0.1.1,range[0-255]:')
        ip = int(a.split('.')[0])
    except ValueError:
            print('Incorrect IPv4 address')

arr = a.split('.')
for i in arr:
    if int(i)<0 or int(i)>255:
        print('incorrect IPv4 address')
if arr.__len__()<4:
    print('incorrect IPv4 address')


if ip > 0 and ip <=127:
    print(('ip address {} class A, this is unicast').format(a))
elif ip > 127 and ip <= 191:
    print(('ip address {} class B, this is unicast').format(a))
elif ip > 191 and ip <= 223:
     print(('ip address {} class C, this is unicast').format(a))
elif ip > 223 and ip <= 239:
    print(('ip address{} class D, this is multicast').format(a))
elif a == '255.255.255.255':
    print(('local broadcast').format(a))
elif a == '0.0.0.0':
    print(('unassigned').format(a))
else:
    print ('unused')