
f = open('03-input.txt')

def main():
    valid_triangles = 0
    for line in f:
        sides = line.split()
        sides = [int(x) for x in sides]
        sides.sort()
        if sides[2] < sides[0] + sides[1]:
            valid_triangles += 1
    print valid_triangles

main()
