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

grid = [[0 for _ in range(width)] for _ in range(height)]

for pos in ps:
	grid[pos[1]][pos[0]] += 1

# finds tree at about 7300
for sec in range(10000):
	for i in range(len(ps)):
		grid[ps[i][1]][ps[i][0]] -= 1
		grid[(ps[i][1] + vs[i][1]) % l[1]][(ps[i][0] + vs[i][0]) % l[0]] += 1
		for j in range(2):
			ps[i][j] += vs[i][j]
			ps[i][j] %= l[j]

	dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
	perimiter = 0
	for r, line in enumerate(grid):
		for c, item in enumerate(line):
			for d in dirs:
				if item != 0 and grid[(r+d[1])%height][(c+d[0])%width] == 0:
					perimiter += 1

	if sec % 100 == 0:
		print(sec)

	# print out tree & info
	if perimiter < 1500:
		print('\n sec:', sec, 'p:', perimiter, '----------------------------------')
		for r, line in enumerate(grid):
			for c, item in enumerate(line):
				if item != 0:
					print('#', end='')
				else:
					print(' ', end='')
			print()
