import json

check_list = ['name']
students_id = {
    1: ['name', 'group', 'course']
}

groups = {
    'group': {
        'english': {
            'name': [5, 3, 4]
        },
        'math': {
            'name': [3, 4]
        },
        'programming': {
            'name': [5, 4]
        }
    }
}

def load_data():
    global students_id, groups
    try:
        with open('students_data.json', 'r') as f:
            data = json.load(f)
            students_id = data['students_id']
            groups = data['groups']
            students_id = {int(k): v for k, v in data['students_id'].items()}
    except FileNotFoundError:
        print('data not found, starting without previous data')


def safe_data():
    data = {
        'students_id': students_id,
        'groups': groups,
    }
    with open('students_data.json', 'w') as f:
        json.dump(data, f, indent=4)

def show():
    load_data()
    keys = list(students_id.keys())
    print('Possible IDs:', keys)
    ch = int(input('Choose ID: '))
    if ch in students_id:
        stud_data = list(students_id[ch])
        print(stud_data)
        print(stud_data[1])
        print(groups.keys())
        keys1 = list(groups[str(stud_data[1])].keys())
        print (keys1)
        pr_data = {}
        for key1 in keys1:
            ddt2 = groups[stud_data[1]][key1]
            pr_data[key1] = ddt2
        print(f'students data: {stud_data} ,subjects data {pr_data}')
    else:
        print("Invalid ID chosen.")


def add():
    while True:
        key_count = max(students_id.keys()) + 1
        name = input('Write name: ')
        group_name = input('Write group: ')
        course = input('Write course: ')

        if name not in check_list:
            check_list.append(name)
            students_id[key_count] = [name, group_name, course]
        else:
            ch = input('This person has already been added. Do you want to try again (y or n)? ')
            if ch.lower() != 'y':
                break

        if group_name not in groups:
            ch = input(f'No such group: {group_name}. Do you want to add this group? (y or n): ').lower()
            if ch == 'y':
                group_name = input('Write new group name: ')
                groups[group_name] = {}

                while True:
                    try:
                        subjects = input('Write subjects separated by space: ').split()
                        for subject in subjects:
                            groups[group_name][subject] = []
                    except ValueError:
                        print('Something wrong with your values, please try again.')
                    print('New group has been added.')
                    break
            else:
                while True:
                    print("Please enter a valid group name.")
                    group_name = input(f"Choose a correct group from these options: {list(groups.keys())}: ")
                    if group_name in groups:
                        break
                    else:
                        print("Incorrect value, please try again.")

        subjects = list(groups[group_name].keys())
        for el in subjects:
            while True:
                try:
                    rt = input(f'Write the grade/grades for the subject "{el}", it must be integers: ')
                    rt = [int(x) for x in rt.split()]
                    groups[group_name][el] = rt
                    print(f'Grades for {el} added: {rt}')
                    break
                except ValueError:
                    print('Wrong grade/grades, please try again.')
        safe_data()
        break


while 1:
    chokopai = input("write a number what you want to do (check person [1], added a new person [2]: ")
    if chokopai == '1' or chokopai == '[1]':
        show()
    elif chokopai == '2' or chokopai == '[2]':
        add()
    else:
        print('invalid value, try again')
    ch = input('do you want continue (y or n): ').lower()
    if ch == 'n':
        break
    elif ch != 'y':
        print('invalid value, default value y ')
