f = open("input.txt", "r")

lines = f.read().split('\n')
lines = [[int(c) for c in line] for line in lines]

print(lines)

def get_score(r, c):
	visited = [[0 for c in line] for line in lines]
	dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
	queue = [[r, c]]
	nines = 0

	while queue:
		visited[r][c] = 1
		temp = queue.pop()
		r = temp[0]
		c = temp[1]
		if lines[r][c] == 9:
			nines += 1
			continue

		for d in dirs:
			if not (0 <= r+d[0] < len(lines) and 0 <= c+d[1] < len(lines[0])):
				continue
			if visited[r+d[0]][c+d[1]]:
				continue
			if lines[r][c]+1 == lines[r+d[0]][c+d[1]]:
				queue.append([r+d[0], c+d[1]])

	return nines
	
ans = 0
for r in range(len(lines)):
	for c in range(len(lines[r])):
		if lines[r][c] == 0:
			ans += get_score(r, c)

print(ans)