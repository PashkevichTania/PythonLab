# f = open('CAM_table.txt','r')
# print(f.read())

s = list('')

with open('CAM_table.txt', 'r') as f:
    for line in f:
        if '.' in line:
            s.append(line.rstrip())
for i in sorted(s):
    print(i)


