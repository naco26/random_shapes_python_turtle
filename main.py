#from turtle import Turtle,Screen
import turtle as t
from shapes import movements
from million_dollar_painting import painting

t.colormode(255)
#screen object and set size
screen=t.Screen()
screen.screensize(canvwidth=600,canvheight=600)

#make turtle and assign shape,color,speed,width
torry=t.Turtle()
tim=t.Turtle()
torry.speed('slow')
torry.width(5)
torry.shape("turtle")
torry.color("DarkGreen")
torry.hideturtle()
tim.hideturtle()

#reset all properties for torry the turtle
def refresh(torry):
    torry.clear()
    torry.penup()
    torry.goto(0,0)
    torry.pendown()
    torry.speed('slow')
    torry.width(5)

options = ["Draw a Square.","Draw a dashed line","Draw n number of shapes","Random Walk"
           ,"Draw a Spirograph","Draw a million dollar painting."]

print("Welcome to turtle Game. We have following options for you to choose from")
num=1
for i in options:
    print(num," - ",i)
    num+=1
choice='y'
while choice.lower()=='yes' or choice.lower()=='y':
    option = int(input("Enter your choice:"))
    if option==1:
        #drawing square
        movements.draw_square(torry)
        refresh(torry)
    elif option==2:
        #drawing dashed line
        movements.draw_dashed_line(torry)
        refresh(torry)
    elif option==3:
        #draw all shapes at one point
        n = int(input("Enter num of shapes u want:"))
        movements().draw_all_shapes(torry,n+3)
        refresh(torry)
    elif option==4:
        #a random walk of fixed steps
        movements().random_Walk(torry)
        refresh(torry)
    elif option==5:
        #draw a spirograph
        movements().spirograph(torry)
        refresh(torry)
    elif option==6:    
        #million dollar painting
        painting.draw_painting(tim)
        refresh(tim)
    else:
        print("option not supported")
    choice = input("Want to choose again? Type 'yes' or 'y' for yes and press any key for no ")
print("Thanks for visiting today")
#to keep screen up until a click

screen.exitonclick()


