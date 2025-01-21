age = int(input("Enter the age:"))
student_class = int(input("Enter the class: "))

if 10 <= age <= 20 and student_class == 10:
    result = "Student can enrol in the class."
else:
    result = "Student cannot enrol in the class."

print(result)
