import turtle
import random

t = turtle
t.speed(.5)
lol = 1
t.width(2)

while lol <= 1000:
  if t.xcor() > 150:
    t.ht()
    t.pu()
    t.setx(-150)
    t.st()
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
  for clr in ['red', 'orange', 'yellow', 'green', 'blue', 'purple']:
    t.color(clr)
    num = random.randint(1,10)
    move = random.randint(1,5)
    turn = random.randint(5, 15)
    t.fd(move)
    if num <= 5:
      t.rt(turn)
    if num > 5:
      t.lt(turn)
  lol = lol + 1

t.pu()
t.home()
t.color('red')
t.clear()
t.getscreen().bgcolor('black')
t.lt(90)
t.bk(100)
t.rt(90)
t.pd()
t.circle(100)
t.lt(72)

for x in range(5):
  t.fd(190)
  t.lt(144)

t.pu()
t.lt(18)
t.fd(93)
t.lt(90)
t.fd(40)
t.pd()
t.write('Hail Satan', font = ('Verdana', 12, 'normal'))
t.ht()
