with open('04t.txt', 'r') as file:
    file = file.read()
    
bbi = file.split("\n")

ins = bbi[0]
del bbi[0:2]

bbs = list()
b = list()
cb = list()

rl = len(bbi[0])
cr = list()

for bb in bbi:
    if bb == "":
        b.append(cb)
        cb = list()
        continue
    cr = list()
    row = list(bb)
    pre = ""
    for i in row:
        if i == " ":
            if len(pre) > 0:
                cr.append(pre)
            pre = ""
        else:
            pre += i
    cr.append(pre)
    cb.append(cr)

b.append(cb)

print(str(len(b)))