#розв’язання завдань відповідно до варіанту, результат виконання завдання записати в інший JSON файл.
#Задано дані про n=10 співробітників фірми (прізвище, зарплата, посада і стать).
# Скласти програму, яка визначає: а) прізвища осіб, які мають найменшу та
# найбільшу зарплату (вважати, що такий є лише один).
import json
def individual_task():
    with open("indiv_task.json", "r") as file:
        data = json.load(file)
    temp = {}
    index = 0
    for el in data["employees"]:
        temp[el["salary"]] = index
        index += 1
    minsal, maxsal = min(temp), max(temp)
    lst_name_min, lst_name_max = data["employees"][temp[minsal]]["last_name"], data["employees"][temp[maxsal]]["last_name"]
    print(f'min salary has: {lst_name_min}')
    print(f'max salary has: {lst_name_max}')
    with open("min_max_indiv_task.json","w") as file:
        data = {
        minsal:lst_name_min,
        maxsal:lst_name_max,}
        json.dump(data, file, indent=4)

individual_task()

