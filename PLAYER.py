from turtle import Turtle,Screen
class Player(Turtle):
    def __init__(self):
        super().__init__()

    tur=Turtle("turtle")

    def up(self):
        tur.fd(20)
    sc=Screen()
    sc.listen()
    sc.onkey(up,"Up")
    sc.exitonclick()
