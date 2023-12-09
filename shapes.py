from turtle import Turtle
import random

def random_angle():
    angles=[0,90,180,270]
    return random.choice(angles)
class movements:
    def random_color_gen(self):
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    def draw_square(torry,size=100):
        for _ in range(0,4):
            torry.forward(100)
            torry.right(90)

    def draw_dashed_line(torry,length=10,size=10):
        for _ in range(length):
            torry.forward(10)
            torry.penup()
            torry.forward(10)
            torry.pendown()

    def draw_all_shapes(self,torry,size=10):
        for n in range(3,size):
            torry.pencolor(self.random_color_gen()) 
            for _ in range(n):
                torry.forward(100)
                torry.right(360/n)

    def random_Walk(self,torry,steps=20,num=250):
        torry.speed('fastest')
        torry.width(15)
        for _ in range(num):
            torry.forward(steps)
            torry.pencolor(self.random_color_gen())
            torry.setheading(random_angle())
            
    def spirograph(self,torry,size=10):
        torry.speed('fastest')
        torry.width(1)
        for _ in range(int(360/size)):
            torry.pencolor(self.random_color_gen())
            torry.circle(30)
            torry.setheading(torry.heading() + size)
        