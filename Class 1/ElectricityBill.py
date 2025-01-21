units_consumed = int(input(" Please enter the number of units you consumed: "))

basic_rate = 130  
total_cost = 0
surcharge = 0

if units_consumed < 50:
    total_cost = units_consumed * 2.60
    surcharge = 25

elif units_consumed <= 100:
    total_cost = basic_rate + ((units_consumed - 50) * 3.25)
    surcharge = 35

elif units_consumed <= 200:
    total_cost = basic_rate + 162.50 + ((units_consumed - 100) * 5.26)
    surcharge = 45

else:
    total_cost = basic_rate + 162.50 + 526 + ((units_consumed - 200) * 8.45)
    surcharge = 75

total_bill = total_cost + surcharge
print("\nYour Electricity Bill is: %.3f BDT" % total_bill)
