f = open("input.txt", "r")

rules, lines = f.read().split('\n\n')
rules = [rule.split('|') for rule in rules.split('\n')]
lines = [line.split(',') for line in lines.split('\n')]

# item index finding with a dict
line_dicts = [{item : line.index(item) for item in line} for line in lines]

def check_rule(rule, line_dict):
	if rule[0] not in line_dict or rule[1] not in line_dict:
		return True
	return line_dict[rule[0]] < line_dict[rule[1]]

def check_line(line_dict):
	return all(check_rule(rule, line_dict) for rule in rules)

ans = 0
for i in range(len(lines)):
	ans += int(lines[i][(len(lines[i])-1)//2]) * check_line(line_dicts[i])

print(ans)