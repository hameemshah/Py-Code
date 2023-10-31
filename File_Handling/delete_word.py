import os.path
if os.path.isfile('abc.txt'):
    infile=open('abc.txt','r')
    s=input('Enter the word you want to delete -->')
    contents=infile.read()
    newcontents=contents.replace(s,'')
    print(newcontents)
    infile=open('abc.txt','w')
    infile.write(newcontents)
    infile.close()
else:
    print("File does not exist")