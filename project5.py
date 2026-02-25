import turtle, math, time, random
from utils import *

# Section 1: Setup
# TODO - create your player character and any other sprites

# TODO - set the starting value for your variables
sprite_list = []
set_background("minecr (1)")
H1 = create_sprite("harper")
D1 = create_sprite("darian")
message_sprite = create_sprite("alien", -335,-257)
message_sprite.hideturtle()
message_sprite.write("Harper = {H_Daimonds}/n Dariun = {D_Daimonds} ",font = ("Arial", 17, "normal"))
# Section 2: Controls
H_Diamonds = 0
D_Diamonds = 0
daimonds = 0
# TODO - define your controls
#movement
def move_up2():
    x = D1.xcor()
    y = D1.ycor() + 5
    D1.goto(x,y)
        
def move_down2():
    x = D1.xcor()
    y = D1.ycor() - 5
    D1.goto(x,y)
    
def move_left2():
    x = D1.xcor() - 5
    y = D1.ycor() 
    D1.goto(x,y)
    
def move_right2(): 
    x = D1.xcor() + 5
    y = D1.ycor() 
    D1.goto(x,y)


def move_up():
    x = H1.xcor()
    y = H1.ycor() + 5
    H1.goto(x,y)
        
def move_down():
    x = H1.xcor()
    y = H1.ycor() - 5
    H1.goto(x,y)
    
def move_left():
    x = H1.xcor() - 5
    y = H1.ycor() 
    H1.goto(x,y)
 #the goal of this game is to get 20 diamonds fasteer then the other player   
def move_right(): 
    x = H1.xcor() + 5
    y = H1.ycor() 
    H1.goto(x,y)


# TODO - pick keys for each control
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")
window.onkeypress(move_up2, "Up")
window.onkeypress(move_down2, "Down")
window.onkeypress(move_left2, "Left")
window.onkeypress(move_right2, "Right")
#end of movement
message_sprite4 = create_sprite("alien", 0, 0)
message_sprite3 = create_sprite("alien", 0, 0)
message_sprite2 = create_sprite("alien", -335, 225)
message_sprite = create_sprite("alien", -335, 200)

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    if i % 10 == 0:
        x = random.randint(-300, 300)
        DDD = create_sprite("dsimond", x, 400)
        DDD.setheading(270)
        sprite_list.append(DDD)
    
    for DDD in sprite_list:
        DDD.forward(5)

    for daimonds in sprite_list:
        x = daimonds.xcor()
        y = daimonds.ycor()
        daimonds.goto(x, y-1)
    
    for daimonds in sprite_list:
        if get_distance(daimonds, D1) < 50:
            D_Diamonds += 1
            daimonds.hideturtle()
            sprite_list.remove(daimonds)

    for daimonds in sprite_list:
        if get_distance(daimonds, H1) < 50:
            H_Diamonds += 1
            daimonds.hideturtle()
            sprite_list.remove(daimonds)
    
    if D_Diamonds >= 20:
        message_sprite3.write(f"Darian Wins!",font = ("Arial", 40, "normal")) 
        break
    message_sprite3.hideturtle()
    # TODO - make an if statement for ending the game
    

    message_sprite4.hideturtle()
    if H_Diamonds >= 20:
        message_sprite3.hideturtle()
        message_sprite3.write(f"Harper Wins!",font = ("Arial", 40, "normal"))
        break
    message_sprite.clear()
    message_sprite.hideturtle()
    message_sprite.write(f"Harper points = {H_Diamonds}",font = ("Arial", 17, "normal"))
    message_sprite2.clear()
    message_sprite2.hideturtle()
    message_sprite2.write(f"Darian points = {D_Diamonds}",font = ("Arial", 17, "normal"))    
    time.sleep(0.01)
    window.update()
