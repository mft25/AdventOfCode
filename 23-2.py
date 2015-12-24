
f = open('23-input.py')

def build_actions():
	actions = []
	for line in f:
		parts = line.split()
		action = [parts[0], parts[1].strip(",")]
		if len(parts) == 2:
			action.append(int(parts[1].strip("+")) if parts[0] == "jmp" else 0)
		else:
			action.append(int(parts[2].strip("+")))
		actions.append(action)
	return actions
	

def main():
	actions = build_actions()
	reg = { "a":1, "b":0 }
	i = 0
	while i < len(actions):
		action = actions[i]
		if action[0] == "inc":
			reg[action[1]] += 1
		if action[0] == "hlf":
			reg[action[1]] /= 2
		if action[0] == "tpl":
			reg[action[1]] *= 3
		if action[0] == "jmp":
			i += action[2]
			continue
		if action[0] == "jie" and reg[action[1]]%2 == 0:
			i += action[2]
			continue
		if action[0] == "jio" and reg[action[1]] == 1:
			i += action[2]
			continue		
		i += 1
	print reg

main()