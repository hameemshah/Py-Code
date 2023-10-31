outputFile = open('abc.txt', 'r')
for line in outputFile:
    print(line, end = '')
outputFile.close()