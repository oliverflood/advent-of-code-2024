f = open("input.txt", "r")

lines = f.read()
lines = [line.split(': ') for line in lines.split('\n')]

left = [int(line[0]) for line in lines]
right = [list(map(int, line[1].split(' '))) for line in lines]

def recurse(l, r, curr):
	if len(r) == 0:
		return l == curr

	return recurse(l, r[1:], curr + r[0]) or recurse(l, r[1:], curr * r[0])

ans = sum(recurse(left[i], right[i][1:], right[i][0]) * left[i] for i in range(len(left)))
print(ans)