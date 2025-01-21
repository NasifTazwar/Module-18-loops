start_range = int(input("Enter a lower range: "))
end_range = int(input("Enter an upper range: "))

print("Prime numbers between", start_range, "and", end_range, "are:")

for number in range(start_range, end_range + 1):
    if number > 1:
        for divisor in range(2, number):
            if (number % divisor) == 0:
                break
        else:
            print(number)
