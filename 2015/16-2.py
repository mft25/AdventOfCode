import operator

f = open('16-input.py')

properties = {
	"children":[3,operator.eq],
	"cats":[7,operator.gt],
	"samoyeds":[2,operator.eq],
	"pomeranians":[3,operator.lt],
	"akitas":[0,operator.eq],
	"vizslas":[0,operator.eq],
	"goldfish":[5,operator.lt],
	"trees":[3,operator.gt],
	"cars":[2,operator.eq],
	"perfumes":[1,operator.eq]
}

def is_match(parts):
	for i in xrange(0,3):
		comparison = properties[parts[2*i+2].strip(":")]
		if not comparison[1](int(parts[2*i+3].strip(",")), comparison[0]):
			return False
	return True

def main():
	for line in f:
		parts = line.strip().split()
		if is_match(parts):
			print parts[1].strip(":")
		
main()