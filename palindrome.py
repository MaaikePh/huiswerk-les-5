#Palindrome Checker
# Een Palindrome is een woord dat hetzelfde is als je het van voor naar achter leest als andersom. Bijvoorbeeld: lepel, radar en fiets zijn palindromes. Schrijf een programma dat een lijst van woorden heeft en voor elk woord aangeeft of het een palindrome is of niet.
# Het programma moet een dictionary maken waarbij de key het woord is en de value een boolean die aangeeft of het woord een palindrome is of niet.
# De dictionary moet er als volgt uitzien:
# {
#     "radar": True,
#     "fiets": False,
#     "lepel": True,
#     "python": False
# }

words = ['radar', 'fiets', 'lepel', 'python']

palindrome = {}
for word in words:
    checker = ""
    for letters in word:
        checker = letters + checker
    if word == checker:
        palindrome[word] = True
    else:
        palindrome[word] = False

print(palindrome)

#Bonus
# 2 zinnen, 1 zin is geen palindrome, de andere wel uncomment de zin die je wilt testen
# zin = "dit is een testzin om te testen of dit programma werkt"
zin = "eva can i see bees in a cave"

#Tip 1: Gebruik de replace() functie om alle spaties uit de zin te halen.

zin = zin.replace(" ", "")
palindromes = {}
checker = ""
for letters in zin:
    checker = letters + checker
    if zin == checker:
        palindromes[zin] = True
    else:
        palindromes[zin] = False

print(palindromes)