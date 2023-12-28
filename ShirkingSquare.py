import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("Light green")
turtle_screen.title("Turtle Python")

turtle_instace = turtle.Turtle()
turtle_instace.color("blue")

def shiring_square(size):
    for i in range(4):
        turtle_instace.forward(size)
        turtle_instace.left(90)
        size = size -5


shiring_square(150)
shiring_square(145)
shiring_square(140)
shiring_square(135)
shiring_square(130)
shiring_square(125)
shiring_square(120)
shiring_square(115)
shiring_square(110)
shiring_square(105)
shiring_square(100)
shiring_square(95)
shiring_square(90)
shiring_square(85)
shiring_square(80)
shiring_square(75)
shiring_square(70)
shiring_square(65)
shiring_square(60)
shiring_square(55)
shiring_square(50)
shiring_square(45)
shiring_square(40)
shiring_square(35)
shiring_square(30)
shiring_square(25)
shiring_square(20)
shiring_square(15)
shiring_square(10)
shiring_square(5)
shiring_square(0)


turtle.done
