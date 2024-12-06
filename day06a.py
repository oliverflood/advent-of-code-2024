f = open("input.txt", "r")

lines = f.read()
lines = lines.split('\n')

visited = [[0 for _ in line] for line in lines]

r, c = 0, 0
for i, line in enumerate(lines):
	if '^' in line:
		c = line.index('^')
		r = i

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
d = 0

visited[r][c] = 1
while (0 <= r+dirs[d][0] < len(lines)) and (0 <= c+dirs[d][1] < len(lines[0])):
	if lines[r+dirs[d][0]][c+dirs[d][1]] == '#':
		d += 1
		d %= 4
	else:
		r += dirs[d][0]
		c += dirs[d][1]
	visited[r][c] = 1

ans = sum(sum(line) for line in visited)
print(ans)