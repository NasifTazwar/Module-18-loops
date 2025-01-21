number = int(input("Enter a number: "))
total_sum = 0
temp_number = number

while temp_number > 0:
    digit = temp_number % 10
    total_sum += digit ** 3
    temp_number //= 10

if number == total_sum:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
