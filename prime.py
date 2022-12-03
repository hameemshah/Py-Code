#Write your code below this line 👇
def prime_checker(number):
  flag = True
  for i in range(2,number):
    if number%i == 0:
      flag = False
  if flag:
    print("Prime")
  else:
    print("Not Prime")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)