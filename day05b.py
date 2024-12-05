from functools import cmp_to_key
f = open("input.txt", "r")

rules, lines = f.read().split('\n\n')
rules = [list(map(int, rule.split('|'))) for rule in rules.split('\n')]
lines = [list(map(int, line.split(','))) for line in lines.split('\n')]

# item index finding with a dict
line_dicts = [{item : line.index(item) for item in line} for line in lines]

def check_rule(rule, line_dict):
	if rule[0] not in line_dict or rule[1] not in line_dict:
		return True
	return line_dict[rule[0]] < line_dict[rule[1]]

def check_line(line_dict):
	return all(check_rule(rule, line_dict) for rule in rules)

def compare(a, b):
	# no precedence
	if [a, b] not in rules and [b, a] not in rules:
		return 0

	# b should be before a (a,b -> b,a)
	if [b, a] in rules:
		return 1

	# a should be before b (a,b -> a,b)
	return -1


ans = 0
for i in range(len(lines)):
	if not check_line(line_dicts[i]):
		l = lines[i]
		l.sort(key=cmp_to_key(compare))
		ans += l[(len(l)-1)//2]

print(ans)