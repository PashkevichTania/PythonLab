import string
def ispunct(ch):
    return ch in string.punctuation


abc1 = 'abcdefghijklmnopqrstuvwxyz'
abc2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abc3 = 'абвгдежзийклмнопрстуфхцчшщъьыэюя'
abc4 = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lang = (input("Ввевдите язык (ru/en)"))
n = int(input("Введите сдвиг: "))
read = input('Введите имя файла для чтения: ')
write = input('Введите имя файла для записи: ')
res = ''

with open(read,'r') as f1, open(write,'w+') as f2:
    #for line in f1:
    st = f1.readline()
    print('Вы ввели: ',st)
    if (lang == 'ru'):
        for i in st:
            if (i == ' '):
                res += ' '
            elif (ispunct(i)):
                res += i
            elif (i.isupper()):
                res += abc4[(abc4.index(i) + n) % len(abc4)]
            else:
                res += abc3[(abc3.index(i) + n) % len(abc3)]
    else:
        for i in st:
            if (i == ' '):
                res += ' '
            elif (ispunct(i)):
                res += i
            elif (i.isupper()):
                res += abc2[(abc2.index(i) + n) % len(abc2)]
            else:
                res += abc1[(abc1.index(i) + n) % len(abc1)]
    print('Результат: ',res)
    f2.write(res)


