import operator
import re

f = open('04-input.txt')

def decrypt_name(room):
    regex = re.compile("(.*)-([0-9]+).*")
    (name, sector) = regex.match(room).groups()
    decrypted_name = ""
    for char in name:
        if ord(char) > 96 and ord(char) < 123:
            decrypted_name += chr(((ord(char) - 97 + int(sector)) % 26) + 97)
    return decrypted_name

def main():
    for room in f:
        print decrypt_name(room) + " " + room.strip()

main()
