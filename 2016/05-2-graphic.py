# -*- coding: utf-8 -*-
import copy
import hashlib
import random
import sys

key = "abbhdwsy"
placeholders = "#!($%@^&*)"

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
        if i % 50000 == 0:
            display = copy.deepcopy(password)
            for j in xrange(0,len(display)):
                if display[j] == " ":
                    display[j] = placeholders[random.randint(0, len(placeholders) - 1)]
            print display
            sys.stdout.write("\033[F") # Cursor up one line
        m = hashlib.md5()
        m.update(key + str(i))
        val = m.digest()
        after_five_zeros(val, password)
        if " " not in password:
            break
    print ''.join(password)

main()
