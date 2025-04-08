# Boeken geleend door Groep 1
groep1 = ["Harry Potter", "De Hobbit", "De Da Vinci Code", "De Hobbit", "De Da Vinci Code", "Twilight", "De Vijfde Golf", "Harry Potter", "De Hobbit"]

# Boeken geleend door Groep 2
groep2 = ["De Da Vinci Code", "De Alchemist", "Harry Potter", "De Hobbit", "Twilight", "The Hunger Games", "Gone Girl", "Twilight", "De Hobbit"]

set_1 = (set(groep1))
set_2 = (set(groep2))

print(set_1)
print(set_2)
print(set_1.intersection(set_2))
print(set_1.difference(set_2))
print(set_2.difference(set_1))

# boeken_groep = {}
for boeken in groep1:
    if boeken == 'De Da Vinci Code':
        # boeken_groep[] =
        print('Da Vinci')
    elif boeken == 'Harry Potter':
        print('Potter')
    elif boeken == 'De Hobbit':
        print('Hobbit')
    elif boeken == 'Twilight':
        print('Twilight')
    elif boeken == 'De Vijfde Golf':
        print('Golf')

boeken_groep_1 = {'Harry Potter':2, 'De Hobbit': 3, 'De Da Vinci Code': 2, 'Twilight': 1, 'De Vijfde Golf': 1}
print(boeken_groep_1)

boeken_groep_2 = {}

for boek in groep2:
    if boek in boeken_groep_2:
        boeken_groep_2[boek] += 1
    else:
        boeken_groep_2[boek] = 1

print(boeken_groep_2)

meest_geleend = max(boeken_groep_1, key=boeken_groep_1.get)
print(f"Het meest geleende boek is: {meest_geleend} ({boeken_groep_1[meest_geleend]} keer)")

meest_geleend = max(boeken_groep_2, key=boeken_groep_2.get)
print(f"Het meest geleende boek is: {meest_geleend} ({boeken_groep_2[meest_geleend]} keer)")

