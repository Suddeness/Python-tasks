import json, os
# виведення на екран вмісту JSON файлу;
def show(flname = "Newfile.json", n=0):
    try:
        with open(flname, "r") as file:
            data = json.load(file)
            if n == 0:
                for i,key in enumerate(data):
                    print(f"{i}: key[{key}]: value[{data[key]}")
        return data
    except FileNotFoundError:
        print("file not found")

# пошук даних у JSON файлі за одним із полів на вибір;
def find(flname = "Newfile.json"):
    data = show(flname,1)
    while True:
        key = input("enter key: ")
        if key in data:
            print(f"file found\nkey[{key}]:val[{data[key]}]")
            break
        else:
            print("Key not found, try again.")
        if input("if u want find more, enter Y: ").lower() != "y":
            break

# додавання нового запису у JSON файл;
def add(flname = "Newfile.json"):
    if not os.path.exists(flname):
        data = {}
        new = False
        if (input(f"file {flname} not found\nif u want to create new enter Y: ")).lower() != "y":
            return
        else:
            new = True
        if not new:
            data = show(flname,1)
        while True:
            k = input("enter key: ")
            v = input("enter value: ")
            data[k] = v
            if (input("if u want add more, enter Y: ")).lower() != "y":
                break
        with open(flname, "w") as file:
            json.dump(data, file, indent=4)

#видалення запису JSON файл;
def dlt(flname = "Newfile.json"):
    data = show(flname, n=1)
    new_data = {}
    found = False
    while True:
        key = input("enter key: ")
        for el in data:
            if key == el:
                print(f"file deleated\nkey[{key}]:val[{data[key]}")
                found = True
            else:
                new_data[el] = data[el]
        if found:
            break
        else:
            print("Key not found. Try again.")
            continue
    with open(flname, "w") as file:
        json.dump(new_data, file, indent=4)

while True:
    usr = input("Select an option:\n 1 - Add data\n 2 - Show data\n 3 - Find data\n 4 - Deleat data\n 5 - Exit\ninput: ")
    if usr == "5":
        break
    flname = input("enter file name: ")
    if usr == "1":
        add(flname)
    if usr == "2":
        show(flname)
    if usr == "3":
        find(flname)
    if usr == "4":
        dlt(flname)
