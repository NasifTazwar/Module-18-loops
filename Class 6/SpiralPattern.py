import turtle

window = turtle.Screen()
window.bgcolor("light blue")
window.title("Turtle")
pen = turtle.Turtle()
dimension = 0

while True:
    for count in range(4):
        pen.fd(dimension + 1)
        pen.left(90)
        dimension -= 5
    dimension += 1
