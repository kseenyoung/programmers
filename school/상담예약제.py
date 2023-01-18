booked = [["09:10", "lee"]]
unbooked = [["09:00", "kim"], ["09:05", "bae"]]

visitor = booked + unbooked
visitor.sort(key=lambda x: x[0])

late = []
fin = []
current = visitor[0][0]

for t, v in visitor:
    if t < current:
        late.append([t, v])
    current += 10
    print(current)
