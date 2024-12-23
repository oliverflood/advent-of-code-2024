f = open("input.txt", "r")
lines = f.read().split('\n')

grid = [list(line) for line in lines]
start = [0, 0]
dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]

for r, line in enumerate(grid):
	for c, char in enumerate(line):
		if char == 'S':
			start = [r, c]

import heapq
queue = [[0, start, dirs[3], []]]
heapq.heapify(queue)

# print(queue)
visited = {}
good = set()
counter = 0
ans = 0

############# NOTE: started working on part 2 in this file so my original part 1 code is lost
while queue:

	score, pos, currd, history = heapq.heappop(queue)

	# counter += 1
	# if counter % 100000 == 0:
	# 	print(score, pos, currd)
	# 	print(len(queue))

	if score > 11048:
		continue
	if visited.get(tuple(pos+currd), 0) != 0:
		for tile in history:
			visited[tuple(pos+currd)].add(tuple(tile))
		continue
	visited[tuple(pos+currd)] = set()
	for tile in history:
		visited[tuple(pos+currd)].add(tuple(tile))


	print(score, pos, currd)
	if ans != 0 and score > ans:
		break
	if grid[pos[0]][pos[1]] == 'E':
		ans = score
		for thing in history:
			good = good.union(visited[thing])
			# good.add(tuple(tile))
			# good.add(tuple(pos))
		break

	d1, d2, d3 = dirs[(dirs.index(currd)+1)%4], currd, dirs[(dirs.index(currd)-1)%4]
	if grid[pos[0] + d1[0]][pos[1] + d1[1]] == '#':
		if grid[pos[0] + d2[0]][pos[1] + d2[1]] == '#':
			if grid[pos[0] + d3[0]][pos[1] + d3[1]] == '#':
				continue
	
	if grid[pos[0] + currd[0]][pos[1] + currd[1]] != '#':
		# if visited.get(tuple([pos[0] + currd[0], pos[1] + currd[1]]+currd), 0) <= score+1 and score+1000 <= 11048:
		heapq.heappush(queue, [score+1, [pos[0] + currd[0], pos[1] + currd[1]], currd, history+[tuple(pos+currd)]])
	
	currd = dirs[(dirs.index(currd)+1)%4]
	if grid[pos[0] + currd[0]][pos[1] + currd[1]] != '#':
		# if visited.get(tuple(pos+currd), 0) <= score+1000 and score+1000 <= 11048:
		heapq.heappush(queue, [score+1000, pos, currd, history+[tuple(pos+currd)]])
	
	currd = dirs[(dirs.index(currd)+2)%4]
	if grid[pos[0] + currd[0]][pos[1] + currd[1]] != '#': 
		# if visited.get(tuple(pos+currd), 0) <= score+1000 and score+1000 <= 11048:
		heapq.heappush(queue, [score+1000, pos, currd, history+[tuple(pos+currd)]])


print('ans:', len(good))
for r, line in enumerate(grid):
	for c, char in enumerate(line):
		if (r, c) in good:
			print('O', end='')
		else:
			print(char, end='')
	print()