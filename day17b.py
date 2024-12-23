import functools

# f = open("input.txt", "r")
# registers, program = f.read().split('\n\n')
# pattern = r"[-]?\d+"
# program = list(map(int, program.split(' ')[1].split(',')))

# based on my puzzle input
needed_out = '2412750347175530'

# based on my puzzle input
def calc_given_a(a):
	b, c = 0, 0
	out = ''
	while a != 0:
		b = a % 8
		b = b ^ 2
		c = a // (2**b)
		a = a // (2**3)
		b = b ^ c
		b = b ^ 7
		out += str(b%8)
	return out


# observation: bit in the ans can only depend on next 10 bits to the left
# brute force based on that:
@functools.lru_cache(maxsize=None)
def recurse(inc, carry):
	for left in range(2**10):
		a = left * (2**(inc*3)) + carry
		out = calc_given_a(a)

		if out[:inc] == needed_out[:inc]:
			if out == needed_out:
				print('possible ans', a)
				return

			carry = a % (2**((inc+1)*3))
			recurse(inc + 1, carry)

recurse(0, 0)