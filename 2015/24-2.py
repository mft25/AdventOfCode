from operator import mul

f = open('24-input.py')

# Same algorithm as day 17
def get_groupings(total, items):
	groups = []
	options = [([], sorted(items, reverse=True))]
	while len(options) > 0:
		new_options = []
		for pair in options:
			if sum(pair[0]) > total:
				continue
			if sum(pair[0]) == total:
				groups.append(pair[0])
				continue
			for (i, item) in enumerate(pair[1]):
				new_left_list = list(pair[0])
				new_left_list.append(item)
				new_pair = (new_left_list, pair[1][i+1:])
				new_options.append(new_pair)
		options = new_options
	return groups
	
def get_qe(list):
	return reduce(mul, list, 1)

def main():
	presents = [int(line) for line in f]
	total = sum(presents)/4
	groups = get_groupings(total, presents)	
	min_length = len(presents)
	min_qe = get_qe(presents)
	for group in groups:
		remains = [x for x in presents if x not in group]
		new_groups = get_groupings(total, remains)
		if len(group) <= min_length and len(new_groups) > 0:
			qe = get_qe(group)
			if len(group) < min_length:
				min_qe = qe
				min_length = len(group)
			min_qe = min(qe, min_qe)
	print min_qe
	
main()