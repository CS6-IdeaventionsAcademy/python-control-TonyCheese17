
from turtle import *
from random import*

def randomcolor():
  red = randint(0,255)
  green = randint(0,255)
  blue = randint(0,255)
  color(red,green,blue)

def randomplace():
  penup()
  x = randint(-100,100)
  y = randint(-100,100)
  goto(x,y)
  pendown()

def randomheading():
  setheading = randint(1,360)


shape("turtle")
randomcolor()

for i in range(200):
  randomplace()
  randomcolor()
  randomheading()
  stamp()

