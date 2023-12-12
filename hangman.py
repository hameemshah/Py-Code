import random
word_list = [
    "apple", "banana", "orange", "grape", "kiwi", "strawberry", "blueberry", "pineapple", "watermelon", "melon",
    "cat", "dog", "elephant", "lion", "tiger", "giraffe", "zebra", "cheetah", "monkey", "kangaroo",
    "car", "bus", "train", "bicycle", "motorcycle", "airplane", "helicopter", "boat", "ship", "submarine",
    "computer", "keyboard", "mouse", "monitor", "printer", "laptop", "tablet", "smartphone", "camera", "headphones",
    "school", "teacher", "student", "classroom", "book", "pen", "pencil", "notebook", "desk", "chalkboard",
    "guitar", "piano", "violin", "trumpet", "drums", "flute", "saxophone", "clarinet", "harmonica", "accordion",
    "sun", "moon", "star", "planet", "galaxy", "universe", "telescope", "astronaut", "rocket", "space",
    "mountain", "river", "ocean", "desert", "forest", "lake", "island", "volcano", "canyon", "waterfall",
    "hamburger", "pizza", "spaghetti", "sushi", "icecream", "chocolate", "sandwich", "pancake", "cupcake", "cookie"]
chosen_word = random.choice(word_list)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

while True: 
    guess = input("Guess a letter: ").lower()

    #TODO-2: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    print(display)