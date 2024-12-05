f = open("input.txt", "r")

lines = f.read().split("\n")
lines = [line.split(" ") for line in lines]
lines = [[int(a) for a in line] for line in lines]

def safe(line):
    inc_or_dec = all(line[i] < line[i+1] for i in range(len(line)-1)) or all(line[i] > line[i+1] for i in range(len(line)-1))
    diff = all(1 <= abs(line[i]-line[i+1]) <= 3 for i in range(len(line)-1))
    return inc_or_dec and diff

def new_safe(line):
    ans = False
    for i in range(len(line)):
        ans = ans or safe(line[0:i] + line[i+1:])
    return ans

ans = sum(new_safe(line) for line in lines)
print(ans)