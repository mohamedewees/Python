import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

placeholder = []

for i in chosen_word:
    placeholder.append("_")

print(''.join(placeholder))

tries = 0
display = placeholder
while tries < len(display):
    guess = input("Guess a letter: ").lower()

    letter_index = 0

    # TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

    for letter in chosen_word:
        if display[letter_index] == "_":
            if letter == guess:
                # print("Right")
                display[letter_index] = letter
                print(letter_index)
                tries += 1
                # letter_index += 1
            else:
                display[letter_index] == "_"
                # letter_index += 1
        letter_index += 1

    print(''.join(display))

print("You Won!")