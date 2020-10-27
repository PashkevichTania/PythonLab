file = open('config_sw1.txt', 'r')
f = file.read().lstrip().rstrip().split('\n')
#print(f)
for i in f:
    if i.startswith('!') != 1:
        print(i)

