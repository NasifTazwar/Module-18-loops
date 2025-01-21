num_rows = int(input("Enter the number of rows: "))
if num_rows % 2 == 0:
    half_rows = int(num_rows / 2)
else:
    half_rows = int(num_rows / 2) + 1

spaces = half_rows - 1

for a in range(1, half_rows + 1):
    for b in range(1, spaces + 1):
        print(end=" ")
    spaces -= 1
    number = 1
    for b in range(2 * a - 1):
        print(end=str(number))
        number += 1
    print()

spaces = 1

for a in range(1, half_rows):
    for b in range(1, spaces + 1):
        print(end=" ")
    spaces += 1
    number = 1
    for b in range(1, 2 * (half_rows - a)):
        print(end=str(number))
        number += 1
    print()
