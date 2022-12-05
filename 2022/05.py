def cr(cts):
    rows = cts.split("\n")
    lr = str(rows[len(rows)-1:])
   
    lrs = lr.strip()

    ar = qr[len(lr)-4]
    ra= range(0,int(ar))
    
    st = list()
    for r in ra:
        st.append(list())
    
    startSplit = 4
    
    rows.pop()
    for r in rows:
        for i in ra:           
            sp = startSplit*i
            ep = startSplit*i + 3
            b = r[sp:ep].strip()
            if b != "":
                st[i].insert(0,b)
    return st
    
def cm(insc, st):
    ins = insc.split("\n")
    for instruction in ins:
        ni = instruction.split(" ")
        am = int(ni[1])
        fr = int(ni[3])-1
        to = int(ni[5])-1
        res = st[fr][-am:]#add for part 1[::-1]
    
        for r in res:
            st[to].append(r)
        st[fr] = st[fr][:-am]
  
    for r in st:
        print(r[-1])
        
with open('05.txt', 'r') as file:
    file = file.read()

d = file.split("\n\n")

cts = d[0]
ins = d[1]

st = cr(cts)
cm(ins,st)
