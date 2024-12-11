f = open("input.txt", "r")

lines = f.read()
lines = [int(c) for c in lines]

files = lines[0::2]
spaces = lines[1::2]

file = []
for i in range(len(files)):
	for _ in range(files[i]):
		file.append(i)

l = 0 
r = len(file)-1
c = 0
ans = 0

for p in range(len(lines)):
	if p % 2 == 0:
		for _ in range(lines[p]):
			ans += c * file[l]
			c += 1
			if c == len(file):
				break
			l += 1
			
	if p % 2 == 1:
		for _ in range(lines[p]):
			ans += c * file[r]
			c += 1
			if c == len(file):
				break
			r -= 1
	
	if c == len(file):
				break

print(ans)