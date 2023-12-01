with open('01.txt', 'r') as file:
    file = file.read()

ms = file.split("\n")

pm = 0

first = True

i = 0
j = -1
k = -2
l = -3

ed = list()

a = 0
b = 0
c = 0
d = 0

ec = 0
lm = 0

ind = 0

for m in ms:
    im = int(m)
    
    if i < 3:
        a += im
        i += 1
        if i == 3:
            ed.append(a)
            a = 0
    elif i == 3:
        i = 0
    
    if j >= 0 and j < 3:
        b += im
        j += 1
        if j == 3:
            ed.append(b)
            b = 0
    elif j == 3:
        j = 0

    if k >= 0 and k < 3:
        c += im
        k += 1
        if k == 3:
            ed.append(c)
            c = 0 
    elif k == 3:
        k = 0
    
    if l >= 0 and l < 3:
        d += im
        l += 1
        if l == 3:
            ed.append(d)
            d = 0 
    elif l == 3:
        l = 0
        
        
    if k < 0:
        k += 1
    if j < 0:
        j += 1
    if l < 0:
        l += 1
        
for m in ed:
    print(m)
    if m > pm and first == False:
        ec+=1
    pm = int(m)
    first = False
    
print(ec)