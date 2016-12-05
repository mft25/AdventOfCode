
f = open('03-input.txt')

def main():
    valid_triangles = 0
    c_sides = [[],[],[]]
    for line in f:
        sides = [int(x) for x in line.split()]
        for (i, side) in enumerate(sides):
            c_sides[i].append(side)
            if len(c_sides[i]) == 3:
                c_sides[i].sort()
                if c_sides[i][2] < c_sides[i][0] + c_sides[i][1]:
                    valid_triangles += 1
                c_sides[i] = []
    print valid_triangles

main()
