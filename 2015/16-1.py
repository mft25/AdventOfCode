
f = open('16-input.py')

properties = {
	"children":3,
	"cats":7,
	"samoyeds":2,
	"pomeranians":3,
	"akitas":0,
	"vizslas":0,
	"goldfish":5,
	"trees":3,
	"cars":2,
	"perfumes":1
}

def is_match(parts):
	for i in xrange(0,3):
		if properties[parts[2*i+2].strip(":")] != int(parts[2*i+3].strip(",")):
			return False
	return True

def main():
	for line in f:
		parts = line.strip().split()
		if is_match(parts):
			print parts[1].strip(":")
		
main()