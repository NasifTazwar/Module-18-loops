x=int(input("Enter the number for x: "))

value=0

for i in range(1,11):
  value+=1
  print(value,x**i)

y=int(input("Enter the number for y: "))

value=0

for i in range(10,0,-1):
  value+=1
  print(value,y**i)