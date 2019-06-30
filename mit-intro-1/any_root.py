# Finger exercise: Write a program that asks the user to enter an integer and
# prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal
# to the integer entered by the user. If no such pair of integers exists, it should
# print a message to that effect.


#Find the cube root of a perfect cube
x = int(input('Enter an integer: '))

evens  = [2, 4, 6]
odds = [3, 5]

def find_root(x, divisor):
    power = 0

    while abs(x) != 1:
        if x % divisor != 0:
            # print 'divisor', divisor
            return 0
        else:
            x = x // divisor
            power += 1
    return power

root = 0
power = 0

if x % 2 == 1:
    # print odds
    for number in odds:
        ok = find_root(x, number)
        if ok != 0:
            root, power = number, ok


else:
    for number in evens:
        ok = find_root(x, number)
        if ok != 0:
            root, power = number, ok
    # print 'root', root, 'power', power

if power == 0:
    print "there isn't a root/power pair"
else:
    print 'root', root, 'power', power
