total_rows = int(input("Please enter the total number of rows: "))
current_num = 1

print("Floyd's Triangle")

for row in range(1, total_rows + 1):
    for col in range(1, row + 1):
        print(current_num, end='  ')
        current_num += 1
    print()
