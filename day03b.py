##### How I originally did it
f = open("input.txt", "r")

lines = f.read()
lines = lines.split('mul(')
lines = [line.split(')') for line in lines]
lines = [[s.split(',') for s in line] for line in lines]

ans = 0
do = 1

for line in lines:
    for s in line:
        for item in s:
            if item[-6:] == 'don\'t(':
                do = 0
            if item[-3:] == 'do(':
                do = 1
        try:
            a = int(s[0])
            b = int(s[1])
            ans += a*b*do
        except:
            pass

print(ans)




##### How I should have done it lmao
##### rewrote this later after rushing to solve at first 
##### I never remember regex :(
import re

f = open("input.txt", "r")
line = f.read()

pattern = r"don\'t\(\)|do\(\)|mul\(\d+,\d+\)"
lines = re.findall(pattern, line)

ans = 0
do = 1

for item in lines:
    if item[0] == 'm':
        pattern = r"\d+"
        a, b = re.findall(pattern, item)
        ans += int(a)*int(b)*do
    elif item == 'do()':
        do = 1
    else:
        do = 0

print(ans)