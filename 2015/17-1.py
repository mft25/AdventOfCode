from collections import defaultdict

f = open('17-input.py')

def main(total, containers):
	count = 0
	options = [([], sorted(containers))]
	while len(options) > 0:
		new_options = []
		for pair in options:
			if sum(pair[0]) > total:
				continue
			if sum(pair[0]) == total:
				count += 1
				continue
			for (i, item) in enumerate(pair[1]):
				new_left_list = list(pair[0])
				new_left_list.append(item)
				new_pair = (new_left_list, pair[1][i+1:])
				new_options.append(new_pair)
		options = new_options
	print count

# Description of algorithm:
#
# Assumptions:
#   1) Every container has capacity > 0.
#   2) Containers with the same capacity can be distinguished as 'larger' or 'smaller' (eg. by maintaining an index).
#
# Start with a list of pairs of lists, starting with the pair (empty list, all containers).
# While there are any pairs in the list:
#
# For each pair in the list:
#   1) Pop from the list.
#   2) If the left list sums to 150, add one to the combination count and continue.
#   3) If the left list sums to more than 150, continue.
#   4) Otherwise, for each item in the right list:
#      - Take a copy of the pair.
#      - Move the given item from the right list to the left list.
#      - Add the new pair to the main list.
main(150, [int(line) for line in f])
