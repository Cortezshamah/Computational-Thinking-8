# Section 1 - Your code
from utils import *
set_background("castle")

s1 = create_sprite("pinetree", 200, -10)
s2 = create_sprite("present", 100, -120)
s2 = create_sprite("present", 140, -180)
s2 = create_sprite("puppy", 250, -130)

message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("Cortez Shamah",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()