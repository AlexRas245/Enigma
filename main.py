def shifrator(string_1, code_1, num_1):
    if num_1 == 2:
        code_1 = code[::-1]
    code_1 = list(map(int, code_1))
    lenstr = len(string_1)
    lencode = len(code_1)
    if num_1 == 1:
        string_1 = string_1.ljust(lenstr + (lencode - lenstr % lencode) % lencode, "\0")
        lenstr = len(string_1)
    count = int(lenstr / lencode)
    p1 = 0
    p2 = lencode
    string_2 = ''
    for i in range(count):
        helpstr = string_1[p1:p2]
        for j in code_1:
            string_2 += str(helpstr[j])
        p1 = p2
        p2 = p2 + lencode
    if num_1 == 2:
        while string_2[-1] == '\0':
            string_2 = string_2[:-1]
    return string_2


def shifrator_1(string_1, code_1, num_1):
    if num_1 == 2:
        code_1 = code_1[::-1]
    code_1 = list(map(int, code_1))
    lencode = len(code_1)
    if num_1 == 1:
        string_1 = string_1.split()
        lenstr = len(string_1)
        while len(string_1) != lenstr + (lencode - lenstr % lencode) % lencode:
            string_1.append('\0')
    elif num_1 == 2:
        string_1 = list(string_1.replace(' ', ' \0 ').split(' '))
    lenstr = len(string_1)
    count = int(lenstr / lencode)
    p1 = 0
    p2 = lencode
    string_2 = []
    for i in range(count):
        helpstr = string_1[p1:p2]
        for j in code_1:
            string_2.append(str(helpstr[j]))
        p1 = p2
        p2 = p2 + lencode
    string_3 = ''
    if num_1 == 1:
        for i in string_2:
            string_3 += i
    elif num_1 == 2:
        for i in string_2:
            string_3 += i + ' '
        string_3 = string_3.replace(' \0', '')
        string_3 = string_3[:-1]
    return string_3


def check_code(code_1):
    if len(code_1) == 0:
        print('Вы ничего не ввели.')
        return False
    else:
        try:
            code_1 = list(map(int, code_1))
        except ValueError:
            print('Некорректные данные. Ключ должен состоять из чисел.')
            return False
        maxc = max(code_1)
        if len(set(code_1)) != maxc + 1:
            print('Некорректные данные. В ключе пропущены числа или есть повторяющиеся.')
            return False
        return True


def check_num(num_1):
    if len(num_1) == 0:
        print('Вы ничего не ввели.')
        return False
    else:
        try:
            num_1 = int(num_1)
        except ValueError:
            print('Некорректные данные. Начнем заново.')
            return False
    if num_1 != 0 and num_1 != 1 and num_1 != 2:
        return False
    return True


def check_string(string_1):
    if len(string_1) == 0:
        print('Вы ничего не ввели.')
        return False
    return True


def check_z(z_1):
    if len(z_1) == 0:
        print('Вы ничего не ввели.')
        return False
    else:
        try:
            z_1 = int(z_1)
        except ValueError:
            print('Некорректные данные. Начнем заново.')
            return False
    if z_1 != 1 and z_1 != 2 and z_1 != 3:
        return False
    return True


def check_lenb(lenb_1):
    pass

print('Здравствуйте, вас приветствует программа "Enigma", я помогу вам зашифровать и расшифровать сообщение.')
while True:
    print('1 - зашифровать сообщение\n2 - расшифровать сообщение\n0 - выйти')
    num = input()
    if check_num(num):
        num = int(num)
        if num == 1 or num == 2:
            string = input('Введите сообщение\n')
            if check_string(string):
                if num == 1:
                    print('Как вы хотите зашифровать сообщение?\n1 - посимвольно \n2 - по словам \n3 - по блокам')
                else:
                    print('Как было зашифровано сообщение?\n1 - посимвольно \n2 - по словам \n3 - по блокам')
                z = input()
                if check_z(z):
                    z = int(z)
                    code = input('Введите ключ - каждое число через пробел\n').split()
                    if check_code(code):
                        if z == 1:
                            print(shifrator(string, code, num))
                        elif z == 2:
                            print(shifrator_1(string, code, num))
                        else:
                            lenb = input('Введите длину блока\n')
                            if check_lenb(lenb):
                                pass
        else:
            exit()
