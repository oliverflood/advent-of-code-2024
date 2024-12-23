f = open("input.txt", "r")
grid, moves = f.read().split('\n\n')
grid = grid.split('\n')
new_grid = [[] for _ in grid]
for r, line in enumerate(grid):
	for c in line:
		if c == 'O':
			new_grid[r].append('[')
			new_grid[r].append(']')
		elif c == '@':
			new_grid[r].append('@')
			new_grid[r].append('.')
		else:
			new_grid[r].append(c)
			new_grid[r].append(c)
grid = new_grid

moves = ''.join(moves.split('\n'))
dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
movemap = {'^': dirs[1], 'v': dirs[0], '<': dirs[2], '>': dirs[3]}
moves = [movemap[move] for move in moves]

def print_grid():
	for line in grid:
		print(''.join(line))
	print()

def push(r, c, d, partner_called):
	next_type = grid[r + d[0]][c + d[1]]

	if next_type == '#':
		return False
	elif next_type == '.':
		grid[r + d[0]][c + d[1]] = grid[r][c]
		grid[r][c] = '.'
		return True

	elif next_type == '[' or next_type == ']':
		if d[0] == 0:
			push(r + d[0], c + d[1], d, False)
			grid[r + d[0]][c + d[1]] = grid[r][c]
			grid[r][c] = '.'
		if d[0] != 0:
			push(r + d[0], c + d[1], d, False)
			if not partner_called: 
				if next_type == '[':
					push(r, c + 1, d, True)
				if next_type == ']':
					push(r, c - 1, d, True)

				grid[r + d[0]][c + d[1]] = grid[r][c]
				grid[r][c] = '.'

def pushable(r, c, d, partner_called):
	next_type = grid[r + d[0]][c + d[1]]

	if next_type == '#':
		return False
	elif next_type == '.':
		return True
	elif next_type == '[' or next_type == ']':
		if d[0] == 0:
			return pushable(r + d[0], c + d[1], d, False)
		if d[0] != 0:
			if partner_called:
				return pushable(r + d[0], c + d[1], d, False)
			if not partner_called: 
				if next_type == '[':
					return pushable(r + d[0], c + d[1], d, False) and pushable(r, c + 1, d, True) 
				if next_type == ']':
					return pushable(r + d[0], c + d[1], d, False) and pushable(r, c - 1, d, True) 


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
		push(curr_r, curr_c, d, False)
		curr_r += d[0]
		curr_c += d[1]

	elif next_type == '[' or next_type == ']':
		if pushable(curr_r, curr_c, d, False):
			push(curr_r, curr_c, d, False)
			curr_r += d[0]
			curr_c += d[1]

ans = 0
for r, line in enumerate(grid):
	for c, char in enumerate(line):
		ans += (char == '[')*(100*r + c)

print(ans)