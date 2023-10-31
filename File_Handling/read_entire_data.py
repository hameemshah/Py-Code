input_file = open('abc.txt', 'r')
lines = input_file.readlines()
for line in lines:
    print(line, end='')
input_file.close()
