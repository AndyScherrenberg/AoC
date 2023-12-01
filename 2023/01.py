import re

with open('01.txt', 'r') as file:
    file = file.read()
    
instr = file.split("\n")
written = ["one", "two","three", "four", "five", "six", "seven", "eight", "nine"]
p1,p2 = 0,0

def get_written_numbers(line):
    numbers = []
    for c in re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|\d))",line):
        if c.isdigit():
            numbers.append(c)
        else:
            numbers.append(str(written.index(c) + 1))
    return numbers
    
def get_numbers(line):
    numbers = []
    for c in line:
        if c.isdigit():
            numbers.append(c)
    return numbers
    
def get_value(numbers):
    return int(numbers[0] + numbers[-1])
    
for line in instr:
    p1 += get_value(get_numbers(line))
    p2 += get_value(get_written_numbers(line))

print(p1)
print(p2)