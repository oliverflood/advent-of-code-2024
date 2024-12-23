f = open("input.txt", "r")
squares = f.read().split('\n')
squares = [list(map(int, square.split(','))) for square in squares]

size = 71
grid = [[0 for _ in range(size)] for _ in range(size)]

def tupadd(a, b):
	return [a[0]+b[0], a[1]+b[1]]

def in_bounds(a):
	return 0 <= a[0] < size and 0 <= a[1] < size

def pathable(grid):
	tempgrid = [[item for item in line] for line in grid]
	dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]
	q = [[0, 0]]

	while q:
		curr = q.pop(0)
		if curr == [size-1, size-1]:
			break

		for d in dirs:
			n = tupadd(curr, d)
			if in_bounds(n) and tempgrid[n[0]][n[1]] == 0:
				q.append(n)
				tempgrid[n[0]][n[1]] = tempgrid[curr[0]][curr[1]] + 1

	ans = tempgrid[size-1][size-1]
	return ans

for i, square in enumerate(squares[:1024]):
	grid[square[1]][square[0]] = -1

print(pathable(grid))

# part 1 remade, was overwritten with part 2 stuff originally