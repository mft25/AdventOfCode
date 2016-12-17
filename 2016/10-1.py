import re

file = open('10-input.txt')

def add_or_extend(d, key, val):
	if key not in d:
		d[key] = [val]
	else:
		d[key].append(val)

def read_instructions(file):
	state = {}
	state_regex = re.compile("value ([0-9]+) goes to bot ([0-9]+)")
	actions = {}
	action_regex = re.compile("bot ([0-9]+) gives low to (bot|output) ([0-9]+) and high to (bot|output) ([0-9]+)")
	for instruction in file:
		if state_regex.match(instruction):
			(chip, bot) = state_regex.match(instruction).groups()
			add_or_extend(state, int(bot), int(chip))
		elif action_regex.match(instruction):
			action = action_regex.match(instruction).groups()
			actions[int(action[0])] = {
				"hi": [action[3], int(action[4])],
				"lo": [action[1], int(action[2])]
			}
	return (state, actions)

def find_loaded_bot(state):
	for bot in state:
		if len(state[bot]) > 1:
			return bot
	
def main():
	(state, actions) = read_instructions(file)
	output = {}
	done = False
	while not done:
		bot = find_loaded_bot(state)
		if min(state[bot]) == 17 and max(state[bot]) == 61:
			done = True
		lo_action = actions[bot]["lo"]
		if lo_action[0] == "bot":
			add_or_extend(state, lo_action[1], min(state[bot]))
		else:
			add_or_extend(output, lo_action[1], min(state[bot]))
		hi_action = actions[bot]["hi"]
		if hi_action[0] == "bot":
			add_or_extend(state, hi_action[1], max(state[bot]))
		else:
			add_or_extend(output, hi_action[1], max(state[bot]))
		state[bot] = []
	print bot

main()
