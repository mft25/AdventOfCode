import operator
import re

f = open('04-input.txt')

def get_valid_sector(room):
    regex = re.compile("(.*)-([0-9]+)\[([a-z]+)\]")
    (name, sector, checksum) = regex.match(room).groups()
    letters = {}
    for letter in re.findall("[a-z]", name):
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    letters = sorted(letters.items(), key=lambda item: item[0])
    letters = sorted(letters, key=lambda item: item[1], reverse=True)
    derived_checksum = ''.join([item[0] for item in letters[:5]])
    return int(sector) if checksum == derived_checksum else 0

def main():
    sum = 0
    for room in f:
        sum += get_valid_sector(room)
    print sum

main()
