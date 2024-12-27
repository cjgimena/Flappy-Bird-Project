#import modules
import turtle as trtl
import pygame
import random

#setup 
wn = trtl.Screen()
wn.setup(width=1.0,height=1.0)
wn.bgcolor("black")
wn.title("Flappy Bird")
wn.bgpic("background.gif")

#Title Screen
bird = trtl.Turtle()
wn.addshape("flappy.gif")
writer = trtl.Turtle()
writer.color("Black")
writer.penup()
writer.goto(0,100)
writer.pendown()
writer.write ('Flappy Bird', align = 'center', font = ('Comic Sans MS', 40, 'bold'))
writer.penup()
writer.goto (0,50)
writer.pendown()
writer.write ('Press "s" to start', align = 'center', font = ('Comic Sans MS', 20, 'bold'))
writer.hideturtle()

pipe1 = trtl.Turtle()
pipe2 = trtl.Turtle()
wn.tracer(False)

#flappy function
def flappy():
  wn.tracer(True)
  writer.clear()
  global bird
  bird.shape("flappy.gif")
  bird.color("yellow")
  bird.speed(0)
  bird.penup()
  bird.goto(0,200)
  bird.fall = 0

  gravity = 0.05

  pipe1.ht()
  pipe1.speed(10)
  pipe1.color("green")
  pipe1.shape("square")
  pipe1.shapesize(15,5)
  pipe1.penup()
  pipe1.goto(450, 150)

  pipe2.ht()
  pipe2.speed(10)
  pipe2.color("green")
  pipe2.shape("square")
  pipe2.shapesize(15,5)
  pipe2.penup()
  pipe2.goto(450, -290)

  while True:
    bird.fall -= gravity
    bird.sety(bird.ycor() + bird.fall)
    #check for ground
    if bird.ycor() < -220:
      bird.fall *= 0 
      gravity *= 0
      writer.penup()
      writer.goto (0,100)
      writer.write ('You have hit the ground!', align = 'center', font = ('Comic Sans MS', 30, 'bold'))
      writer.goto (0,0)
      writer.write ("Press 's' to play again", align = 'center', font = ('Comic Sans MS', 30, 'bold'))
      break
    if abs(bird.xcor() - pipe1.xcor()) < 70 and abs(bird.ycor() - pipe1.ycor()) < 165:
      hit()
      break
    if abs(bird.xcor() - pipe2.xcor()) < 70 and abs(bird.ycor() - pipe2.ycor()) < 165:
      hit()
      break
    pipe()

def pipe():
  wn.tracer(False)
  if pipe1.xcor() >= -500:
    pipe1.st()
    pipe2.st()
    pipe1.backward(3)
    pipe2.backward(3)
  if pipe1.xcor() <= -500:
    rand_y = random.randint(90, 375)
    pipe1.ht()
    pipe2.ht()
    pipe1.goto(450, rand_y)
    pipe2.goto(450, rand_y - 440)
    pipe1.st()
    pipe2.st()
  wn.tracer(True)
      
#bird jump
def space():
  bird.fall = 3

#play agian function
def hit():
  pipe1.ht()
  pipe2.ht()
  writer.penup()
  writer.goto (0,100)
  writer.write ('You have hit a pipe!', align = 'center', font = ('Comic Sans MS', 30, 'bold'))
  writer.goto (0,0)
  writer.write ("Press 's' to play again", align = 'center', font = ('Comic Sans MS', 30, 'bold'))


#function calls
wn.onkeypress(flappy,"s")
wn.onkeypress(space," ")

wn.listen()
wn.mainloop()


#citations
#https://www.youtube.com/watch?v=HHQV3ifJopo&list=RDCMUC2vm-0XX5RkWCXWwtBZGOXg&index=3