
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
	molecules = set([molecule])
	#molecules = set(["OBCaF"])
	n = 0
	while not "e" in molecules:
		n += 1
		print len(molecules)
		print n
		new_molecules = set([])
		for molecule in molecules:
			for i in xrange(len(molecule)):
				for permutation in permutations:
					count = len(permutation[1])
					if molecule[i:i+count] == permutation[1]:
						new_molecules.add(molecule[:i] + permutation[0] + 
molecule[i+count:])
		molecules = new_molecules
	print n		

main()
