f = open("input.txt", "r")
blocks = f.read().split('\n\n')

blocks = [block.split('\n') for block in blocks]
locks = []
keys = []

def conv_lock(block):
	ans = [0 for _ in range(len(block[0]))]
	for c in range(len(ans)):

		for r in range(len(block)):
			if block[r][c] == '.':
				ans[c] = r-1
				break

	return ans


def conv_key(block):
	ans = [0 for _ in range(len(block[0]))]
	for c in range(len(ans)):
		for r in range(len(block)):
			if block[r][c] == '#':
				ans[c] = 7-r-1
				break

	return ans

for block in blocks:
	if block[0] == '#####':
		locks.append(block)
	else:
		keys.append(block)

# print(locks)
# print(keys)
# #locks, keys

# print(conv_lock(locks[0]))
# print(conv_key(keys[0]))

def fits(k, l):
	ck = conv_key(k)
	cl = conv_lock(l)

	return all(ck[i] + cl[i] <= 5 for i in range(5))

ans = 0
for k in keys:
	for l in locks:
		if fits(k, l):
			ans += 1

print(ans)