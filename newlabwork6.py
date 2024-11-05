#1. Розбиття списку на два списки за вказаним порядковим номером елемента для розбиття.
def rozbifka():
    try:
      ls = list(map(int, input("give integers separated by space: ").split()))
      ch = int(input("write after which element you want to split the line: "))
    except ValueError:
        return "wrong values, give integers separated by space"
    while 1:
        if ch < 0 or ch >= len(ls):
            print ("wrong value for split")
            ch = int(input("write after which element you want to split the line: ")) + 1
        else:
            break
    part1 = ls[0: ch]
    part2 = ls[ch:]
    return "list:", ls, "part num 1:", part1, "part num 2:", part2

#print(rozbifka())

#2. Знайти найдовше слово в списку.
def nahodka ():
    while 1:
        ls = list(input("give strings separated by space: ").split())
        if not ls:
            print ("ur list is empty")
        else:
            break
    maxstr = ""
    for el in ls:
        if len(el) > len(maxstr):
            maxstr = el
    return "longest word is: " + maxstr

#print(nahodka())
#3. Маємо деякий набір продуктових товарів n, асортимент магазину – це множина товарів з цього набору.
# Компанія володіє m магазинами. За інформацією щодо асортименту, наданому кожним з цих магазинів,
# скласти програму, яка сформує В – множину продуктів, яких немає в жодному магазині.
def shop():
    N = set(list(input("set of products n = ").split()))
    M = input("how many shops m = ")
    ll = set()
    for el in range(1, int(M) + 1):
        x = set(input("who's products in shop " + str(el) + ": " ).split())
        ll.update(x)
    B = N - ll
    return "this products not in shops " + str(B)

print (shop())