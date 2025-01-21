import turtle

screen = turtle.Screen()
turtle.speed(2)

for index in range(100):
    turtle.circle(5 * index)
    turtle.circle(-5 * index)
    turtle.left(index)

turtle.exitonclick()
