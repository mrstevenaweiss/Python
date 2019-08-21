import random

def flip(numFlips): 
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1 
    return heads/numFlips

def flipSim(numFlipsPerTrial, numTrials): 
    fracHeads = []
    for i in range(numTrials): 
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads) 
    return mean

print("% about of X that are HEADS:", flipSim(100, 100) )