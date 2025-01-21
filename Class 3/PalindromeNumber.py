number = int(input("Enter a number: "))
reversed_number = 0
temp_number = number

while temp_number > 0:
    remainder = temp_number % 10
    reversed_number = remainder + (reversed_number * 10)
    temp_number = int(temp_number / 10)

if reversed_number == number:
    print("\nIt is a Palindrome Number")
else:
    print("\nIt is not a Palindrome Number")
