f = open("input.txt", "r")
initials, lines = f.read().split('\n\n')
initials = initials.split('\n')
initials = [initial.split(': ') for initial in initials]

# print(initials, lines)
dic = {}
for l, r in initials:
	dic[l] = int(r)

# print(lines)

lines = lines.split('\n')
lines = [line.split(' ') for line in lines]

# print(lines)
# print(lines)
ops = [line[1] for line in lines]
lines = [[line[0], line[2], line[4]] for line in lines]
# print(dic)
# print(ops)
# print(lines)

# for i, line in enumerate(lines):
# 	if ops[i] == "AND":
# 		dic[line[2]] = dic[line[0]] & dic[line[1]]
# 	if ops[i] == "XOR":
# 		dic[line[2]] = dic[line[0]] ^ dic[line[1]]
# 	if ops[i] == "OR":
# 		dic[line[2]] = dic[line[0]] | dic[line[1]]

check = set()
for i in range(len(lines)):
	check.add(i)

calculated = set()
i = 0
while lines:
	# print(i)
	line = lines[i]

	if check == calculated:
		break
	if i in calculated:
		i += 1
		i %= len(lines)
		continue
	if line[0] in dic and line[1] in dic:
		calculated.add(i)
		print('yippeee')
		if ops[i] == "AND":
			dic[line[2]] = dic[line[0]] & dic[line[1]]
		if ops[i] == "XOR":
			dic[line[2]] = dic[line[0]] ^ dic[line[1]]
		if ops[i] == "OR":
			dic[line[2]] = dic[line[0]] | dic[line[1]]
	i += 1
	i %= len(lines)

print(dic)

ans = ''
for key in sorted(list(filter(lambda k: k[0] == 'z', dic.keys()))):
	ans += str(dic[key])
ans = ans[::-1]

print(ans)
print(int(ans, 2))	
