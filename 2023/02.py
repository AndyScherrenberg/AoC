import re

with open('02.txt', 'r') as file:
    file = file.read()
    
    
instr = file.split("\n")

p1,p2 = 0,0

blue = 14
red = 12
green = 13


def get_cube_amount(cube):
    find = re.findall("\d* "+cube, g)
    amount = 0
    if find:
        amount = int(find[0].replace(cube,""))
    return amount
    
for line in instr:
    possible = True
    #print(line)
    collection = line.split(":")
    gameid = int(collection[0].replace("Game ", "").replace(":",""))
    #print(gameid)
    game = collection[1].split(";")
    
    highest_blue = 0
    highest_red = 0
    highest_green = 0
    
    for g in game:
        #current_set = g.split(",")
        #sets.append(g.split(","))
        #for cs in current_set:
        red_amount = get_cube_amount("red")
        blue_amount = get_cube_amount("blue")
        green_amount =get_cube_amount("green")
        if(red_amount > highest_red):
            highest_red = red_amount
        if(green_amount > highest_green):
            highest_green = green_amount
        if(blue_amount > highest_blue):
            highest_blue = blue_amount
        if(green_amount > green or red_amount >red or blue_amount > blue):
            possible = False
        
    if (possible):
        p1 += gameid
    p2 += highest_blue * highest_red * highest_green
    
    #print(sets)
print(p1,p2)