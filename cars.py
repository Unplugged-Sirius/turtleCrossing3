from turtle import Turtle
import random
class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.carss=[]



    def create(self):
        y = random.randint(-450, 450)
        print(y)
        new_car=Turtle()
        new_car.penup()
        new_car.shape = "square"
        new_car.color = "green"
        new_car.shapesize(2, 10)
        new_car.penup()
        new_car.setpos(500, y)
        self.carss.append(new_car)
    def move(self):
       for car in self.carss:
         y = random.randint(-450, 450)
         while True:
            if car.xcor()>=-500:
                 car.bk(20)
                 car.speed("slowest")

            elif car.xcor()<500:

                car.goto(500,y)
                print(y)
