def tl(bs, i):
    l = list()
    for ba in bs:
        l.append(int(ba[i]))
    return l 

def ol(bs, rowz):
    ls = list()

    for i in rowz:
        ls.append(list())

    for ba in bs:
        for i in rowz:
            ls[i].append(int(ba[i]))
    return ls

def p1(bs):
    rowz = range(0, len(bs[0]))
    ls = ol(bs, rowz)
    gamma = list()
    elips = list()

    for i in rowz:
        zero = ls[i].count(0)
        one =  ls[i].count(1)

        if(zero > one):
            gamma.append(0)
            elips.append(1)
        else:
            gamma.append(1)
            elips.append(0)     

    gs = "".join(str(b) for b in gamma)
    ep = "".join(str(b) for b in elips)

    print(int(ep, 2) * int(gs, 2))

def p2(bs):
    rowz = range(0, len(bs[0]))
    ls = ol(bs, rowz)
    
    co = -1
    cs = -1
        
    zero = ls[0].count(0)
    one =  ls[0].count(1)
    
    if zero > one:
        co = 0
        cs = 1
    else:
        co = 1
        cs = 0
    
    ts = bs.copy()
    
    ss = list()
    os = list()
    
    for i in rowz:
        if i >= 1:
            bs = os
            os = list()
            qs = tl(bs, i)
            zero = qs.count(0)
            one =  qs.count(1)
            if zero > one:
                co = 0
            else:
                co = 1
        if len(bs) == 1:
            os = bs
            break
        for b in bs:
            if b[i] == str(co):
                os.append(b)
    
    for i in rowz:
        if i >= 1:
            ts = ss
            ss = list()
            qs = tl(ts, i)
            zero = qs.count(0)
            one =  qs.count(1)
            print("zero: " + str(zero))
            print("one: " +str(one))
            if one < zero:
                cs = 1
            else:
                cs = 0
            print(cs)
        if len(ts) == 1:
            ss = ts
            break
        for b in ts:
            if b[i] == str(cs):
                print(b)
                ss.append(b)            
    
    print(os[0]) 
    print(ss[0])
    print(int(os[0])*int(ss[0]))
    print(int(os[0], 2) * int(ss[0], 2))


with open('03.txt', 'r') as file:
    file = file.read()

bs = file.split("\n")
#p1(bs)
p2(bs)