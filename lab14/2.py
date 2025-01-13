import csv
import matplotlib.pyplot as plt

x=[]
y=[]
z=[]
with open("data_file.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        if len(line)>=3:
            x.append(int(line[0]))
            y.append(int(line[1]))
            z.append(int(line[2]))
plt.plot(x,z,label="First_Country", color="purple")
plt.plot(x,y,label="Second_Country", color="yellow")
plt.title('Population, ages 7-11, total', fontsize=15)
plt.xlabel('Year', fontsize=12, color='red')
plt.ylabel('Indicator', fontsize=12, color='red')
plt.legend()
plt.grid(True)
plt.savefig("plot2.png",dpi=300)


fig, ax = plt.subplots()
ax.pie(y, labels = x)
ax.axis("equal")
plt.legend()
plt.savefig("plot3.png",dpi=300)