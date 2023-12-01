with open('02t.txt', 'r') as file:
    file = file.read()
    
cmds = file.split("\n")

fw = list()
depth = list()
aim = 0
for cmd in cmds:
    if "forward" in cmd:
        r = int(cmd.replace("forward ", ''))
        fw.append(r)
    else:
        if "up" in cmd:
            d= -int(cmd.replace("up ",''))
        else:
            d = int(cmd.replace("down", ''))
        depth.append(d)
        aim += d
print(fw)
print(depth)

fr = 0
dr = 0
for f in fw:
    fr += f

for d in depth:
    dr += d
    
print(str(dr*fr))