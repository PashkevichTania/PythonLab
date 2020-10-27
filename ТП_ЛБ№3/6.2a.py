
ignore = ['duplex', 'alias', 'Current configuration']

with open('config_sw1.txt','r') as f:
    for line in f:
        k = True
        for i in range(3):
            if ignore[i] in line:
                k = False
                break
        if not '!' in line and not '\n' == line[0] and k:
            print(line)