import csv
import matplotlib.pyplot as plt

x=[]
y=[]
z=[]
def grfk(name,n=0):
    plt.title('Population, ages 7-11, total', fontsize=15)
    plt.xlabel('Year', fontsize=12, color='red')
    plt.ylabel('Indicator', fontsize=12, color='red')
    plt.grid(True)
    if n == 0:#2.1
        plt.plot(x, y, label="First_Country", color="purple")
        plt.plot(x, z, label="Second_Country", color="yellow")
    else:#2.2
            usr_inp = (input("enter country (first/second): ")).lower()
            if usr_inp == "first":
                plt.bar(x,y)
            elif usr_inp == "second":
                plt.bar(x, z)
            else:
                print("wrong value")
    plt.savefig(name, dpi=300)
    plt.close()

with open("data_file.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        if len(line)>=3:
            x.append(int(line[0]))
            y.append(int(line[1]))
            z.append(int(line[2]))
    grfk("plot2.png")
    grfk("plot3.png",1)
