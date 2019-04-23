from sys import argv
from os.path import exists

print "You need 2 arguments: a file to copy, a file to paste"
print "\n"

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
in_data = in_file.read()

print "The input file is %d bytes long" % len(in_data)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print "All done."

out_file.close()
in_file.close()


