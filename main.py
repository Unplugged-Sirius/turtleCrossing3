from turtle import Screen
from cars import Cars
sc=Screen()
sc.setup(1000,700)
c=Cars()
c.create()
c.move()
sc.exitonclick()
