# f = open('CAM_table.txt','r')
# print(f.read())
vlan = input('enter vlan number ')
s = list('')

with open('CAM_table.txt', 'r') as f:
    for line in f:
        if '.' in line:
            s.append(line.rstrip().lstrip())
for i in sorted(s):
    if i.startswith(vlan):
        print(i)


