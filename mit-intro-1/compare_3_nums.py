
print "let's compare three numbers"

one = int(input("What is your first number: "))
two = int(input("What is your second number: "))
three = int(input("What is your first number: "))
greatest = 0

if one > two:
   greatest = one
else: 
   greatest = two

if greatest > three:
   print('The larger number is ' + greatest)
else: 
   print('The larger number is ' + three)

