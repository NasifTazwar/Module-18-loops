number = int(input("Enter the number: "))
temp = number
length = 0

while temp > 0:
    length += 1
    temp //= 10

if length >= 4:
    mid_index = length // 2
    check = 0
    while number > 0:
        remainder = number % 10
        if check == mid_index:
            middle_one = remainder
        elif check == (mid_index - 1):
            middle_two = remainder
        number //= 10
        check += 1
    product = middle_one * middle_two
    print("\nProduct of Mid digits (" + str(middle_one) + "*" + str(middle_two) + ") =", product)
else:
    print("\nIt's not a 4 or more than 4-digit number!")
