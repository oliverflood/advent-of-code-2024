f = open("input.txt", "r")
lines = f.read().split("\n")
lines = [line.split("   ") for line in lines]
a = [line[0] for line in lines]
b = [line[1] for line in lines]
a.sort()
b.sort()

diffs = []
for i in range(len(a)):
    diffs.append(abs(int(a[i])-int(b[i])))

print(sum(diffs))