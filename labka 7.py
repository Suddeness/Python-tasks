#Задано дані про n=10 співробітників фірми (прізвище, зарплата і стать). Скласти програму, яка визначає: а) прізвище особи,
# яка має найбільшу зарплату (вважати, що такий є лише один); б) прізвища чоловіка і жінки, які мають найменшу зарплату
# (вважати, що такі є і вони єдині в своїй групі співробітників).


one_slovarik_for_all_situation = {
    5000: ["Иван Иванов", 'male'],
    4500: ["Мария Петрова", 'female'],
    6000: ["Анна Смирнова", 'female'],
    5500: ["Дмитрий Соколов", 'male'],
    4800: ["Сергей Попов", 'male'],
    5300: ["Ольга Васильева", 'female'],
    4700: ["Николай Павлов", 'male'],
    5100: ["Александр Федоров", 'male'],
    4950: ["Елена Кузнецова", 'female'],
    5200: ["Алина Морозова", 'female']
}
def sortirovka():
    keys = list(one_slovarik_for_all_situation.keys())
    keys = sorted(keys)
    n = 1
    for key in keys:
        print(f"{n}. salary: {key}, person: {one_slovarik_for_all_situation[key][0]}, gender: {one_slovarik_for_all_situation[key][1]}")
        n += 1
def del_data_from_slovarik(key):
    if key in list(one_slovarik_for_all_situation.keys()):
        ch = (input(f'do you really want to delete person: {one_slovarik_for_all_situation[key]} write yes: '))
        if ch == 'yes':
             print('completed........')
        else:
            print('failed.')
    else:
        print('no person with this salary')
def make_slovarik():
    slovarik = {}
    person = []
    n = 1
    while 1:
      if n > 10:
          print("vse mesta netu, enough!!!!!")
      try:
        name = input('write name: ')
        gender = input('who is this person (male or female)???? ').lower()
        key_or_salary = int(input('write salary for person: '))
        if gender == 'male' or gender == 'female':
            person.append(name)
            person.append(gender)
            slovarik[key_or_salary] = person
        else:
            print('this gender is wrong, try again')
      except ValueError:
          print('something wrong with your value, i think incorrect salary >_<')
      ch = input('continue? y or n: ')
      if ch == 'n':
          break
      elif ch != 'y':
          print('wrong choice, default value y')
      n += 1
    return slovarik
def a():
    max_keys_from_one_slovarik = max(one_slovarik_for_all_situation.keys())
    return max_keys_from_one_slovarik
def b():
    mans = []
    womans = []
    for el in list(one_slovarik_for_all_situation.keys()):
        list_from_one_slovarik = one_slovarik_for_all_situation[el]
        if list_from_one_slovarik[1] == 'male':
            mans.append(el)
        if list_from_one_slovarik[1] =='female':
            womans.append(el)
    omgwhatisit = [min(womans), min(mans)]
    return omgwhatisit
print('what you want to do? write integer')
while 1:
    aaa = input('1-> check max salary, 2-> check min salary, 3-> check all sort data and delete: ')
    if aaa == '1':
        print (f"max salary: {a()} this salary belong to: {one_slovarik_for_all_situation[a()][0]}")
    elif aaa == '2':
        woop = b()
        print (f"min salary for famale {woop[0]} this salary belong to {one_slovarik_for_all_situation[woop[0]][0]}")
        print (f"min salary for male {woop[1]} this salary belong to {one_slovarik_for_all_situation[woop[1]][0]}")
    elif aaa == '3':
        sortirovka()
        try:
            del_data = int(input('write salary for delete data: '))
            del_data_from_slovarik(del_data)
        except ValueError:
            print('it is not a salary (')
    else:
        print('somthing wrong')
    cc = input('next y or n: ')
    if cc == 'n':
        break
