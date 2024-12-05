f = open("input.txt", "r")
lines = f.read().split("\n")
lines = [line.split("   ") for line in lines]
a = [int(line[0]) for line in lines]
b = [int(line[1]) for line in lines]
a.sort()
b.sort()

from collections import Counter
c = Counter(b)

ans = 0
for num in a:
    ans += num*c[num]

print(ans)