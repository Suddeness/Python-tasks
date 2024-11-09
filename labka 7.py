#Задано дані про n=10 співробітників фірми (прізвище, зарплата і стать). Скласти програму, яка визначає: а) прізвище особи,
# яка має найбільшу зарплату (вважати, що такий є лише один); б) прізвища чоловіка і жінки, які мають найменшу зарплату
# (вважати, що такі є і вони єдині в своїй групі співробітників).

def cust_values():
    names = {}
    genders = {}
    salaries = {}
    counting = 1

    while 1:
        ch = ''
        name = (input("write name: ").title())
        gender = (input("write gender: ").lower())
        salary = (input("write salary: "))
        ch = (input("write n for next or e for exit: ").lower())
        if ch == 'e':
            break
        elif ch != 'n':
            print("something wrong, default value n")
        names[counting] = name
        genders[counting] = gender
        salaries[counting] = salary
        counting += 1

names = {
    1: "Иван Иванов",
    2: "Мария Петрова",
    3: "Алексей Сидоров",
    4: "Оля Громова",
    5: "Сергей Кузнецов",
    6: "Наталья Лебедева",
    7: "Владимир Федоров",
    8: "Анна Васильева",
    9: "Денис Павлов",
    10: "Екатерина Соколова"
}

genders = {
    1: "male",
    2: "female",
    3: "male",
    4: "female",
    5: "male",
    6: "female",
    7: "male",
    8: "female",
    9: "male",
    10: "female"
}

salaries = {
    1: 5000,
    2: 4500,
    3: 6000,
    4: 5500,
    5: 4000,
    6: 6500,
    7: 7000,
    8: 7000,
    9: 3500,
    10: 3200
}

def a():
    max_salary_id = max(salaries, key=salaries.get)
    return names[max_salary_id], salaries[max_salary_id]

print ("max salary: ", a())

def b():
    min_male_salary = float('inf')
    min_female_salary = float('inf')
    min_male_name = ""
    min_female_name = ""

    for i in salaries:
        if genders[i] == 'male' and salaries[i] < min_male_salary:
            min_male_salary = salaries[i]
            min_male_name = names[i]
        elif genders[i] == 'female' and salaries[i] < min_female_salary:
            min_female_salary = salaries[i]
            min_female_name = names[i]
    return (min_male_name, min_male_salary), (min_female_name, min_female_salary)

(min_male_name, min_male_salary), (min_female_name, min_female_salary) =  b()
print(f"male: {min_male_name}, salary: {min_male_salary}")
print(f"famale: {min_female_name}, salary: {min_female_salary}")
