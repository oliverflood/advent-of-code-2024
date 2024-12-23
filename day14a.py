import re
f = open("input.txt", "r")

pattern = r"[-]?\d+"
lines = f.read().split('\n')
lines = [list(map(int, re.findall(pattern, line))) for line in lines]

ps = [[line[0], line[1]] for line in lines] 
vs = [[line[2], line[3]] for line in lines] 

width = 101
height = 103
l = [width, height]

for sec in range(100):
	for i in range(len(ps)):
		for j in range(2):
			ps[i][j] += vs[i][j]
			ps[i][j] %= l[j]

quads = [0, 0, 0, 0]
for pos in ps:
	if pos[0] < width//2 and pos[1] < height//2:
		quads[3] += 1
	if pos[0] > width//2 and pos[1] < height//2:
		quads[0] += 1
	if pos[0] > width//2 and pos[1] > height//2:
		quads[1] += 1
	if pos[0] < width//2 and pos[1] > height//2:
		quads[2] += 1

from math import prod
ans = prod(quads)
print(ans)