print("Half Pyramid Pattern of Stars (*):")
rows = int(input("Enter the number of rows: "))

for x in range(rows):
    for y in range(x + 1):
        print("* ", end="")
    print()