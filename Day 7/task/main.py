import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6
# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

placeholder = []

for i in chosen_word:
    placeholder.append("_")

print(''.join(placeholder))

tries = 0
display = placeholder
while tries < len(display):
    guess = input("Guess a letter: ").lower()
    correct_guess = False
    letter_index = 0

    # TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

    for letter in chosen_word:
        if display[letter_index] == "_":
            if letter == guess:
                display[letter_index] = letter
                # print(letter_index)
                tries += 1
                correct_guess = True

        letter_index += 1

    if not correct_guess:  # this is same as if correct_guess == False
        print(stages[lives])
        print(f"Wrong guess, You have : {lives} Lives remaining.")
        lives -= 1

    print(''.join(display))
    if lives < 0:
        print("You lose.")
        break

# print("You Won!")
