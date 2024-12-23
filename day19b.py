import functools
f = open("input.txt", "r")
patterns, designs = f.read().split('\n\n')

patterns = patterns.split(', ')
designs = designs.split('\n')

@functools.lru_cache(maxsize=None)
def count(design):
	if design == '':
		return 1

	return sum(count(design[len(pattern):]) if design.find(pattern) == 0 else 0 for pattern in patterns)

ans = sum(count(design) for design in designs)
print(ans)