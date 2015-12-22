
f = open('19-input.py')

def main():
	permutations = []
	molecule = ""
	for line in f:
		parts = line.strip().split()
		if len(parts) > 2:
			permutations.append([parts[0], parts[2]])
		if len(parts) == 1:
			molecule = parts[0]
	molecules = set([])
	for i in xrange(len(molecule)):
		for permutation in permutations:
			count = len(permutation[0])
			if molecule[i:i+count] == permutation[0]:
				molecules.add(molecule[:i] + permutation[1] + molecule[i+count:])
	print len(molecules)

main()