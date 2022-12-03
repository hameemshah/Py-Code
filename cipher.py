def encode(message,shift):
    encoded_message = []; cipher = [];
    for i in range(0,len(message)):
        encoded_message.append(ord(message[i])+int(shift))
        cipher.append(chr(encoded_message[i]))
    return cipher
def decode(message,shift):
    decoded_message = ord(message)-int(shift)
    return chr(decoded_message)
print("Welcome to cipher")
task = input("Enter E for encoding and D for decoding:").lower()
char_list = []
if(task == 'e'):
    message = input("Enter the message:")
    shift = input("Enter the shift")
    for i in message:
        char_list.append(i)
    print(encode(char_list,shift))
elif(task == 'd'):
    message = input("Enter the message and shift:")
    shift = input("Enter the shift")
    print(decode(message,shift))
else:
    print("Wrong Input")