import csv, json

def write(name: str, type: str, data):
    if "." not in name or type == "json" or type =="csv":
        with open(name+"."+type, "w") as file:
            if type == "json":
                json.dump(data, file, indent = 4)
            elif type == "csv":
                writer = csv.writer(file)
                writer.writerows(data)
            return
    print("incorrect format")
    return

def convert(name: str, type: str, user_data = []):
    try:
        if "." not in name or type == "json" or type =="csv":
            with open(name+"."+type, "r") as file:
                new_type = ""
                if type == "json":
                    new_type = "csv"
                    load_data=list(json.load(file))
                    data = [["name", "type", "health"]]
                    for el in load_data:
                        temp = []
                        for i in data[0]:
                            temp.append(el[i])
                        data.append(temp)
                    for s in range(len(user_data)):
                        data.append(user_data[s])
                elif type == "csv":
                    new_type = "json"
                    reader = list(csv.reader(file))
                    keys = []
                    data = user_data
                    for el in range(len(reader)):
                        if el == 0:
                            for key in reader[el]:
                                keys.append(key)
                        elif el > 0 and el%2 == 0:
                            val = {}
                            for i in range(len(reader[el])):
                                val[keys[i]] = reader[el][i]
                            data.append(val)
                if input(f"file {name}.{type} prepeared to convert to {name}.{new_type}\nif want to "
                         f"change the name for the conversion file\nenter Y: ").lower() == "y":
                    name = input("enter file name: ")
                write(name=name, type=new_type, data=data)
            return
        print("incorrect format")
        return
    except FileNotFoundError:
        print(f"File {name}.{type} not found")

def add_convert(name: str, type: str):
    if "." not in name or type == "json" or type == "csv":
        data = []
        print("adding new data...")
        while True:
            an_name = input("enter name: ")
            an_type = input("enter type: ")
            an_health = input("enter HP: ")
            if type == "json":
                data.append([an_name, an_type, an_health])
            elif type == "csv":
                data.append({"name": an_name, "type": an_type, "health": an_health})
            if input("if u want add one more enter Y: ").lower() != "y":
                break
        convert(name,type,data)
        return
    print("incorrect format")
    return
#"first stutent"
first_data = [["name", "type", "health"], ["2B", "android", 10000], ["2S", "android", 7000]]
write(name="file1", type="csv", data=first_data)
convert(name="file1", type="csv")
#"second student"
add_convert(name="file1", type="json")
#"third student"
add_convert(name="file2", type="csv")