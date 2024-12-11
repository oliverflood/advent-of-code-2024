f = open("input.txt", "r")

lines = f.read().split('\n')
lines = [[int(c) for c in line] for line in lines]

# print(lines)

def score(r, c):
	dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

	if lines[r][c] == 9:
		return 1

	arr = [[r+d[0], c+d[1]] for d in dirs]
	arr = list(filter(lambda pair: 0 <= pair[0] < len(lines) and 0 <= pair[1] < len(lines[0]), arr))
	arr = list(filter(lambda pair: lines[pair[0]][pair[1]] == lines[r][c]+1, arr))

	if len(arr) == 0:
		return 0
	return sum(score(pair[0], pair[1]) for pair in arr)
	
ans = 0
for r in range(len(lines)):
	for c in range(len(lines[r])):
		if lines[r][c] == 0:
			ans += score(r, c)

print(ans)