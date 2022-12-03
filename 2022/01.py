with open('01.text', 'r') as file:
    file = file.read()

e = file.split("\n\n")

print(elves)

bigSnack = 0
goodSnack = 0
mediumSnack = 0

for elf in elves:
    food = list(map(int, elf.split("\n")))
    smallSnack = 0
    for snack in food:
        smallSnack += snack
    
    if(smallSnack > bigSnack):
        mediumSnack = goodSnack
        goodSnack = bigSnack
        bigSnack = smallSnack
    elif(smallSnack > goodSnack):
        mediumSnack = goodSnack
        goodSnack = smallSnack
    elif(smallSnack > mediumSnack):
        mediumSnack = smallSnack
            
        
print(bigSnack)    
print(goodSnack)    
print(mediumSnack)    
snackz = bigSnack + goodSnack + mediumSnack
print(snackz)
