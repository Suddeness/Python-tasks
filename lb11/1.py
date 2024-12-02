import csv
from csv import DictReader


def write_csv():
    try:
        ndict = {}
        with open("Data.csv", "r") as file:
            reader = csv.DictReader(file)
            for r in reader:
                values = ((year, r[f"{year} [YR{year}]"]) for year in range (2014, 2024))
                for y, i in values:
                    if i not in ("..", ""):
                        ndict[y] = i
                        print(f"year: {y}; Life expectancy at birt: {i}")
        while True:
            usr_ch = int(input(" write year which data you want to enter in csv file\n  first year: "))
            usr_ch2 = int(input("  last year: "))
            if usr_ch in ndict and usr_ch2 in ndict:
                with open("NewData.csv", "w") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Years", "Life expectancy at birt"])
                    for year in range(usr_ch, usr_ch2+1):
                        if year in ndict:
                          writer.writerow([year, ndict[year]])
                    print("compleated")
                    break
            print("This years is incorrect")
    except ValueError:
        print("You have written an incorrect value")
    except FileNotFoundError:
        print("File \"Data.csv\" not found")
    finally:
        if input("if you want to try again enter Y: ").lower() == "y":
            write_csv()
        return

def check_write_csv():
    try:
        usr = int(input ("entered years which data you want to check.\npossible years 2014-2024\nfirst year: "))
        usr2 = int(input ("last year: "))
        ndict = {}
        if usr in range(2014, 2024) and usr2 in range(2014, 2024):
            with open("Data.csv", "r") as file:
                reader = csv.DictReader(file)
                for r in reader:
                   values = ((year, r[f"{year} [YR{year}]"]) for year in range (usr, usr2+1))
                   for y, i in values:
                        if i not in ("..", ""):
                            ndict[y] = i
                            print(f"year: {y}; Life expectancy at birt: {i}")
            if input("if you want to write this data in a file, enter Y: ").lower() == "y":
                with open ("NewDataFile.csv", "w") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Years", "Life expectancy at birt"])
                    for year in range(usr, usr2 + 1):
                        if year in ndict:
                            writer.writerow([year, ndict[year]])
                    print("compleated")
                    return
        print("this year is incorrect")
    except ValueError:
        print("You have written an incorrect value")
    except FileNotFoundError:
        print("File \"Data.csv\" not found")
    finally:
        if input("if you want to try again enter Y: ").lower() == "y":
            check_write_csv()
        return

def show():
    with open("Data.csv", "r") as file:
        reader = csv.reader(file)
        print("data from csv:")
        for i, el in enumerate(reader):
            print(f"{i+1}\n {el}")
            if i == 1:
                return

def mind_mid():
    tk = input("what u want to do? (enter a number)\n 1->show data, 2->write, 3->check and write")
    if tk == 1:
        show()
    elif tk == 2:
        write_csv()
    elif tk == 3:
        check_write_csv()
    else:
        print("._.")
        return
