f = open("input.txt", "r")
import numpy as np
import re

pattern = r"\d+"
machines = f.read().split('\n\n')
machines = [machine.split('\n') for machine in machines]
machines = [[list(map(int, re.findall(pattern, row))) for row in machine] for machine in machines]

alist = [np.array([[machine[0][0], machine[1][0]], [machine[0][1], machine[1][1]]]) for machine in machines]
blist = [np.array([machine[2][0] + 10000000000000, machine[2][1] + 10000000000000]) for machine in machines]

ans = 0
for i in range(len(alist)):
	x = np.linalg.solve(alist[i], blist[i])
	int_x = np.round(x).astype(np.int64)

	if np.array_equiv(np.matmul(alist[i], int_x), blist[i]):
		ans += int_x[0]*3 + int_x[1]
		answers[i][0] = x.astype(int)

print(ans)