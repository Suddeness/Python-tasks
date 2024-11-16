def task_one(a, b):
    if 1 <= a <= 100 and 1 <= b <= 100:
        if a > b:
            return a / b + 1
        elif a == b:
            return a + 25
        elif a < b:
            return (a*b-2)/a
    return (f'values {a,b} is incorrect')

def task_two():
    res = 0
    for i in range(1, 40, 2):
        res += i
    return (f'sum: {res} quantity: {len(range(1, 40, 2))}')

def task_three(n):
    if 1 < n < 9:
        orign = n
        l = []
        space = []
        for _ in range(1, orign + 1):
            space.append(' ')
        for i in range(1, orign + 1):
            l.append(n)
            print(f'{" ".join(map(str, space))}{" ".join(map(str, l[::-1]))}')
            n -= 1
        l = [min(l)]
        for i in range(1, orign + 1):
            print(f'{" ".join(map(str, space))}{" ".join(map(str, l[::-1]))}')
            l.append(max(l) + 1)
            space.pop()
    else:
        print(f'{n} >= 9 or => 1')

try:
    a = int(input(f'task one: write a and b (range 1 - 100): \n a = '))
    b = int(input(' b = '))
    print(task_one(a,b))
    print(f'task two: {task_two()}')
    task_three(int(input('task three write int 1 < and < 9: ')))
except ValueError:
    print('the value is wrong')
