from turtle import * 
import math 
import random
#name of turtle 
lilo = Turtle()
 
colors= ["orange", "green", "pink", "red", "darkblue"]
setup(500,300)
x_pos = -250
y_pos = -150

lilo.penup()
lilo.setposition(x_pos, y_pos)
 
lilo.pendown()
def drawShape(side, length):
		for i in range(4):
			lilo.fd(300)
			lilo.left(90)
			lilo.pencolor(random.choice(colors))
drawShape(lilo, 100)
def drawSquare(side, length):
		for i in range(5):
			lilo.fd(250)
			lilo.left(72)
			lilo.pencolor(random.choice(colors))
drawSquare(lilo, 100)
def smallsquare(side, length):
		for i in range(6):
			lilo.fd(150)
			lilo.left(60)
			lilo.pencolor("purple")
smallsquare(lilo, 100)
def smallersquare(side, length):
		for i in range(8):
			lilo.fd(190)
			lilo.left(45)
			lilo.pencolor("lightblue")
smallersquare(lilo, 100)



exitonclick()




