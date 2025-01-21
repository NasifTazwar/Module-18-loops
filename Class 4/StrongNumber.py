num = int(input("Please enter any number: "))
total_sum = 0
temp_num = num

while temp_num > 0:
    factorial = 1
    i = 1
    remainder = temp_num % 10

    while i <= remainder:
        factorial *= i
        i += 1

    print("\nFactorial of %d = %d" % (remainder, factorial))
    total_sum += factorial
    temp_num //= 10

print("\nSum of factorials of a given number %d = %d" % (num, total_sum))

if total_sum == num:
    print("%d is a Strong Number" % num)
else:
    print("%d is not a Strong Number" % num)
