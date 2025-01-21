rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for a in range(1, rows, 2):
    print((a * ".|.").center(columns, "-"))

print("WELCOME".center(columns, "-"))

for a in range(rows - 2, -1, -2):
    print((a * ".|.").center(columns, "-"))