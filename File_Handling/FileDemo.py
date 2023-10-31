outputFile = open('abc.txt', 'w')
print('First Line', file=outputFile)
print('Second Line', file=outputFile)
outputFile.close()