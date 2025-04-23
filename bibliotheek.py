bibliotheek = {
    "The Silent Patient": {
        "auteur": "Alex Michaelides",
        "genre": "Thriller",
        "publicatiejaar": 2019
    },
    "Where the Crawdads Sing": {
        "auteur": "Delia Owens",
        "genre": "Fictie",
        "publicatiejaar": 2018
    },
    "The Night Circus": {
        "auteur": "Erin Morgenstern",
        "genre": "Fantasy",
        "publicatiejaar": 2011
    },
    "Educated": {
        "auteur": "Tara Westover",
        "genre": "Memoir",
        "publicatiejaar": 2018
    },
    "Circe": {
        "auteur": "Madeline Miller",
        "genre": "Fantasy",
        "publicatiejaar": 2018
    }
}

#Je gaat een bibliotheekprogramma maken. Het programma moet de volgende functionaliteiten hebben:
#1. De gebruiker moet boeken kunnen toevoegen aan de bibliotheek. Een boek heeft de volgende eigenschappen:
#   - Naam
#   - Auteur
#   - Genre
#   - Publicatiejaar

#2. De gebruiker moet een lijst van alle boeken in de bibliotheek kunnen opvragen. De lijst moet de volgende informatie bevatten:
#   - Naam
#   - Auteur
#   - Genre
#   - Publicatiejaar

#3. De gebruiker moet een lijst van alle boeken in een bepaald genre kunnen opvragen. De gebruiker moet het genre kunnen invoeren en het programma moet alle boeken in dat genre tonen. De lijst moet de volgende informatie bevatten:
#   - Naam
#   - Auteur
#   - Publicatiejaar

#4. De gebruiker moet het programma kunnen stoppen.

#Een paar tips voor het maken van dit programma:
# Als je een keuze menu maakt, kun je een while loop gebruiken die blijft loopen totdat de gebruiker kiest om te stoppen.
# Je keuze menu is eigenlijk een if-elif-else statement. Je kunt de keuze van de gebruiker opslaan in een variabele en dan met if-elif-else bepalen wat er moet gebeuren.


def main():
    keuze = 0
    while keuze != "4":
        print("Welkom bij de bibliotheek.")
        print("1) Voeg een boek toe.")
        print("2) Bekijk alle boeken.")
        print("3) Bekijk alle boeken van een bepaald genre.")
        print("4) Sluit het programma.")
        keuze = input("Maak je keuze: ")

        if keuze == "1":
            print("Laten we een boek toevoegen...")
            naam_boek = str(input("Vul hier de naam van het boek in: "))
            naam_auteur = str(input("Vul hier de auteur van het boek in: "))
            genre = str(input("Vul hier het genre van het boek in: "))
            publicatiejaar = str(input("Vul hier het publiecatiejaar van het boek in: "))
            bibliotheek[naam_boek] = {"auteur": naam_auteur, "genre": genre, "publicatiejaar": publicatiejaar}

        elif keuze == "2":
            print("Laten we alle boeken bekijken...")
            for boek, info in bibliotheek.items():
                print(f"- {boek} ({info['genre']}, {info['publicatiejaar']}) door {info['auteur']}")


        elif keuze == "3":
            print("Laten we alle boeken van een specifiek genre bekijken...")
            genre_keuze = input("Vul het genre naar keuze in: ")
            gevonden = False
            for x, y in bibliotheek.items():
                if y["genre"].lower() == genre_keuze.lower():
                    print(f"- {x} door {y['auteur']}")
                    gevonden = True
            if not gevonden:
                print("Geen boeken gevonden in dit genre.")

        elif keuze == "4":
            print("Tot ziens!")

        else:
            print("Ongeldige keuze. Probeer het opnieuw.")

main()
