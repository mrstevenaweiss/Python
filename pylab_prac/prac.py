import pylab


# pylab.figure(1)  #create figure 1 
# pylab.plot([1,2,3,4], [1,7,3,5]) #draw on figure 1 
# pylab.show() #show figure on screen

principal = 10000 #initial investment 
interestRate = 0.05
years = 20
values = []
for i in range(years + 1): 
    values.append(principal)
    principal += principal*interestRate
pylab.plot(values, 'ro')
pylab.title('5% Growth, Compounded Annually') 
pylab.xlabel('Years of Compounding') 
pylab.ylabel('Value of Principal ($)')
pylab.show() #show figure on screen