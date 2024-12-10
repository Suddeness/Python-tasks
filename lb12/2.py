import json

def create(n=0, flname = "Newfile.json", data = {} ):
    data = data
    if n == 0:
        if input("if u want to add some data enter Y: ").lower() == "y":
            while True:
                key, value = input("enter key: "), input("enter value: ")
                data[key]=value
                if input("enter Y if u want continue: ").lower() != "y":
                    break
    with open(flname, "w") as file:
        json.dump(data, file, indent=4)

def show(n=0, flname = "Newfile.json"):
    try:
        with open(flname, "r") as file:
            datafile = json.load(file)
            if n == 1:
                return (datafile)
            else:
                count = 0
                for key, value in datafile.items():
                    count += 1
                    print(f"{count}. key: {key}  value: {value}; ")
                print(f"total {count} entries")
    except FileNotFoundError:
        if input("file not found, enter Y if u want to create new: ").lower() == "y":
            create()
    except json.JSONDecodeError:
        print("something wrong with json file")
        if input("if u want to create a new file enter Y: ").lower() == "y":
            create()

def add_del():
    usr = input("enter [1 -> add] or [2 -> delete]: " )
    if usr == "1":
        data = show(1)
        newdata = {}
        while True:
            ukey = input("enter new key for value: ")
            uval = input("enter new value: ")
            if ukey in data:
                if input("this key already in the file, if u want rewrite enter Y: ").lower() == "y":
                    pass
                else:
                    for el in range (1, 101):
                        ukey += f"({str(el)})"
                        if ukey not in data:
                            break
            newdata[ukey] = uval
            data.update(newdata)
            if  input("enter Y if u want to add one more: ").lower() != "y":
                break
        create(n=1, data=data)
    elif usr =="2":
        while True:
            usrk = input("enter key for delete data or show if u want to see all data: ")
            if usrk.lower() == "show":
                show()
                usrk = input("enter key for delete: ")
            other_data = show(1)
            if usrk not in other_data:
                print("there is no such key")
            else:
                old_val = other_data.pop(usrk)
                create(1, data=other_data)
                print (f"({usrk}--{old_val}) deleted")
                break
    else:
        print("you entered wrong value, pls try again")

def find():
    ukey = input("Enter key to find some data: ")
    data = show(1)
    found_data = {}
    if ukey in data:
        print(f"Data found: key {ukey} value {data[ukey]}")
        found_data[ukey] = data[ukey]
    else:
        print("Key not found.")
        if input("Do you want to find by value? (y or n): ").lower() == "y":
            val = input("Enter value: ")
            for key, value in data.items():
                if value == val:
                    print(f"Data found: key ({key}) value ({value})")
                    found_data[key] = value
    return found_data

def individual_task():
    data = show(1,"data.json")
    temp = {}
    index = 0
    for el in data["employees"]:
        temp[el["salary"]] = index
        index += 1
    minsal, maxsal = min(temp), max(temp)
    lst_name_min, lst_name_max = data["employees"][temp[minsal]]["last_name"], data["employees"][temp[maxsal]]["last_name"]
    print(f'min salary has: {lst_name_min}')
    print(f'max salary has: {lst_name_max}')
    create(n=1, flname="newdata.json" ,data = {
        minsal:lst_name_min,
        maxsal:lst_name_max,
    })

def midline():
    while True:
        us = input("1->create new file \n2->show all data \n3->add/delete data \n4->find data "
                   "\n5->individual task \nenter a number or break: ")
        if us == "1":
            create()
        elif us == "2":
            show()
        elif us == "3":
            add_del()
        elif us == "4":
            find()
        elif us == "5":
            individual_task()
        elif us.lower() == "break":
            break
        else:
            print("incorrect value pls try again")
            continue
        if input("continuing? y/n: ").lower() == "y":
            continue
        break

midline()