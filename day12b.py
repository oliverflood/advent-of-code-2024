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

def count_groups(edge_set):
	visited = set()

	def fill(given):
		queue = set()
		queue.add(given)

		dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

		while queue:
			curr = queue.pop()
			visited.add(curr)

			for d in dirs:
				r2 = curr[0] + d[0]
				c2 = curr[1] + d[1]
				if (r2, c2) in edge_set and (r2, c2) not in visited:
					queue.add((r2, c2))

	c = 0
	for g in list(edge_set):
		if g not in visited:
			fill(g)
			c += 1
	return c

def perimiter(r, c):
	plant_type = lines[r][c]

	queue = [[r, c]]
	visited = [[0 for c in line] for line in lines]
	visited[r][c] = 1
	dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
	
	edges = [set() for i in range(4)] # find N,E,S,W edges separately
	while queue:
		r, c = queue.pop()
		visited[r][c] = 1
		
		for i, d in enumerate(dirs):
			r2 = r + d[0]
			c2 = c + d[1]
			if in_bounds(r2, c2) and not visited[r2][c2] and lines[r2][c2] == plant_type:
				queue.append([r2, c2])
				visited[r2][c2] = 1
			if not in_bounds(r2, c2):
				edges[i].add((r2, c2))
			elif lines[r2][c2] != plant_type:
				edges[i].add((r2, c2))

	return sum(count_groups(edges[i]) for i in range(4)) # group N,E,S,W edges

ans = 0
for r in range(len(lines)):
	for c in range(len(lines[0])):
		if not global_area_visited[r][c]:
			ans += area(r, c) * perimiter(r, c)

print(ans)