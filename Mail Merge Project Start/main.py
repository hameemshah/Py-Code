#TODO: Create a letter using starting_letter.txt
with open('./input/Letters/starting_letter.txt', 'r') as input_file:
    letter_list = input_file.readlines()
    with open('./input/Names/invited_names.txt', 'r') as name_file:
        name_list = name_file.readlines()
        for name in name_list:
            new_list = letter_list[0].replace("[name]", name.strip())
            print(new_list)
    #print(contents)
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp