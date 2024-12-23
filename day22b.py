f = open("input.txt", "r")
nums = list(map(int, f.read().split('\n')))

def mix(num, val):
	return num ^ val

def prune(num):
	return num % 16777216

def next(num):
	num = prune(mix(num, num*64))
	num = prune(mix(num, num//32))
	num = prune(mix(num, num*2048))
	return num

def nnext(num, n):
	for _ in range(n):
		num = next(num)
	return num

def ndiffs(num, n):
	arr = []
	prices = []
	for _ in range(n):
		prev = num
		num = next(num)
		prices.append(num%10)
		arr.append((num%10) - (prev % 10))
	return arr, prices

seqdicts = [{} for _ in nums]

# precalculate prices for every sequence for each secret number
for i, num in enumerate(nums):
	print(i)
	nd, prices = ndiffs(num, 2000)
	for j in range(len(nd)-4):
		t = (nd[j], nd[j+1], nd[j+2], nd[j+3])
		seqdicts[i][t] = seqdicts[i][t] if t in seqdicts[i] else prices[j+3]

# get all possible sequences
res = set(seqdicts[0].keys())
for i, s in enumerate([set(seqdict.keys()) for seqdict in seqdicts]):
	print(i)
	res = res.union(s)

ansseq = max(res, key=lambda t: sum(seqdict.get(t, 0) for seqdict in seqdicts))
ans = sum(seqdict.get(ansseq, 0) for seqdict in seqdicts)
print(ans)

# runs a little long (~25 secs) could be improved