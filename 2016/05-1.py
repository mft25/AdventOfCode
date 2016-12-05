import hashlib

key = "abbhdwsy"

def after_five_zeros(val):
    for (j, char) in enumerate(val):
        if j == 0 and ord(char) & 0xff:
            return -1
        if j == 1 and ord(char) & 0xff:
            return -1
        if j == 2 and ord(char) & 0xf0:
            return -1
        if j == 2:
            return ord(char) & 0x0f

def main():
    i = 0
    password = ""
    while True:
        i += 1
        m = hashlib.md5()
        m.update(key + str(i))
        val = m.digest()
        sixth = after_five_zeros(val)
        if sixth >= 0:
            password += format(sixth, 'x')
            if len(password) >= 8:
                break
    print password

main()
