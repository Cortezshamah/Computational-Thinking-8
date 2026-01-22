# Section 1 - Your code
from utils import *
set_background("castle")

s1 = create_sprite("bench", 100, 100)
s2 = create_sprite("cucumber", -100, 100)
s3 = create_sprite("snowflake", -100, -100)
s4 = create_sprite("images", 100, -100)

message1 = create_sprite("alien",-200,200)
message1.color("red")
# message'[9]',font = ("Arial", 40, "normal")
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("black")
message2.write("Your motto",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()