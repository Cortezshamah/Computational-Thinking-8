import turtle, time, random
from utils import *
#The goal off this game is to make the perfect creme brulee by making four jam and two creme from eggs and jam
# Section 1 - setup
# TODO - set a background using set_background()
set_background("kichen")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
eggs = 0
creme = 0
raspberry = 0
jam = 0
final = 0
# OPTIONAL: use this invisible alien to say a message

message_sprite = create_sprite("alien", -335,-257)
message_sprite.hideturtle()
message_sprite.write("Eggs and Raspberrys, try to make a creme brulee with jam",font = ("Arial", 17, "normal"))
message_sprite = create_sprite("balloon", -325,-282)
message_sprite.hideturtle()
message_sprite.write("500 e = 1 c , 250 r = 1 j and then 4 j + 2 c + space = win",font = ("Arial", 17, "normal"))

# Section 2 - controls
# TODO - define an action. ex: def my_control()
def make_egg () :
    global eggs
    eggs += 1
    x = random.randint(-325,325)
    y = random.randint(-325,200)
    create_sprite("egg",x,y)
window.onkeypress(make_egg, "e")

def make_raspberry () :
    global raspberry
    raspberry += 1
    x = random.randint(-325,325)
    y = random.randint(-325,200)
    create_sprite("raspberry",x,y)
window.onkeypress(make_raspberry, "r")
# TODO - make a second control

def make_creme () :
    global creme, eggs
    if eggs >= 250 :
        creme += 1
        eggs -= 250
        x = random.randint(-325,325)
        y = random.randint(200,250)
        create_sprite("creme",x,y)
        
window.onkeypress(make_creme, "c")

def make_jam () :
    global raspberry, jam
    if raspberry >= 125 :
        jam += 1
        raspberry -= 125
        x = random.randint(-300,300)
        y = random.randint(275,325)
        create_sprite("jam",x,y)
window.onkeypress(make_jam, "j")

def make_final () :
    global creme, jam, final
    if jam >= 4 and creme >= 2 :
        final += 1
        jam -= 4
        creme -= 2
        x = 0
        y = 0
        create_sprite("forty",x,y)
        create_sprite("float", 300,-25)
        message_sprite = create_sprite("float", -300,-25)
        message_sprite.write("YOU WIN",font = ("Arial", 115, "normal"))
window.onkeypress(make_final, "space")

message_sprite = create_sprite("noting", -335,100)
# 

# Section 3 - game loop
window.listen()
for i in range(1000000000):
    message_sprite.clear()
    message_sprite.write(f"Eggs: {eggs}\nCreme: {creme}\nRaspberry: {raspberry}\nJam: {jam}",font=("Arial",30,"normal"))

    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")

    time.sleep(0.01)
    window.update()