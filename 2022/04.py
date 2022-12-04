def contains(small, big):
    for i in range(len(big)-len(small)+1):
        for j in range(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return i, i+len(small)
    return False

def rn(st):
    a = st.split("-")
    l = int(a[0])
    h = int(a[1])
    k = list()
    r = range(l,h+1)
    for i in r:
        k.append(i)
    return k
        
    

with open('04.txt', 'r') as file:
    file = file.read()

ars = file.split("\n")

m = 0
m2 = 0
for ar in ars:
    q = ar.replace('\'','').replace('[','').replace(']','')
    was = q.split(",")
    a1 = rn(was[0])
    a2 = rn(was[1])
    
    if contains(a1,a2) or contains(a2, a1):
        m += 1
    
    match = False
    for a in a1:
        match = a2.count(a) > 0
        print(a)
        if match == True:
            m2 += 1
            break
    print("+")
    if match == False:
        for b in a2:
            print(b)
            match = a1.count(b) > 0
            if match == True:
                m2 += 1
                break
    print(was)
    print(match)
    print("====")
        
print(m)
print(m2)
    
    