def to_binary(number):
    if number > 1:
        to_binary(number // 2)
    print(number % 2, end=" ")

decimal = float(input("Enter a number to find its binary value: "))
to_binary(decimal)
print()

decimal = float(input("Enter a number to find its binary value: "))
to_binary(decimal)
print()