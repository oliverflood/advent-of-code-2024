import re
f = open("input.txt", "r")
registers, program = f.read().split('\n\n')

prog = program.split(' ')[1] + ','

pattern = r"[-]?\d+"
a, b, c = [int(re.findall(pattern, line)[0]) for line in registers.split('\n')]
program = list(map(int, program.split(' ')[1].split(',')))

# print(a,b,c,program)

# literal operand: 0,1,2, ... 7
# combo operand: 0,3 -> 0,3, 4,5,6 -> a,b,c
# print(len(program))

import math


# need = '10000111010100011100001011110110'
need = ''


################## NOTE: my part 1 is lost to time since I started working on part 2 here
for counter in range(1000000000):
	val = counter*(2**len(need)) #+ int(need, 2)
	a = val
	# print(a)
	out = ''
	c = 0
	i = 0
	while True:
		c += 1
		if c == 1000:
			break
		if not (i < len(program)):
			break
		inst = program[i]
		literal = program[i+1]
		combo = 0
		if literal <= 3:
			combo = literal
		if literal == 4:
			combo = a
		if literal == 5:
			combo = b
		if literal == 6:
			combo = c

		if inst == 0:
			a = math.trunc(a/(2**combo))
		if inst == 1:
			b ^= literal
		if inst == 2:
			b = combo % 8
		if inst == 3:
			if a == 0:
				i += 2
				continue
			i = 2*literal
			i -= 2
		if inst == 4:
			b = b^c
		if inst == 5:
			# print(combo % 8, end=',')
			out += str(combo%8) + ','
		if inst == 6:
			b = math.trunc(a/(2**combo))
		if inst == 7:
			c = math.trunc(a/(2**combo))
		i += 2

	# if counter%1000 == 0:
	# 	print(out, '   ', val, '  ', bin(val))
	if out[:6] == prog[:6]:
		print('ans:', val, '  bin:', bin(val))
