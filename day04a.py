f = open("input.txt", "r")

lines = f.read().split('\n')
lines = [[c for c in line] for line in lines]
tester = [['.' for c in line] for line in lines]

def h(lines, x, y):
	c = 0
	arr = [1, 0, -1]
	for a in arr:
		for b in arr:
			if a == b and a == 0:
				continue

			if not (0 <= x+3*a < len(lines)):
				continue
			if not (0 <= y+3*b < len(lines[0])):
				continue
			
			try:
				test = ''.join([lines[x+i*a][y+i*b] for i in range(4)])
				if test == 'XMAS':
					# print(x, y, "  ", a, b)
					tester[x][y] = 'X'
					c += 1
			except:
				pass
	
	return c

ans = 0
for x in range(len(lines)):
	for y in range(len(lines[0])):
		ans += h(lines, x, y)



print(ans)
# for line in tester:
# 	print(''.join(line))