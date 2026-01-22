import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -200
y1 = 100
x2 = -200
y2 = 50
x3 = -200
y3 = 0
x4 = -200
y4 = -50


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("images")
t1 = create_sprite("download (1)",x1,y1)
t2 = create_sprite("pug",x2,y2)
t3 = create_sprite("football",x3,y3)
t4 = create_sprite("tricolor",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(60):
    x1 += random.randint(0,10)
    x2 += random.randint(3,12)
    x3 += random.randint(0,10)
    x4 += random.randint(0,10)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("player MOnkey wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("player Pug wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("player FOOtbaLL wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    print("player DOg wins!")
# it is  almost completely random because 3 of them have the same
# chance but the pug is a little higher so it is more likely to win

turtle.exitonclick()