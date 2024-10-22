from part1 import task2
def task1(a):
    import math
    result = math.tan(math.radians(3*a))
    return result

print('task1')
value = int(input('give me ur value for a: '))
print("result (z): ", task1(value))

print('task2')
value1 = int(input('give me ur value for x: '))
value2 = int(input('give me ur value for n: '))
print("result (z): ", task2(value1, value2))
