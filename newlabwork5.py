def task1():
    mas = input("give integers separated by spaces: " )
    try:
        mas = list(map(int, mas.split()))
    except ValueError:
        return("please give integers separated by spaces: ")
    s = 1
    for el in mas:
        if el != 0 and el % 2 != 0:
            s *= el
    if s == 1:
        return ("no matching elements")
    return ("result: ", s)


def task2():
    double_mas = []
    for el in range(1, 8):
        if el == 1 or el == 7:
            x = 4
        elif el == 2 or el == 6:
            x = 5
        elif el == 3 or el == 5:
            x = 6
        else:
            x = 7
        x = x * 1111111
        double_mas.append([x])
    for el in double_mas:
        res = ' '.join(map(str, el))
        print (res)


#print (task1())
#task2 ()
