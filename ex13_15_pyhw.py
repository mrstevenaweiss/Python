
#print "-----CONCEPTS-------"
# 1. sys is a library,  argv is a feature/module where you can accept arguments
# 2. read files  

from sys import argv

#script, first, second, third = argv
#fourth = raw_input('Dimelo muchacho!!' )
#print "The script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third
#print "Damelo: ", fourth

#script, user_name = argv
#prompt = '> '

#print "Hi %s, I'm the %s script." % (user_name, script)
#print "I'd like to ask you a few questions."
#print "Do you like me %s?" % user_name
#likes = raw_input(prompt)

#print "Where do you live %s?" % user_name
#lives = raw_input(prompt)

#print "What kind of computer do you have?"
#computer = raw_input(prompt)

#print '''
#Alright, so you said %r about liking me.
#You live in %r.  Not sure where that is.
#And you have %r computer. Nice.
#''' % (likes, lives, computer)

script, filename = argv
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

