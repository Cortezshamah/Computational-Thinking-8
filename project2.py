yellow_points = 0
red_points = 0
blue_points = -1

input("Welcome to the favorite primary color quiz")
print("----------------------------------------------------------------------")
answer1 = input("Do you like A blueberrys, B strawberrys, or C bananas more?")
if answer1 == "A" or "a" or " a" or " A":
    blue_points += 1
elif answer1 == "B" or "b" or " b" or " B":
    red_points += 1
elif answer1 == "C" or "c" or " c" or " C":
    yellow_points += 1
print("----------------------------------------------------------------------")
print("Make sure to answer capitalized without spaces")
answer2 = input("Do you like A nitro takis, B cheese takis, or C chili lime takis the most?")
if answer2 == "A":
    blue_points += 1
elif answer2 == "B":
    yellow_points += 2
elif answer2 == "C":
    red_points += 1
print("----------------------------------------------------------------------")
answer3 = input(r"Do you like A Cold colors(second half of the rainbow) or B Warm colors(first half of the rainbow)?")
if answer3 == "A":
    blue_points += 1
elif answer3 == "B":
    yellow_points += 1
    red_points += 1
print("----------------------------------------------------------------------")
answer4 = input("Do you like A pikachu, B squirtle, or C charmander?")
if answer4 == "A":
    yellow_points += 1
elif answer4 == "B":
    blue_points += 1
elif answer4 == "C":
    red_points += 1
print("----------------------------------------------------------------------")
answer5 = input("Do you like A red gatorade, B yellow gatorade, or C blue gatorade the most?")
if answer4 == "A":
    red_points += 1
elif answer4 == "B":
    yellow_points += 1
elif answer4 == "C":
    blue_points += 1
print("----------------------------------------------------------------------")
answer6 = input("Do you like A roses, B hydrangea, or C sunflowers?")
if answer6 == "A":
    red_points += 1
elif answer6 == "B":
    blue_points += 1
elif answer6 == "C":
    yellow_points += 1
print("----------------------------------------------------------------------")
if red_points > blue_points and red_points > yellow_points:
    print("You are a red person!")
elif blue_points > yellow_points and blue_points > red_points:
    print("You are a blue person!")
elif yellow_points > red_points and yellow_points > blue_points:
    print("You are a yellow person!")
elif yellow_points == red_points and yellow_points > blue_points and red_points > blue_points:
    print("You are a orange person!")
elif yellow_points == blue_points and yellow_points > red_points and blue_points > red_points:
    print("You are a green person!")
elif red_points == blue_points and red_points > yellow_points and blue_points > yellow_points:
    print("You are a purple person!")
elif red_points == blue_points == yellow_points:
    print("You are a brown person!")