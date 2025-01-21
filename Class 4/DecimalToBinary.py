def decimal_to_binary(decimal):
    if decimal >= 1:
        decimal_to_binary(decimal // 2)
    print(decimal % 2, end='')

decimal_number = int(input("Enter a decimal number: "))
print("Binary representation of", decimal_number, "is: ", end='')
decimal_to_binary(decimal_number)
print()
