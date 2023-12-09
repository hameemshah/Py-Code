import random as r
from input import my_list
r.shuffle(my_list)
with open("input.txt", "w") as file:
    print("[", file=file, end="")
    for line in my_list:
        print(line, file=file, end=", ")
    print("]", file=file, end="")