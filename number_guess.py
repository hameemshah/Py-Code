import random

def guess():
    number = random.randint(1,100)
    guesses = difficulty()
    score = 0
    while guesses!=0:
        print(f"You have {guesses} attempts to guess the number")
        guess = int(input("Make a guess:"))
        if guess == number:
            score += 1
            print(f"You got it! The answer was {number}. Your score is {score}")
            play_again = input("Do you want to play again? (y/n)")
            if play_again == 'y':
                number = random.randint(1,100)
                guesses = difficulty()
            else:
                exit()
        elif guess>number:
            if abs(guess - number) <= 5:
                print("Too high but you are close")
            else:
                print("Too high")
            guesses-=1
        elif guess<number:
            if abs(guess - number) <= 5:
                print("Too low but you are close")
            else:
                print("Too low")
            guesses-=1
        else:
            print("Something went wrong!")
    if guesses == 0:
        print("You Lose")
        print(f"The number was {number}")
        play_again = input("Do you want to play again? (y/n)")
        if play_again == 'y':
            number = random.randint(1,100)
            guesses = difficulty()
            score = 0
        else:
            exit()

print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")
def difficulty():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
        if difficulty == 'easy':
            return 10
        elif difficulty == 'hard':
            return 5
        else:
            print("Please enter valid option")
guess()
