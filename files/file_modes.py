with open('hello.txt', "r") as file:
    contents = file.read()
    print(contents)

score = int(contents) + 10

score = str(score)

with open('hello.txt', "w") as file:
    file.write(score)

with open('hello.txt', "r") as file:
    contents = file.read()
    print(contents)