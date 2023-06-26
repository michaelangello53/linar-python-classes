import random

word_list = ["apple", "banana", "orange", "grape", "strawberry"]
word = random.choice(word_list)
correct_guesses = []
incorrect_guesses = []
max_guesses = 6

def display_hangman(incorrect_guesses):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |     
           -
        """
    ]

    print(stages[len(incorrect_guesses)])

while True:
    display_hangman(incorrect_guesses)
    print()

    for letter in word:
        if letter in correct_guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    
    print()

    guess = input("Enter a letter: ")

    if guess in word:
        correct_guesses.append(guess)
    else:
        incorrect_guesses.append(guess)

    if set(word) == set(correct_guesses):
        print("Congratulations! You won!")
        break

    if len(incorrect_guesses) == max_guesses:
        print("Game Over. You lost!")
        break
