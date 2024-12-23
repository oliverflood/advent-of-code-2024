f = open("input.txt", "r")
codes = f.read().split('\n')

npos = [3, 2]
dpos = [0, 2]
dpos2 = [0, 2]

# handmade dictionary for optimal directional movements
# there's only 1 or 2 options for each so you can find best ones pretty quick
# an optimal path for one directional keypad must be optimal for all since they always end in A
dic = {'<': {'<': "A", '^': ">^A", '>': ">>A", 'v': ">A", 'A': ">>^A"}, 
		'^': {'<': "v<A", '^': "A", '>': "v>A", 'v': "vA", 'A': ">A"}, 
		'>': {'<': "<<A", '^': "<^A", '>': "A", 'v': "<A", 'A': "^A"}, 
		'v': {'<': "<A", '^': "^A", '>': ">A", 'v': "A", 'A': "^>A"},
		'A': {'<': "v<<A", '^': "<A", '>': "vA", 'v': "<vA", 'A': "A"}}

# goes from one dictionary representation of one directional numpad string to the next highest
def d_d(s): # s is a dict now
	s_dict = {}

	for key, value in s.items():
		l = key[0]
		r = key[1]
		chunk = dic[l][r]
		assert(len(key) == 2)

		# s_dict[cl+cr] = s_dict.get(cl+cr, 0) + mdic[cl][cr]
		for i in range(len(chunk)):
			# cl = chunk[i-1] if i > 0 else 'A'
			cl = 'A' if i == 0 else chunk[i-1]
			cr = chunk[i]
			s_dict[cl+cr] = s_dict.get(cl+cr, 0) + value
	
	return s_dict

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
for i, code in enumerate(codes):
	val = conv_seq(n_d1(code))

	for j in range(25):
		val = d_d(val)

	seqlen = sum(val.values())
	numeric = int(code[:-1])
	ans += seqlen*numeric

print(ans)