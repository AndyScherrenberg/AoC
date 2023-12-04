import re

with open('03.txt', 'r') as file:
    file = file.read()
    
instr = file.split("\n")


symbols = ["$", "+","*", "#"]


def get_digit(idx, line):
    digit_index_test = []
    digit_value_test = ""
    digit_values = []
    for c,k in enumerate(line):
        if (k.isdigit()):
            digit_value_test += k
            digit_index_test.append(c)
        else:
            if (idx in digit_index_test or (idx-1) in digit_index_test or (idx+1) in digit_index_test):
                digit_values.append(int(digit_value_test))       
            digit_index_test = []
            digit_value_test = ""
    return digit_values

def gear_ratio(pline,cline,nline):
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print(pline)
    print(cline)
    print(nline)
    cline_gear_ratio = 0
    for c,k in enumerate(cline):
        if k == "*":
            p_digit = get_digit(c, pline)
            c_digit = get_digit(c, cline)
            n_digit = get_digit(c, nline)
            result = p_digit + c_digit + n_digit
            
            if (len(result) > 1):
                a = 1
                for r in result:
                    a *= r
                cline_gear_ratio += a
                print(p_digit,c_digit,n_digit, a)
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    return cline_gear_ratio
            

def digit_connect(idx, line):
    symbol_index = []
    for c,k in enumerate(line):
        if (k != "." and k.isdigit() == False):
            symbol_index.append(c)
    for ni in idx:
        if (ni in symbol_index or (ni-1) in symbol_index or (ni+1) in symbol_index):
            return True
    else: 
        return False

def digit_connects(cline, pline, nline):
    value = 0
    digit_index = []
    digit_value = ""
    for c,k in enumerate(line):
        if (k.isdigit()):
            digit_value += k
            digit_index.append(c)
        else:
            co_c = digit_connect(digit_index, cline)
            co_p = digit_connect(digit_index, pline)
            co_n = digit_connect(digit_index, nline)
            if (co_c or co_p or co_n):
                print(digit_value)
                value += int(digit_value)
            digit_index = []
            digit_value = ""
       
    co_c = digit_connect(digit_index, cline)
    co_p = digit_connect(digit_index, pline)
    co_n = digit_connect(digit_index, nline)
    if (co_c or co_p or co_n):
        print(digit_value)
        value += int(digit_value)
    return value

result_1,result_2 = 0  ,0
for idx,line in enumerate(instr):
    if (idx == 0):
        continue
    p = ""
    if idx > 0:
        p = instr[idx-1]
    c = line
    n = ""
    if idx+1 < len(instr):
        n = instr[idx+1]
    #result_1 += digit_connects(c,p,n)
    result_2 += gear_ratio(p,c,n)
   
print(result_1)
print(result_2)
    