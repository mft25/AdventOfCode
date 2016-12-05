
f = open('02-input.txt')

# Pad with 0 to make arrays 1 based.
U = [0,1,2,3,1,2,3,4,5,6]
D = [0,4,5,6,7,8,9,7,8,9]
L = [0,1,1,2,4,4,5,7,7,8]
R = [0,2,3,3,5,6,6,8,9,9]

def main():
    key = 5
    code = ""
    for line in f:
        for char in line:
            if char == "U":
                key = U[key]
            elif char == "D":
                key = D[key]
            elif char == "L":
                key = L[key]
            elif char == "R":
                key = R[key]
        code = code + str(key)
    print code

main()
