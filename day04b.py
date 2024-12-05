f = open("input.txt", "r")

lines = f.read().split('\n')
lines = [[c for c in line] for line in lines]

def h(lines, x, y):
	c = 0

	# check bounds
	if x == 0 or x == len(lines)-1:
		return 0
	if y == 0 or y == len(lines[0])-1:
		return 0

	# check for two MAS's (awful) 
	a = 1
	b = 1
	test =  ''.join([lines[x+(i-1)*a][y+(i-1)*b] for i in range(3)])
	if test == 'MAS' or test == 'SAM':
		c += 1
	a = 1
	b = -1
	test =  ''.join([lines[x+(i-1)*a][y+(i-1)*b] for i in range(3)])
	if test == 'MAS' or test == 'SAM':
		c += 1
	return c==2

ans = 0
for x in range(len(lines)):
	for y in range(len(lines[0])):
		ans += h(lines, x, y)

print(ans)