import random
name = input("Enter your name: ")
print("Good luck " + name + "!")
file = open("names.txt")
words = file.readlines()
word = random.choice(words)
word = word.lower()
word = str(word).strip('\n')
word = str(word).strip('\r')
print("Guess the characters")
guesses = str()
if ' ' in word:
    guesses += ' '
turns = 6
while turns>0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1     
    if failed == 0:
        print("\nYou Win")
        exit()
    guess = input("\n\nGuess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have " + str(turns) + " more guesses")
    if turns == 0:
        print("You Lose")
        print("The word is:", word)