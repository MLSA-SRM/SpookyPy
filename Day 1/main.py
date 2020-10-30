# import the random module
import random

# input the name of the player
name = input("Enter your name: ")
print("Good luck " + name + "!")

# open and read txt file with name of movies
file = open("names.txt")
words = file.readlines()

# pick a randome movie from the txt file
word = random.choice(words)

# clean the movie name
word = word.lower()             # converting to lower case
word = str(word).strip('\n')    # removing '\n'
word = str(word).strip('\r')    # removing '\r'

# prompting user to start the game
print("Guess the characters")
guesses = str()

# check for spaces in the name and handle extra spaces
if ' ' in word:
    guesses += ' '

# main game loop with 6 wrong guesses
turns = 6
while turns > 0:
    failed = 0                      # initialize the failed flag
    for char in word:               # print currently guessed characters
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1             
    if failed == 0:                 # handle winning case
        print("\nYou Win")
        exit()
    guess = input("\n\nGuess a character: ")    
    guesses += guess                # add each guess to the list of current guesses
    if guess not in word:           # check if current guess is correct
        turns -= 1                  # handle wrong guess
        print("Wrong")
        print("You have " + str(turns) + " more guesses")
    if turns == 0:                  # handle all turns lost (6 wrong guesses)
        print("You Lose")
        print("The word is:", word)
