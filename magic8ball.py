import random

outcomes = [
    'Namean',
    'Fo real?',
    'Yurp',
    'Skuurt',
    'Hope so',
    'I feel that',
    'Try.  Again',
    'Umm ok',
    'Pleaase'
]

def getAnswer(outcome):
    return outcomes[outcome]

while True:
    print("Would you care to read your fortune? 'q' to quit, hit 'Enter' to see \n")
    what = input()
    if what == 'q':
        break
    else:
        r = random.randint(0, 8)
        fortune = getAnswer(r)
        print("Your fortune is", fortune.upper(), "\n")
