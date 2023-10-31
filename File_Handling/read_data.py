input_file = open('abc.txt', 'r')
emptystr = ''
line = input_file.readline()
while line != emptystr: #EOF is encountered, '' string is returened, exit
    print(line, end='')
    line = input_file.readline()
input_file.close()