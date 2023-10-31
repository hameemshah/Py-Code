output_file = open('def.txt', 'w')
strList = ['First Line\n', 'Second Line\n', 'Third Line']
for line in strList:
    output_file.writelines(line)
output_file.close()