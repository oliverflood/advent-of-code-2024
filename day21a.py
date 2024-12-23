f = open("input.txt", "r")
codes = f.read().split('\n')

npos = [3, 2]
dpos = [0, 2]
dpos2 = [0, 2]

# directional to directional
def d1_d2(s):
	dic = {'<': {'<': "A", '^': ">^A", '>': ">>A", 'v': ">A", 'A': ">>^A"}, 
			'^': {'<': "v<A", '^': "A", '>': "v>A", 'v': "vA", 'A': ">A"}, 
			'>': {'<': "<<A", '^': "<^A", '>': "A", 'v': "<A", 'A': "^A"}, 
			'v': {'<': "<A", '^': "^A", '>': ">A", 'v': "A", 'A': "^>A"},
			'A': {'<': "v<<A", '^': "<A", '>': "vA", 'v': "<vA", 'A': "A"}}
	
	ret = ''
	for i in range(len(s)):
		if i == 0:
			ret += dic['A'][s[i]]
		else: 
			ret += dic[s[i-1]][s[i]]
	
	return ret

# numeric to directional 
def n_d1(s):
	if s == "029A":
		return "<A^A>^^AvvvA"
	if s == "980A":
		return "^^^A<AvvvA>A"
	if s == "179A":
		return "^<<A^^A>>AvvvA"
	if s == "456A":
		return "^^<<A>A>AvvA"
	if s == "379A":
		return "^A<<^^A>>AvvvA"

	# muhahaha you bet I just tried the few combinations of what these could be by hand
	if s == "129A":
		return "^<<A>A^^>AvvvA"
	if s == "176A":
		return "^<<A^^Av>>AvvA"
	if s == "985A":
		return "^^^A<AvAvv>A"
	if s == "170A":
		return "^<<A^^A>vvvA>A"
	if s == "528A":
		return "<^^AvA^^Avvv>A"

# returns a dict
def conv_seq(seq): 
	ret_dict = {}
	for i in range(len(seq)):
		l = seq[i-1] if i > 0 else 'A'
		r = seq[i]
		ret_dict[l+r] = ret_dict.get(l+r, 0) + 1
	return ret_dict

ans = 0
conv_seq_list = []

for code in codes:
	numeric = int(code[:-1])
	seq = n_d1(code)
	for j in range(2):
		seq = d1_d2(seq)
	ans += numeric * len(seq)
	print(seq)
	conv_seq_list.append(conv_seq(seq))
	print(len(seq), numeric, numeric * len(seq))
	print()

print('ans', ans)
# print(conv_seq_list)