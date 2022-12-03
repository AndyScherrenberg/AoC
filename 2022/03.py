def chunks(L, n): return [L[x: x+n] for x in range(0, len(L), n)]

def cp(i):
    lc = list("abcdefghijklmnopqrstuvwxyz")
    uc = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    p = 0
    
    if i in lc :
        p = lc.index(i) + 1
    else:
        p = uc.index(i) + 27
    #print(p)
    #print(i)
    #print("-----------")
    return p

with open('03.txt', 'r') as file:
    file = file.read()

rs = file.split("\n")


prio = 0

for r in rs:
    c1 = r[:len(r)//2]
    c2 = r[len(r)//2:]
    #print(c1)
    #print(c2)
    #print("====")
    l1 = list(c1)
    l2 = list(c2)
    for i in l1:
        if l2.count(i) >= 1:
            prio += cp(i)
            break

print("result part 1 = " + str(prio))
prio = 0

gs = chunks(rs, 3)

for g in gs:
    e1 = g[0]
    e2 = g[1]
    e3 = g[2]
    
    for i in e1:
        if e2.count(i) >= 1 and e3.count(i) >= 1:
            #print(i)
            prio += cp(i)
            break;

print("result part 2 = " + str(prio))



