
import random

# List of 5 predefined words
words = ["apple", "python", "school", "laptop", "garden"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

print("===== WELCOME TO HANGMAN GAME =====")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.")

while incorrect_guesses < max_incorrect_guesses:
    # Display the word with hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses, "/", max_incorrect_guesses)

    # Check if the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word:", secret_word)
        break

    guess = input("Enter one letter: ").lower().strip()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try another.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Check if the player lost
if incorrect_guesses == max_incorrect_guesses:
    print("\nGame over! The word was:", secret_word)
