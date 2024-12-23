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
	for line in visited:
		print(line)
	print('\n')
	return visited

def cheatable(a):
	if not (0 < a[0] < len(grid)-1 and 0 < a[1] < len(grid[0])-1):
		return False
	if grid[a[0]][a[1]] != '#':
		return False
	l = [grid[tup_sum(a, d)[0]][tup_sum(a, d)[1]] for d in dirs]
	return l.count('.') + l.count('E') + l.count('S') >= 2



visited = dist(grid)
path = []

q = [start]
while q:
	curr = q.pop(0)
	path.append(curr)
	if curr == end:
		break
	for d in dirs:
		new = tup_sum(curr, d)
		if visited[new[0]][new[1]] == visited[curr[0]][curr[1]] + 1:
			q.append(new)
			break
# print(path)

node = start

# get all reachable nodes on the path in 20 moves from "node"

# LATER REALIZATION: I could have just used *ANY* reachable in 20 moves, 
# as the cheat can go through non walls, leaving my code messy here

def reachable(node):
	reach_list = []
	q = [[node, 0]]
	v = set()

	ran = 20

	while q:
		curr, dist = q.pop(0)
		if dist > ran:
			continue
		if (curr[0], curr[1]) in v:
			continue
		v.add((curr[0], curr[1]))
		if grid[curr[0]][curr[1]] != '#':
			reach_list.append([curr, dist])
		for d in dirs:
			new = tup_sum(curr, d)
			if not in_bounds(new):
				continue
			q.append([new, dist+1])

	return reach_list

def check_diff(first, second, dist):
	return visited[second[0]][second[1]] - (visited[first[0]][first[1]] + dist) >= 100

# print(reachable(start))

# for line in visited:
# 	print(line)

ans_list = []
ans = 0
for i, first in enumerate(path):
	print(i)
	reach_list = reachable(first)
	for second, dist in reach_list:
		ans += check_diff(first, second, dist)
		ans_list.append(visited[second[0]][second[1]] - (visited[first[0]][first[1]] + dist))

# print(ans_list)

final_list = []
from collections import Counter
for key, value in Counter(ans_list).items():
	if key > 0:
		final_list.append([key, value])

for k, v in sorted(final_list):
	print(k, v)

print('ans', ans)

# 221097 too low