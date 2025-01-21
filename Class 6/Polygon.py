import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300, 400)
shape = turtle.Turtle()

sides = 6
length = 70
turn_angle = 360.0 / sides

for count in range(sides):
    shape.forward(length)
    shape.right(turn_angle)

turtle.done()
