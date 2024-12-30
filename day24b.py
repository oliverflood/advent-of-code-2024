from graphviz import Digraph 

f = open("input.txt", "r")
initials, lines = f.read().split('\n\n')
initials = initials.split('\n')
initials = [initial.split(': ') for initial in initials]

dic = {}
for l, r in initials:
	dic[l] = int(r)

lines = lines.split('\n')
lines = [line.split(' ') for line in lines]
ops = [line[1] for line in lines]
lines = [[line[0], line[2], line[4]] for line in lines]

check = set()
for i in range(len(lines)):
	check.add(i)

calculated = set()
i = 0
while lines:
	line = lines[i]

	if check == calculated:
		break
	if i in calculated:
		i += 1
		i %= len(lines)
		continue
	if line[0] in dic and line[1] in dic:
		calculated.add(i)
		if ops[i] == "AND":
			dic[line[2]] = dic[line[0]] & dic[line[1]]
		if ops[i] == "XOR":
			dic[line[2]] = dic[line[0]] ^ dic[line[1]]
		if ops[i] == "OR":
			dic[line[2]] = dic[line[0]] | dic[line[1]]
	i += 1
	i %= len(lines)


def num(char):
	ans = ''
	for key in sorted(list(filter(lambda k: k[0] == char, dic.keys()))):
		ans += str(dic[key])
	ans = ans[::-1]
	return int(ans, 2)

def graph(format='png', view=False):
	graph_name = 'day24b'
	dot = Digraph(comment="directed graph")
	rights = [line[2] for line in lines]

	for key in dic.keys():
		if key not in rights:
			node_color = 'black'
		else:
			j = rights.index(key)
			if ops[j] == 'AND':
				node_color = 'red'
			if ops[j] == 'OR':
				node_color = 'blue'
			if ops[j] == 'XOR':
				node_color = 'purple'
		dot.node(key, key, color=node_color)

	for line in lines:
		dot.edge(line[0], line[2])
		dot.edge(line[1], line[2])

	dot.save(f'{graph_name}.dot')
	dot.render(graph_name, format=format, view=view)

# graph()

# print('  x', num('x'))
# print('  y', num('y'))
# print('x+y', num('x') + num('y'))
# print('  z', num('z'))

l = ['cnk', 'qwf', 'mps', 'z27', 'z39', 'msq', 'z14', 'vhm']
ans = ''
for item in sorted(l):
	ans += item + ','
print(ans[:-1])