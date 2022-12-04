import random

#Funcion to give the final result
def result(result_value):
    if value == 1:
        print("You win")
    elif value == 0:
        print("You Lose")
    else:
        print("Draw")

#Function to compare the result between user and computer
def compare(user,computer):
    if sum(user)>21:
        print(f"The cards of computer are {computer}")
        print("Bust!")
        return 0
    elif sum(computer)==21:
        print(f"The cards of computer are {computer}")
        print("BlackJack! You Lose")
        return 0
    elif sum(user)==21:
        print("BlackJack!")
        return 1
    elif sum(computer)>21:
        print(f"The cards of computer are {computer}")
        return 1
    elif sum(user)>sum(computer):
        print(f"The cards of computer are {computer}")
        return 1
    elif sum(computer)>sum(user):
        print(f"The cards of computer are {computer}")
        return 0
    elif sum(user)==sum(computer):
        print(f"The cards of computer are {computer}")
        return 2
    else:
        return("something went wrong")

#Function to deal between the deck of cards
def deal(player):
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    player.append(random.choice(cards))

#If sum is greater than 20 the 11 becomes 1
    if sum(player)>20 and 11 in player:
        player[player.index(11)]=1
    
#Creating an empty user list to store card values
user =[]

#Getting two cards for user form the deck of cards in deal function
for _ in range(2):
    deal(user)
print(f"Your cards are {user}")

#Checking whether it is black jack to stop execution further
if sum(user)==21:
    print("BlackJack! You Won")
    exit()
    
#Creating empty list for computer 
computer = []
deal(computer)
print(f"The card of computer is {computer}")

#Giving user a choice to choose extra cards whose value is not exceeding 21
flag = 'y'
while flag=='y' and sum(user)<21:
    flag = input("Press y to deal and n to set the current values:").lower()
    if flag=='y':
        deal(user)
    print(f"Your choices are {user}")
deal(computer)

#If after seconds deals the computer has less than 16 sum, then giving it an extra deal
if sum(computer)<16:
    deal(computer)
    
#Finally calling the compare function to check the winner
value = (compare(user,computer))

#Printing winner and loser using result function
result(value)
