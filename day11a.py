f = open("input.txt", "r")

stones = list(map(int, f.read().split(' ')))

for i in range(75):
	print(i)
	new_stones = []
	for stone in stones:
		if stone == 0:
			new_stones.append(1)
		elif len(str(stone)) % 2 == 0:
			s = str(stone)
			a = s[0:len(s)//2]
			b = s[len(s)//2:]
			new_stones.append(int(a))
			new_stones.append(int(b))
		else:
			new_stones.append(stone*2024)
	stones = new_stones

# print(stones)
ans = len(stones)
print(ans)