rows = int(input("Enter the total number of rows: "))

print("Mirrored Right Triangle Star Pattern")
for a in range(1, rows + 1):
    for b in range(1, rows + 1):
        if b <= rows - a:
            print(' ', end='  ')
        else:
            print('*', end='  ')
    print()
