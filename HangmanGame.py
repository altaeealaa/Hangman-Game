"""Design a text-based Hangman game. The program
selects a random word, and the player guesses one
letter at a time to uncover the word. You can set a
limit on the number of incorrect guesses allowed."""

import random
words = ["python", "game", "hangman", "challenge", "program", "computer", "science"]
random_word = random.choice(words).lower()

#variables initialization
guessed_letters = set()
display_word = ["_"] * len(random_word)
max_incorrect_guesses = 5
incorrect_guesses = 0

print("Welcome to Hangman Game! \n")
#print(f"Word: {display_word}")

while incorrect_guesses < max_incorrect_guesses and '_' in display_word:
    guess = input("Enter a letter to guess the word: ").lower()

    if(len(guess)!= 1 or not guess.isalpha):
        print("Please enter a single letter")
        continue

    if guess in guessed_letters:
        print(f"You already guessed the letter {guess}! Try again")
        continue

    if guess in random_word:
        print(f"Very Good! The letter {guess} is in the word")
        guessed_letters.add(guess)

        for i in range(len(random_word)):
            if random_word[i] == guess:
                display_word[i] = guess

    else:
        print("This letter is not in the word :(")
        incorrect_guesses += 1
        print(f"you still have {max_incorrect_guesses - incorrect_guesses} tries left")

    print(f"Word: {' '.join(display_word)}")

if '_' not in display_word:
    print(f"Congratulation! you guessed the word {random_word} correctly!")
else:
    print(f"You didn't guess the word. The word is '{random_word}'. Hard luck next time!")

print("\n-------------------------End of Hungman Game----------------------------------")






