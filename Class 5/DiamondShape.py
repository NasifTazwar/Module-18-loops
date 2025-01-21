rows = 5
spaces = rows - 1

for a in range(1, rows + 1):
    for b in range(1, spaces + 1):
        print(end=" ")
    spaces -= 1
    for b in range(2 * a - 1):
        print(end="*")
    print()

spaces = 1

for a in range(1, rows):
    for b in range(1, spaces + 1):
        print(end=" ")
    spaces += 1
    for b in range(1, 2 * (rows - a)):
        print(end="*")
    print()
