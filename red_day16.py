import turtle
import random

#setting up variables
t = turtle      #to make writing code easier
t.speed(10)

while True:
  #assigning random numbers to variables for number and color
  num = random.randint(10,40)
  r = random.randint(1,255)
  b = 0
  g = 0
  t.pd()
  #assigns color of turtle
  t.color(r, b, g)
  #keeps the turtle from doing things out of the size of the screen
  if t.xcor() > 150:      #if turtle reaches the side of the screen
    t.ht()                #hides turtle from view
    t.pu()
    t.setx(-150)          #brings turtle to opposite side of the screen
    t.st()                #brings turtle back to view
    t.pd()
  elif t.xcor() < -150:
    t.ht()
    t.pu()
    t.setx(150)
    t.st()
    t.pd()
  if t.ycor() > 150:
    t.ht()
    t.pu()
    t.sety(-150)
    t.st()
    t.pd()
  elif t.ycor() < -150:
    t.ht()
    t.pu()
    t.sety(150)
    t.st()
    t.pd()
  #actually drawing
  if r < 85:                    #controls movement if r < 85
    t.fd(num)
    t.rt(num / 2)
    for x in range(3):          #draws three circles
      lol = random.randint(0,5) #sets radius for circle randomly
      if lol <= 3:              #randomizes if fill happens or not
        t.begin_fill()          #starts filling for a shape the turtle makes
        t.circle(lol)
        t.end_fill()            #stops filling
      else:
        t.circle(lol)
  elif r >= 85 and r <= 170:    #controls movement if r >= 85 and r <= 170
    t.fd(num / 2)
    t.rt(num / 4)
    for x in range(5):          #draws a star
        t.rt(144)
        t.fd(10)
  else:                         #controls movement if r > 170 and prints text
    t.fd(num / 4)
    t.lt(num / 2)
    if r < 200:                 #randomizes text that is printed
      t.write("HI", True, font = ("Verdana", 6, "normal"))            #prints text
    if r < 255 and r >= 200:
      t.write("LOVE", True, font = ("Verdana", 6, "normal"))
    if r == 255:
      t.write("HAIL SATAN", True, font = ("Verdana", 12, "normal"))
