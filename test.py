from turtle import Turtle,Screen
tur=Turtle("turtle")
tur.penup()
tur .goto(0,-300)
tur.lt(90)
def up():
     tur.fd(20)
sc=Screen()
sc.listen()
sc.onkey(up,"Up")
sc.exitonclick()
