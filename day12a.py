f = open("input.txt", "r")

lines = f.read().split('\n')
lines = [[c for c in line] for line in lines]
global_area_visited = [[0 for c in line] for line in lines]

def in_bounds(r, c):
	return 0 <= r < len(lines) and 0 <= c < len(lines[0])

def area(r, c):
	plant_type = lines[r][c]

	queue = [[r, c]]
	visited = [[0 for c in line] for line in lines]
	visited[r][c] = 1
	dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]

	while queue:
		r, c = queue.pop()
		visited[r][c] = 1
		global_area_visited[r][c] = 1
		
		for d in dirs:
			r2 = r + d[0]
			c2 = c + d[1]
			if in_bounds(r2, c2) and not visited[r2][c2] and lines[r2][c2] == plant_type:
				queue.append([r2, c2])

	return sum(sum(v) for v in visited)

def perimiter(r, c):
	plant_type = lines[r][c]

	queue = [[r, c]]
	visited = [[0 for c in line] for line in lines]
	visited[r][c] = 1
	dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]

	p = 0

	while queue:
		r, c = queue.pop()
		visited[r][c] = 1
		
		for d in dirs:
			r2 = r + d[0]
			c2 = c + d[1]
			if in_bounds(r2, c2) and not visited[r2][c2] and lines[r2][c2] == plant_type:
				queue.append([r2, c2])
				visited[r2][c2] = 1
			if not in_bounds(r2, c2):
				p += 1
			elif lines[r2][c2] != plant_type:
				p += 1

	return p

ans = 0
for r in range(len(lines)):
	for c in range(len(lines[0])):
		if not global_area_visited[r][c]:
			ans += area(r, c) * perimiter(r, c)

print(ans)