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

def n_next(num, n):
	for _ in range(n):
		num = next(num)
	return num

ans = 0
for num in nums:
	ans += n_next(num, 2000)
print(ans)