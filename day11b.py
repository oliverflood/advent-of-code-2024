f = open("input.txt", "r")

stones = list(map(int, f.read().split(' ')))

stones = {stone: 1 for stone in stones}

for i in range(75):
	new_stones = {}
	for stone in stones.keys():
		if stone == 0:
			new_stones[1] = new_stones.get(1, 0) + stones[stone]
		elif len(str(stone)) % 2 == 0:
			s = str(stone)
			a = s[0:len(s)//2]
			b = s[len(s)//2:]
			new_stones[int(a)] = new_stones.get(int(a), 0) + stones[stone]
			new_stones[int(b)] = new_stones.get(int(b), 0) + stones[stone]
		else:
			new_stones[stone*2024] = new_stones.get(stone*2024, 0) + stones[stone]
	stones = new_stones

# print(stones)
ans = sum(stones[key] for key in stones.keys())
print(ans)