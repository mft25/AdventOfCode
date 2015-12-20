import math

def get_divisors(n):
	divisors = set([])
	for i in xrange(1, int(math.ceil(math.sqrt(n)))):
		if n%i == 0:
			divisors.add(i)
			divisors.add(n/i)
	return divisors

def main(input):
	n = 1
	while 10*sum(get_divisors(n)) < input:
		n += 1
	print n

main(29000000)