

"""A fixed-rate mortgage with no points"""
"""A fixed-rate mortgage with points"""
"""A mortgage with an initial teaser rate followed by a higher rate for the
duration"""

def findPayment(loan, r, m):
    """Assumes: loan and r are floats, m an int
    Returns the monthly payment for a mortgage of size
    loan at a monthly rate of r for m months""" 
    return loan*((r*(1+r)**m)/((1+r)**m - 1))

class Mortgage(object):
    """Abstract class for building different kinds of mortgages""" 
    def __init__(self, loan, annRate, months):
        """Create a new mortgage"""
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan, self.rate, months) 
        self.legend = None #description of mortgage


# INPUTS
years_to_payback = 10 

loan = 100000
annRate = .05
months = 12 * years_to_payback
