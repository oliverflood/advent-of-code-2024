f = open("input.txt", "r")
lines = f.read().split('\n')
edges = [line.split('-') for line in lines]
computers = list(set([x for xs in edges for x in xs]))

neighbors = {}
for l, r in edges:
	neighbors[l] = neighbors.get(l, []) + [r]
	neighbors[r] = neighbors.get(r, []) + [l]

def next(arr):
	newarr = []
	for node in arr:
		newarr += neighbors[node]
	return list(set(newarr))

# brute force
ansset = set()
for n, i in enumerate(computers):
	print(n)
	for k in computers:
		for j in computers:
			if i in neighbors[j] and j in neighbors[k] and k in neighbors[i]:
				if 't' in i[0]+j[0]+k[0]:
					ansset.add(tuple(sorted([i, j, k])))

ans = len(ansset)
print(ans)