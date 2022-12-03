def crps(e, s):
    if (s == 2):
        return e
    elif (s == 3):
        if (e == 1):
            return 2
        elif (e == 2):
            return 3
        else:
            return 1
    else:
        if (e == 1):
            return 3
        elif (e == 2):
            return 1
        else:
            return 2

def rps(e, p):
    score = 0
    if e == p:
        score += 3
    if e == 1:
        if p == 2:
            score += 6
    elif e == 2:
        if p == 3:
            score += 6
    else:
        if p == 1:
            score += 6
    
    score += p
    return score

def me(e):
    if (e == "A"):
        return 1
    elif (e == "B"):
        return 2
    return 3
    

def ms(p):
    if (p == "X"):
        return 1
    elif (p == "Y"):
        return 2
    return 3

with open('02.txt', 'r') as file:
    file = file.read()

#strats="A Y\nB X\nC Z".split("\n")

#A = 1 Rock
#B = 2 Paper
#C = 3 Siscor

#X = Lose
#Y = Draw
#Z = Win

#lose = 1
#draw = 3
#win = 6

# A vs X = draw
# B vs Y = draw
# C vs X = draw
print(strats)
cs = 0
for strat in strats:
    match = strat.split(" ")
    e = me(match[0]) 
    s = ms(match[1])
    r = crps(e,s)
    sc = rps(e,r)
    cs += sc
print(cs)
  


