
ignore = ['duplex', 'alias', 'Current configuration']

with open('config_sw1.txt','r') as f, open('config_sw1_cleared.txt','w+') as f2:
    for line in f:
        k = True
        for i in range(3):
            if ignore[i] in line:
                k = False
                break
        if not '!' in line and not '\n' == line[0] and k:
            print(line)
            f2.write(line)