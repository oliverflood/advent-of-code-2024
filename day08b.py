f = open("input.txt", "r")

lines = f.read()
tester = lines
lines = [[c for c in line] for line in lines.split('\n')]

pos_dict = {}
for r in range(len(lines)):
	for c in range(len(lines[0])):
		if lines[r][c] != '.':
			if lines[r][c] not in pos_dict:
				pos_dict[lines[r][c]] = []
			pos_dict[lines[r][c]].append([r, c])
		
def in_bounds(x):
	return (0 <= x < len(lines))

tester = [['.' for c in line] for line in tester.split()]
vals = set()

for key, value in pos_dict.items():
	for i in range(len(value)):
		for j in range(len(value)):
			if i <= j:
				continue
			diff_r = value[i][0] - value[j][0]
			diff_c = value[i][1] - value[j][1]

			tests = []
			for m in range(0, 100):
				tests.append([value[i][0] + m*diff_r, value[i][1] + m*diff_c])
				tests.append([value[j][0] - m*diff_r, value[j][1] - m*diff_c])
			
			for test in tests:
				if in_bounds(test[0]) and in_bounds(test[1]):
					tester[test[0]][test[1]] = '#'
					vals.add((test[0], test[1]))

# for line in tester:
# 	print(''.join(line))

print(len(vals))