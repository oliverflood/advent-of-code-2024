f = open("input.txt", "r")
grid, moves = f.read().split('\n\n')
grid = [[c for c in line] for line in grid.split('\n')]
moves = ''.join(moves.split('\n'))

dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
movemap = {'^': dirs[1], 'v': dirs[0], '<': dirs[2], '>': dirs[3]}
moves = [movemap[move] for move in moves]

def push(r, c, d):
	next_type = grid[r + d[0]][c + d[1]]

	if next_type == '#':
		return False
	elif next_type == '.':
		grid[r + d[0]][c + d[1]] = grid[r][c]
		grid[r][c] = '.'
		return True
	elif next_type == 'O':
		check = push(r + d[0], c + d[1], d)
		if check:
			grid[r + d[0]][c + d[1]] = grid[r][c]
			grid[r][c] = '.'
		return check

curr_r, curr_c = 0, 0
for r, line in enumerate(grid):
	for c, char in enumerate(line):
		if char == '@':
			curr_r, curr_c = r, c

for i, d in enumerate(moves):
	next_type = grid[curr_r + d[0]][curr_c + d[1]]

	if next_type == '#':
		pass
	elif next_type == '.':
		push(curr_r, curr_c, d)
		curr_r += d[0]
		curr_c += d[1]
	elif next_type == 'O':
		if push(curr_r, curr_c, d):
			curr_r += d[0]
			curr_c += d[1]
	else:
		assert(False)

ans = 0
for r, line in enumerate(grid):
	for c, char in enumerate(line):
		ans += (char == 'O')*(100*r + c)

print(ans)