import random
questions = {
    1: "What is Python, and what is it used for?",
    2: "What is the difference between lists and tuples in Python?",
    3: "How do lambda functions work, and what are their advantages?",
    4: "What are decorators in Python, and how do you use them?",
    5: "What are the main data types in Python?",
    6: "How can you handle exceptions in Python?",
    7: "What is list comprehension, and how is it used?",
    8: "What is the difference between the append() and extend() methods in a list?",
    9: "How does the os module work? Provide examples of its use.",
    10: "What is the GIL in Python, and how does it affect multithreading?"
}
answers = {
    1: "Python is a high-level programming language used for web development, data analysis, machine learning, and more.",
    2: "Lists are mutable, while tuples are immutable. Tuples are faster and suitable for unchangeable data.",
    3: "Lambda functions are short, anonymous functions used for one-line operations, e.g., in map() or filter().",
    4: "Decorators are functions that modify or extend the behavior of other functions, applied using @.",
    5: "Main data types: int, float, str, bool, list, tuple, dict, set, NoneType.",
    6: "Exceptions are handled using the try-except construct.",
    7: "List comprehension creates lists in a single line using loops and conditions.",
    8: "Append adds a single element to the list, while extend adds elements from another iterable.",
    9: "The os module interacts with the operating system, e.g., managing files, directories, and processes.",
    10: "The GIL (Global Interpreter Lock) limits Python to executing one thread at a time, affecting CPU-bound tasks."
}
def clear():
    if input("do you want clear file? yes/no: ") == "yes":
        print("the file has been cleared")
        with open("newfile.txt", "w") as file:
            pass
    else:
        print("the file was not cleared")

def main (n):
    try:
        if n % 2 != 0:
            n += 1
        elif n == 0:
            print("haha thats funny i guess you have no questions...")
            return
        temp = [0, 0, list(questions.keys())]
        for i in range(n):
            if temp[0] == 0:
                randomize = random.choice(temp[2])
                temp[0],temp[1] = 1, randomize
            with open("newfile.txt", "a") as file:
                file.write(f"Yakovenko Maksym, question:\n{questions[temp[1]]}\n")
                file.write(f"Yakovenko Maksym, answer:\n{answers[temp[1]]}\n\n")
                temp[2].remove(temp[1])
                temp[0] = 0
        print("complete")
    except IndexError:
        print("no more questions")
    finally:
         clear()

while True:
    try:
        main(int(input(f"enter the number of cycles, max number -> {len(questions.keys())}: ")))
        break
    except ValueError:
        print("you need to write integer, please try again")
