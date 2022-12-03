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
    

def mp(p):
    if (p == "X"):
        return 1
    elif (p == "Y"):
        return 2
    return 3

with open('02.txt', 'r') as file:
    file = file.read()

strats = file.split("\n")

#A = 1 Rock
#B = 2 Paper
#C = 3 Siscor

#X = Rock
#Y = Paper
#Z = Scissor

#lose = 1
#draw = 3
#win = 6

# A vs X = draw
# B vs Y = draw
# C vs X = draw
print(strats)
currentScore = 0
for strat in strats:
    match = strat.split(" ")
    e = me(match[0]) 
    p = mp(match[1])
    currentScore += rps(e,p)
    print(currentScore)
print(currentScore)
  


