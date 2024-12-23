f = open("input.txt", "r")
lines = f.read().split('\n')
edges = [line.split('-') for line in lines]
computers = list(set([x for xs in edges for x in xs]))

# sets for fast union/intersection
neighbors = {}
for l, r in edges:
	neighbors[l] = neighbors.get(l, set()).union({r})
	neighbors[r] = neighbors.get(r, set()).union({l})

# list for ordered neighbors
neighbors_l = {}
for l, r in edges:
	neighbors_l[l] = neighbors_l.get(l, []) + [r]
	neighbors_l[r] = neighbors_l.get(r, []) + [l]

maxgrp = {}
for cnum, computer in enumerate(computers):
	print(cnum, computer)

	# silly brute force all subsets of neighbors
	for num in range(2**13):
		binary = '0'*(13-len(bin(num)[2:])) + bin(num)[2:]
		
		currgrp = {computer}
		for i, neigh in enumerate(neighbors_l[computer]):
			if binary[i] == '1':
				currgrp.add(neigh)

		for i, neigh in enumerate(neighbors_l[computer]):
			if binary[i] == '1':
				currgrp = currgrp & (neighbors[neigh] | {neigh})

		if len(currgrp) > len(maxgrp):
			maxgrp = currgrp

maxgrp = list(maxgrp)
maxgrp.sort()

ans = ''
for item in maxgrp:
	ans += item + ','
print(ans[:-1])