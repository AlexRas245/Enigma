def shifrator(string_1, code, k):
    lenstr = len(string_1)
    lencode = len(code)
    if k == 1:
        string_1 = string_1.ljust(lenstr + (lencode - lenstr % lencode) % lencode, "|")
        lenstr = len(string_1)
    count = int(lenstr / lencode)
    p1 = 0
    p2 = lencode
    string_2 = ''
    for i in range(count):
        helpstr = string_1[p1:p2]
        for j in code:
            string_2 += str(helpstr[int(j)])
        p1 = p2
        p2 = p2 + lencode
    if k == 2:
        while string_2[-1] == '|':
            string_2 = string_2[:-1]
    return repr(string_2)


print('Здравствуйте, вас приветствует программа "Enigma", я помогу вам зашифровать и расшифровать сообщение.')
while True:
    print('Хотите начать? \n1 - да,\n0 - выйти.')
    num = input()
    if num != '0' and num != '1':
        print('Некорректные данные. Начнем заново.')
    else:
        if num == '1':
            print('1 - зашифровать сообщение,\n2 - расшифровать сообщение.')
            k = input()
            try:
                k = int(k)
            except ValueError:
                print('Некорректные данные. Начнем заново.')
            if k == 1 or k == 2:
                string = input('Введите сообщение\n')
                code = input('Введите шифр - каждое число через пробел\n').split()
                try:
                    code = list(map(int, code))
                except ValueError:
                    print('Некорректные данные. Шифр должен состоять из цифр.')
                print(shifrator(string, code, k))
            else:
                print('Некорректные данные. Начнем заново.')
        else:
            exit()
