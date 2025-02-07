
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = 5
nr_symbol = 3
nr_numbers = 4
pass_letters = []
pass_symbols = []
pass_numbers = []

for i in range(0,nr_letters):
    rand_letter = letters[random.randint(0,len(letters)-1)]
    pass_letters.append(rand_letter)

for j in range(0,nr_symbol):
    rand_symbol = symbols[random.randint(0,len(symbols)-1)]
    pass_symbols.append(rand_symbol)

for k in range(0,nr_numbers):
    rand_number = numbers[random.randint(0,len(numbers)-1)]
    pass_numbers.append(rand_number)

ordered_pass = pass_letters + pass_symbols + pass_numbers
print(ordered_pass)
random.shuffle(ordered_pass)
print("Your Password Is: " + str(''.join(ordered_pass)))
