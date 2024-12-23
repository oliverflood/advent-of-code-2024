f = open("input.txt", "r")
patterns, designs = f.read().split('\n\n')

patterns = patterns.split(', ')
designs = designs.split('\n')

def is_possible(design):
	if design == '':
		return True

	return any(is_possible(design[len(pattern):]) if design.find(pattern) == 0 else False for pattern in patterns)

ans = sum(is_possible(design) for design in designs)
print(ans)