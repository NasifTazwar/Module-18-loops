import turtle

pen = turtle.Turtle()
side_length = int(input("Enter the length of the side of the square: "))
for count in range(4):
    pen.forward(side_length)
    pen.left(90)
