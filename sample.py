from colorsys import rgb_to_hsv
import colorsys
import turtle
a=turtle.Turtle()
b=turtle.Screen()
a.speed(30)
b.bgcolor('black')
a.color('sky blue')
n=1
j=580
a.hideturtle()

while j:
    a.forward(n)
    a.left(120)
    a.left(1)
    n+=1
    j-=1

turtle.done()


    

    

