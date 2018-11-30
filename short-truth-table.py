
print("\n")


def theBoard():
    print("\n")
    print(" P | Q | P v Q | P & Q | P xor Q | P -> Q | P <-> Q ")
    print("---|---|-------|-------|---------|--------|---------")

def theLogic(p, q):
    if p == 'T' and q == 'T':
        print(" T | T |   T   |   T   |    F    |   T    |    T    ")
    elif p == 'T' and q == 'F':
        print(" T | F |   T   |   F   |    T    |   F    |    F    ")
    elif p == 'F' and q == 'T':
        print(" F | T |   T   |   F   |    T    |   T    |    F    ")
    elif p == 'F' and q == 'F':
        print(" F | F |   F   |   F   |    F    |   T    |    T    ")

while True:
    print("-----------------")
    print("Provide two arguments - 'T' or 'F' - and get the compound proposition's truth values. 'q' to quit, hit 'Enter' to see \n")
    print('Give P')
    p = input()
    print('Give Q')
    q = input()
    if p == 'q' or q == 'q':
        break
    else:
        theBoard()
        theLogic(p, q)
        print("\n")
