import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
df = pd.read_csv("comptagevelo20152.csv", sep=",")
header = df.columns.tolist()
sm, max_sm, max_month, month=0,0,0,"01"
data = {"month":months, "visitors":[]}
for i in range(len(df)-1):
    new_month = df.iloc[i, 0][3: 5]
    if month != new_month:
        if sm>max_sm:
            max_sm=sm
            max_month=month
        data["visitors"].append(sm)
        month = new_month
        sm = 0
    sm += np.nansum(df.iloc[i, 2:].tolist())
data["visitors"].append(sm)
print(f"month: {max_month} ({months[int(max_month[1])-1]})\nnumber of visitors: {int(max_sm)}")

df = pd.DataFrame(data)
plt.bar(df["month"], df["visitors"])
plt.xlabel('Month')
plt.ylabel('Num of Visitors')
plt.xticks(rotation=30)
plt.grid(True)
plt.savefig("plt.png", dpi=500)
