import time

with open('04.txt', 'r') as file:
    file = file.read()
    
instr = file.split("\n")

p1,p2 = 0,0

start_time = time.time()

def calculate_win(numbers, win):
    result = 0
    for n in numbers:
        if (n.isdigit()):
            if n in win:
                if (result == 0):
                    result = 1
                else:
                    result *=2
    return result

def increase_tickets(numbers,win, trigger_happy, index):
    winning = 1
    for n in numbers:
        if (n.isdigit()):
            if n in win:
                if len(trigger_happy) > idx+winning: 
                    trigger_happy[idx + winning] += 1
                    winning += 1

trigger_happy = []
for idx,line in enumerate(instr):
    trigger_happy.append(1)

for idx, line in enumerate(instr):
    split = line.split(":")
    game = split[1].split("|")
    numbers = game[0].split(" ")
    win = game[1].split(" ")
    amounts = trigger_happy[idx]
    for i in range(amounts):
        increase_tickets(numbers,win, trigger_happy, idx)
    p1 += calculate_win(numbers,win)

for n in trigger_happy:
    p2 += n
    
print(p1,p2, "--- %s seconds ---" % (time.time() - start_time))
    