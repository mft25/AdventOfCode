
f = open('03-input.txt')

def main():
    valid_triangles = 0
    c0_sides = []
    c1_sides = []
    c2_sides = []
    for line in f:
        sides = [int(x) for x in line.split()]
        c0_sides.append(sides[0])
        c1_sides.append(sides[1])
        c2_sides.append(sides[2])
        if len(c0_sides) == 3:
            c0_sides.sort()
            if c0_sides[2] < c0_sides[0] + c0_sides[1]:
                valid_triangles += 1
            c0_sides = []
        if len(c1_sides) == 3:
            c1_sides.sort()
            if c1_sides[2] < c1_sides[0] + c1_sides[1]:
                valid_triangles += 1
            c1_sides = []
        if len(c2_sides) == 3:
            c2_sides.sort()
            if c2_sides[2] < c2_sides[0] + c2_sides[1]:
                valid_triangles += 1
            c2_sides = []
    print valid_triangles

main()
