file = open('ospf.txt', 'r')
f = file.read().rstrip().split('\n')
#print(f)
for i in f:
    string = i.strip().split()
    string.remove('via')
    string[2].strip('[]')
    string[3].rstrip(',')
    string[4].rstrip(',')
    #print(string)
    keys = ['Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
    OSPF = dict(zip(keys,string))
    print(OSPF)

