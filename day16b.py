f = open("input.txt", "r")
lines = f.read().split('\n')

grid = [list(line) for line in lines]
start = [0, 0]
end = [0, 0]
dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]

for r, line in enumerate(grid):
	for c, char in enumerate(line):
		if char == 'S':
			start = [r, c]
		if char == 'E':
			end = [r, c]

import heapq
queue = [[0, start, dirs[3], []]]
heapq.heapify(queue)

print(queue)
visited = {}

good = set()
counter = 0
ans = 0

numgrid = [[float('inf') for _ in line] for line in grid]


################# This whole day was a mess- solved by tinkering with the input after getting close
while queue:
	score, pos, currd, history = heapq.heappop(queue)

	# if visited.get(tuple(pos+currd), 0) != 0:
	if visited.get(tuple(pos+currd), 0) != 0:
		continue
	# if numgrid[pos[0]][pos[1]] != float('inf'):
	# 	continue
	visited[tuple(pos+currd)] = score
	numgrid[pos[0]][pos[1]] = min(numgrid[pos[0]][pos[1]], score%1000)

	counter += 1
	if counter % 10000 == 0:

	# if score < 6000:
		print(score, pos, currd)
	if ans != 0 and score > ans:
		break
	if grid[pos[0]][pos[1]] == 'E':
		ans = score
		for tile in history:
			good.add(tuple(tile))
			good.add(tuple(pos))

	d1, d2, d3 = dirs[(dirs.index(currd)+1)%4], currd, dirs[(dirs.index(currd)-1)%4]
	if grid[pos[0] + d1[0]][pos[1] + d1[1]] == '#':
		if grid[pos[0] + d2[0]][pos[1] + d2[1]] == '#':
			if grid[pos[0] + d3[0]][pos[1] + d3[1]] == '#':
				continue
	
	if grid[pos[0] + currd[0]][pos[1] + currd[1]] != '#':
		heapq.heappush(queue, [score+1, [pos[0] + currd[0], pos[1] + currd[1]], currd, history+[pos]])
	
	currd = dirs[(dirs.index(currd)+1)%4]
	if grid[pos[0] + currd[0]][pos[1] + currd[1]] != '#':
		heapq.heappush(queue, [score+1000, pos, currd, history+[pos]])
	
	currd = dirs[(dirs.index(currd)+2)%4]
	if grid[pos[0] + currd[0]][pos[1] + currd[1]] != '#': 
		heapq.heappush(queue, [score+1000, pos, currd, history+[pos]])

ans = []
ans.append(end)

queue = [end]
while queue:
	pos = queue.pop()
	score = numgrid[pos[0]][pos[1]]

	for d in dirs:

		newpos = [pos[0] + d[0], pos[1] + d[1]]
		newscore = numgrid[newpos[0]][newpos[1]]

		if newscore == (score-1) and newscore != -1:
			queue.append(newpos)
			ans.append(newpos)

ans = list(map(tuple, ans))
ans = set(ans)

for r, line in enumerate(grid):
	for c, char in enumerate(line):
		if (r, c) in ans:
			print('O', end='')
		else:
			print(char, end='')
	print()

print('final ans', len(ans))