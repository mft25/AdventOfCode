import re

f = open('07-input.txt')

def supernet_parts(ip):
	return re.split('\[[a-z]*\]', ip)
	
def hypernet_parts(ip):
	return re.findall('\[([a-z]*)\]', ip)
	
def has_abba(parts):
	for part in parts:
		for i in xrange(3, len(part)):
			if part[i-3] == part[i] and part[i-2] == part[i-1] and part[i-1] != part[i]:
				return True
	return False

def main():
	count = 0
	for ip in f:
		ip = ip.strip()
		if has_abba(supernet_parts(ip)) and not has_abba(hypernet_parts(ip)):
			count += 1
	print count

main()
