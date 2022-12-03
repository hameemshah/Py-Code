import random
def guess():
    number = random.randint(1,100)
    guesses = difficulty()
    while guesses!=0:
        print(f"You have {guesses} attempts to guess the number")
        guess = int(input("Make a guess:"))
        if guess == number:
            print(f"You got it! The answer was {number}")
            exit()
        elif guess>number:
            print("Too high")
            guesses-=1
        elif guess<number:
            print("Too low")
            guesses-=1
        else:
            print("Something went wrong!")
    if guesses == 0:
        print("You Lose")
        print(f"The number was {number}")
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")
def difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5
    else:
        print("Please enter valid option")
guess()
