import math

def get_divisors(n):
	divisors = set([])
	for i in xrange(1, int(math.ceil(math.sqrt(n)))):
		if n%i == 0:
			divisors.add(i)
			divisors.add(n/i)
	return divisors

def main(input):
	n = 0
	while True:
		n += 1
		divisors = get_divisors(n)
		divisors = [i for i in divisors if n/i <= 50]
		if 11*sum(divisors) >= input:
			break
	print n

main(29000000)