import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','@', '#', '$', '%', '^', '&', '(', ')', '*', '+', '_', '-', '=']


print('Welkom bij het maken van jouw wachtwoord.')
aantal_letters = int(input('Hoeveel letters wil je in je wachtwoord? '))
aantal_symbols = int(input('Hoeveel symbolen wil je in je wachtwoord? '))
aantal_numbers = int(input('Hoeveel nummers wil je in je wachtwoord? '))

wachtwoord = ""

for i in range(0, aantal_letters):
    wachtwoord += random.choice(letters)
for i in range(0, aantal_symbols):
    wachtwoord += random.choice(symbols)
for i in range(0, aantal_numbers):
    wachtwoord += random.choice(numbers)
print(f'Je wachtwoord is:', wachtwoord)

lijst = []

for i in range(0, aantal_letters):
    lijst.append(random.choice(letters))
for i in range(0, aantal_symbols):
    lijst.append(random.choice(symbols))
for i in range(0, aantal_numbers):
    lijst.append(random.choice(numbers))

random.shuffle(lijst)
print(f'Je wachtwoord is:')
print("".join(lijst))