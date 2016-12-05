import hashlib

key = "abbhdwsy"

def after_five_zeros(val, password):
    for (j, char) in enumerate(val):
        if j == 0 and ord(char) & 0xff:
            return
        if j == 1 and ord(char) & 0xff:
            return
        if j == 2 and ord(char) & 0xf0:
            return
        if j == 2:
            pos = ord(char) & 0x0f
        if j == 3 and pos < 8 and password[pos] == " ":
            password[pos] = format((ord(char) & 0xf0) / 0x10, 'x')
            return

def main():
    i = 0
    password = [" " for i in xrange(0,8)]
    while True:
        i += 1
        m = hashlib.md5()
        m.update(key + str(i))
        val = m.digest()
        after_five_zeros(val, password)
        if " " not in password:
            break
    print ''.join(password)

main()
