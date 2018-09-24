

# Conditionally infinite
name = ''
while name != 'your name':
    print('Please type your name')
    name = input()
print('Thanks')


# Using a break
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('Thanks')


# Using a continue
while True:
    print('who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe.  What is the password?')
    password = input()
    if password = "goldfish":
        break
print('Access Granted')

# sys.exit
import sys

while True:
    print('Type to exit.')
    response = input()
    if response = 'exit':
        sys.exit()
    print('You typed ' + response)
