f = open("input.txt", "r")

lines = f.read()
lines = lines.split('\n')
visited = [[set() for _ in line] for line in lines]

r, c = 0, 0
for i, line in enumerate(lines):
	if '^' in line:
		c = line.index('^')
		r = i

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
	

def loops(obs_r, obs_c, r, c):
	visited = [[set() for _ in line] for line in lines]
	d = 0

	visited[r][c].add(d)
	while (0 <= r+dirs[d][0] < len(lines)) and (0 <= c+dirs[d][1] < len(lines[0])):
		if lines[r+dirs[d][0]][c+dirs[d][1]] == '#':
			d += 1
			d %= 4
			continue
		elif r+dirs[d][0] == obs_r and c+dirs[d][1] == obs_c:
			d += 1
			d %= 4
			continue
		else:
			r += dirs[d][0]
			c += dirs[d][1]
		
		if d in visited[r][c]:
			return True
		visited[r][c].add(d)
	return False

print(loops(0, 3, r, c))
print('rows', len(lines))
print('cols', len(lines[0]))

ans = 0
for obs_c in range(len(lines[0])):
	print(obs_c)
	for obs_r in range(len(lines)):

		ans += loops(obs_r, obs_c, r, c)

print(ans)