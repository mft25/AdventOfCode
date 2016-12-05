
f = open('02-input.txt')

# Pad with 0 to make arrays 1 based.
U = [0,1,2,1,4,5,2,3,4,9,6,7,8,11]
D = [0,3,6,7,8,5,10,11,12,9,10,13,12,13]
L = [0,1,2,2,3,5,5,6,7,8,10,10,11,13]
R = [0,1,3,4,4,6,7,8,9,9,11,12,12,13]
K = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D"]

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
        code = code + str(K[key])
    print code

main()
