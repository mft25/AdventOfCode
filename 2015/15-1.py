import operator

f = open('15-input.py')

def score(ingredients, options):
	if len(options) != len(ingredients):
		raise ValueError("Values supplied do not map to ingredients supplied")
	totals = [0 for x in ingredients[0]]
	for (i, amount) in enumerate(options):
		totals = [sum(x) for x in zip(totals, [amount*val for val in ingredients[i]])]
	totals = [max(0, val) for val in totals]
	return reduce(operator.mul, totals[:-1], 1)


def main():
	ingredients = []
	for line in f:
		parts = line.split()
		ingredient = [int(parts[2*i+2].strip(",")) for i in xrange(0,5)]
		ingredients.append(ingredient)
	max_score = 0
	for i in xrange(0, 100):
		for j in xrange(0, 100-i):
			for k in xrange(0, 100-i-j):
				max_score = max(score(ingredients, [i, j, k, 100-i-j-k]), max_score)
	print max_score
	
main()