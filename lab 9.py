import random
import string
import os

def ranline(n):
    line = []
    for _ in range(n):
        len = random.randint(3, 12)
        line.append("".join(random.choices(string.ascii_lowercase, k=len)))
        if random.random() > 0.5:
            line.append(random.choice([',', '.', '!', '?', ';', ':']))
        line.append(" ")
    return "".join(line)

def readfile():
    data = {}
    maxcount = 0
    with open("TF22_1.txt", "r") as file:
        for el in file:
            words = el.split()
            for word in words:
                count = 0
                for i in word:
                    if i == "a":
                        count += 1
                if count >= maxcount:
                    maxcount = count
                    if count not in data:
                        data[count] = []
                    data[count].append(word)
    if maxcount == 0:
        return "no suitable words"
    max_words = data.get(maxcount, [])
    return f"Max a --> {maxcount}\nWord/Words with {maxcount} a: {', '.join(max_words)}"

def opfile(n1=10, n2=10, n3=0):
    if n3 != 0:
        try:
            if not os.path.exists("TF22_2.txt"):
                raise FileNotFoundError
            with open("TF22_2.txt", "a") as file:
                file.write("data append:\n" + readfile() + "\n\n")
                print("completed")
        except FileNotFoundError:
            with open("TF22_2.txt", "w") as file:
                print("file TF22_2.txt not found, created a new file")
                file.write("file created:\n" + readfile() + "\n\n")
    else:
         with open("TF22_1.txt", "w") as file:
            for _ in range(n1):
                file.write(ranline(n2) + "\n")


opfile(10, 10)
opfile(n3=1)





