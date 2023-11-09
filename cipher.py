def encode(msg,sft):
    cipher = [];
    for char in msg:
        cipher.append(chr(ord(char)+int(sft)))
    return cipher

def decode(msg,sft):
    decipher = [];
    for char in msg:
        decipher.append(chr(ord(char)-int(sft)))
    return  decipher

print("Welcome to cipher")
task = input("Enter E for encoding and D for decoding: ").lower()

if(task == 'e'):
    message = input("Enter the message:")
    shift = input("Enter the shift:")
    print("".join(encode(message,shift)))
elif(task == 'd'):
    message = input("Enter the message:")
    shift = input("Enter the shift:")
    print("".join(decode(message,shift)))
else:
    print("Wrong Input")