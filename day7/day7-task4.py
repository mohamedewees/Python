import random
import hangman_words as words
import hangman_art as art

chosen_word = random.choice(words.word_list)
print(art.logo)
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
    wrong_letter = ""

    # TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

    for letter in chosen_word:
        if display[letter_index] == "_":
            if letter == guess:
                display[letter_index] = letter
                # print(letter_index)
                tries += 1
                correct_guess = True
                print(art.stages[lives])
                print(f"****************************{lives}/6 LIVES LEFT****************************")

            else:
                wrong_letter = guess
        else:
            if letter == guess:
                print("You have already guessed this letter \'" + letter + "\'")
                correct_guess = True
                print(art.stages[lives])
                print(f"****************************{lives}/6 LIVES LEFT****************************")
        letter_index += 1

    if not correct_guess:  # this is same as if correct_guess == False
        print(f"'{wrong_letter}' Is a wrong guess, You loose a life.")
        lives -= 1
        print(art.stages[lives])
        print(f"****************************{lives}/6 LIVES LEFT****************************")

    print(''.join(display))
    if lives == 0:
        print("It was "+ chosen_word +"! You lose.")
        print(art.stages[lives])
        break
    elif tries == len(chosen_word) and lives != 0:
        print("Word to guess is: " + chosen_word)
        print("You Won")
