f = open("input.txt", "r")

lines = f.read()
lines = [c for c in lines]

file_pos_lens = []
acc = 0
for p in range(len(lines)):
	if p % 2 == 0:
		file_pos_lens.append([acc, int(lines[p])])
	acc += int(lines[p])
# print(file_pos_lens)

space_pos_lens = []
acc = 0
for p in range(len(lines)):
	if p % 2 == 1:
		space_pos_lens.append([acc, int(lines[p])])
	acc += int(lines[p])
# print(space_pos_lens)

fid = 0
drive = []

for p in range(len(lines)):
	if p % 2 == 0:
		for _ in range(int(lines[p])):
			drive.append(fid)
		fid += 1
	if p % 2 == 1:
		for _ in range(int(lines[p])):
			drive.append(-1)
# print(len(drive))

for fid in reversed(range(len(file_pos_lens))):
	# print(fid)
	file_pos_len = file_pos_lens[fid]

	for i in range(len(drive)-file_pos_len[1]+1):
		if i >= file_pos_len[0]:
			break
		if drive[i:i + file_pos_len[1]] == [-1]*file_pos_len[1]:
			
			for j in range(file_pos_len[1]):
				drive[i + j] = fid
			for j in range(file_pos_len[1]):
				drive[file_pos_len[0] + j] = -1
			break


ans = 0
for i in range(len(drive)):
	if drive[i] != -1:
		ans += drive[i] * i

print(ans)