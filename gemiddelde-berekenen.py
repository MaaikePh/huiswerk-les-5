grades = {"Java": 7, "Python": 8, "C#": 6, "HTML": 9, "CSS": 8}

som = []
for x, y in grades.items():
    som.append(y)
gemiddelde = sum(som) / len(grades)
print(f"Gemiddelde score:", gemiddelde)

average = sum(grades.values()) / len(grades)
print(average)