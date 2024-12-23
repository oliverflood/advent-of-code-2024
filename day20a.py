f = open("input.txt", "r")
grid = f.read().split('\n')
grid = [list(line) for line in grid]
dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]

start = [0, 0]
end = [0, 0]
for r, line in enumerate(grid):
	for c, char in enumerate(line):
		if char == 'S':
			start = [r, c]
		if char == 'E':
			end = [r, c]

def tup_sum(a, b):
	return [a[0] + b[0], a[1] + b[1]]

def in_bounds(a):
	return 0 <= a[0] < len(grid) and 0 <= a[1] < len(grid[0])

def dist(g):
	q = [start]
	visited = [[-1 for _ in range(len(line))] for line in grid]
	visited[start[0]][start[1]] = 0

	while q:
		curr = q.pop(0)
		if curr == end:
			break
		for d in dirs:
			new = tup_sum(curr, d)
			if in_bounds(new) and g[new[0]][new[1]] != '#' and visited[new[0]][new[1]] == -1:
				q.append(new)
				visited[new[0]][new[1]] = visited[curr[0]][curr[1]] + 1
		# for line in visited:
		# 	print(line)
		# print('\n')

	# assert(visited[end[0]][end[1]] != -1)
	return visited[end[0]][end[1]]

def cheatable(a):
	if not (0 < a[0] < len(grid)-1 and 0 < a[1] < len(grid[0])-1):
		return False
	if grid[a[0]][a[1]] != '#':
		return False
	l = [grid[tup_sum(a, d)[0]][tup_sum(a, d)[1]] for d in dirs]
	return l.count('.') + l.count('E') + l.count('S') >= 2


time = dist(grid)

ans_list = []
ans = 0
for r, line in enumerate(grid):
	print(r)
	for c, char in enumerate(line):
		if cheatable([r, c]):
			new_grid = [[c for c in line] for line in grid]
			new_grid[r][c] = '.'
			# print(time - dist(new_grid))
			ans_list.append(time-dist(new_grid))
			if time - dist(new_grid) >= 100:
				ans += 1

from collections import Counter

print(ans_list)
print(Counter(ans_list))

print(ans)

# this part 1 got written over as I started working on part 2 in here
# too lazy to fix it now