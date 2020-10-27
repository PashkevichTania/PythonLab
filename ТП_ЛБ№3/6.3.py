with open('CAM_table.txt','r') as f:
    for line in f:
        if '.' in line:
            a,b,c,d = line.split()
            print('{}    {}    {}    {}'.format(a,b,c,d))