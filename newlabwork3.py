def task1():
    usr = input('give me a string for task 1: ').lower()
    d = (usr[:len(usr)//2])
    return d

def task2():
    usr = input('give me a string for task 2: ').lower()
    if usr == usr[::-1]:
        return True
    return False

def task3():
    usr = input('give me a string for task 3: ').lower()
    wl = usr.split()
    rl = []
    for el in wl:
        if el[0] == 'я' and el[1] == 'к':
            rl.append(el)
    if not rl:
        return 'empty'
    return rl


x1 = task1()
x2 = task2()
x3 = task3()
print('task1: ', x1,', ', 'task2: ', x2, ', ', 'task3: ', x3)

