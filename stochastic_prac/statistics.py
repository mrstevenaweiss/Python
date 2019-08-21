def stdDev(X):
    """Assumes that X is a list of numbers.
    Returns the standard deviation of X""" 
    mean = float(sum(X))/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5 #Square root of mean difference


def CV(X): # coefficient of variance
    """Standard deviation divided by the mean"""
    mean = sum(X)/float(len(X)) 
    try:
        return stdDev(X)/mean 
    except ZeroDivisionError:
        return float('nan')
