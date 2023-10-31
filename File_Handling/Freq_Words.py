freq = {} #empty_dictionary
file_name = 'abc.txt'
my_file = open(file_name, 'r')
for line in my_file:
    linesublist = line.split()
    for w in linesublist:
        freq[w] = freq.get(w,0) + 1 #get count associated with each key
key_list = sorted(freq) #to sort the dict
print('--Occurences of each word in the file --')
for key in key_list:
    print(key, ' ', freq[key])
my_file.close()