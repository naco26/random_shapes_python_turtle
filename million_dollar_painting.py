
from shapes import movements
class painting:
    def draw_painting(torry):
        torry.penup()
        torry.goto(-300,-300)
        torry.pendown()
        torry.speed('fastest')
        torry.width(1)
        for y in range(-300,300,50):
            torry.penup()
            torry.goto(-300,y)
            torry.pendown()
            for _ in range(15):
                torry.pendown()
                torry.fillcolor(movements().random_color_gen())
                torry.begin_fill()
                torry.circle(10)
                torry.end_fill()
                torry.penup()
                torry.forward(50)