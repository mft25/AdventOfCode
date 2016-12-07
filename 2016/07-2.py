import re

f = open('07-input.txt')

def supernet_parts(ip):
	return re.split('\[[a-z]*\]', ip)
	
def hypernet_parts(ip):
	return re.findall('\[([a-z]*)\]', ip)
	
def get_abas(parts):
	abas = []
	for part in parts:
		for i in xrange(2, len(part)):
			if part[i-2] == part[i] and part[i-1] != part[i]:
				abas.append(part[i-2:i+1])
	return abas
	
def convert_aba(aba):
	aba = list(aba)
	a = aba[0]
	aba[0] = aba[1]
	aba[2] = aba[1]
	aba[1] = a
	return ''.join(aba)

def main():
	count = 0
	for ip in f:
		ip = ip.strip()
		supernet_abas = set(get_abas(supernet_parts(ip)))
		hypernet_babs = set([convert_aba(aba) for aba in get_abas(hypernet_parts(ip))])
		if len(supernet_abas.intersection(hypernet_babs)) > 0:
			count += 1
	print count

main()
