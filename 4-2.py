import hashlib

key = "ckczppom"

def can_mine(val):
	for (j,char) in enumerate(val):
		if j==0 and ord(char) & 0xff:
			return False
		if j==1 and ord(char) & 0xff:
			return False
		if j==2 and ord(char) & 0xff:
			return False
	return True

def main():
	i = 0
	while True:
		i += 1
		m = hashlib.md5()
		m.update(key + str(i))
		val = m.digest()
		if can_mine(val):
			print i
			return

main()