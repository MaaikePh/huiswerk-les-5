zin = input("Geef hier je zin op: ")
# woorden = zin.split()
# aantal_woorden = len(woorden)
# print("Aantal woorden:", aantal_woorden)


aantal_woorden = {}

woorden = zin.split()
for woord in woorden:
    if woord in aantal_woorden:
        aantal_woorden[woord] += 1
    else:
        aantal_woorden[woord] = 1

print(aantal_woorden)