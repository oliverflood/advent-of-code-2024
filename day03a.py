f = open("input.txt", "r")

lines = f.read()
lines = lines.split('mul(')
lines = [line.split(')') for line in lines]
lines = [[s.split(',') for s in line] for line in lines]
print(lines)

ans = 0

for line in lines:
    for s in line:
        try:
            a = int(s[0])
            b = int(s[1])
            ans += a*b
        except:
            pass

print(ans)

# this is awful part b has better regex sol