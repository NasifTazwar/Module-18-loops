number = int(input("Enter any number\n"))
digit_count = 0

while number != 0:
    digit_count += 1
    number //= 10

print(digit_count)
