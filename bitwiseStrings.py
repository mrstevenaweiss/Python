
print("\n")
def theBoard(p, q):
    print("\n")
    print(p + " first")
    print(q + " second")
    print("---------")


def AND(a, b):
    if a == '1' and b == '1':
        return '1'
    else:
        return '0'

def XOR(a, b):
    if (a == '1' and b == '0') or (a == '0' and b == '1'):
        return '1'
    else:
        return '0'

def OR(a, b):
    if a == '1' or b == '1':
        return '1'
    else:
        return '0'


def theLogic(foo, bar):
    theOR = []
    theAND = []
    theXOR = []

    for f, q in zip(list(foo), list(bar)):
        theOR.append(OR(f, q))
        theAND.append(AND(f, q))
        theXOR.append(XOR(f, q))

    print(''.join(theOR), " A compliment")
    print(''.join(theAND), " A union B")
    print(''.join(theXOR), " A intersection B")

while True:
    print("-----------------")
    print("Provide two bitwise strings of any length. ie. 00 11 or 1010 01010 - and get the bitwise value back. 'q' to quit, hit 'Enter' to see \n")
    print('Give first string')
    first = input()
    print('Give second string')
    second = input()
    if first == 'q' or second == 'q':
        break
    else:
        theBoard(first, second)
        theLogic(first, second)
        print("\n")
