studenten = [("Alice", 8.5), ("Bob", 7.0), ("Charlie", 6.2), ("Diana", 9.1)]

for x,y in studenten:
    print(x, y)

som = []
for x, y in studenten:
    som.append(y)
gemiddelde = sum(som) / len(studenten)
print(f"Gemiddelde score:", gemiddelde)

maximum = studenten[0]
for x, y in studenten:
    if y > maximum[1]:
        maximum = (x, y)
print(f"Het hoogst behaalde cijfer is van {maximum[0]} met cijfer {maximum[1]}")