from sys import argv
from os.path import exists

#take two arguments, the file you have and the one you want to create.
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# use a semicolon for two commands on the same line
# assign a variable the open file, assign another variable what is read there.
in_file = open(from_file); indata = in_file.read()

# print the length to show off.
print "The input file is %d bytes long" % len(indata)

# is there already an output file?
# give a chance to abort.
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# open the new file for writing, write the data of the original file.
out_file = open(to_file, 'w')
out_file.write(indata)

# show a progress message.
print "Alright, all done."

# close both files.
out_file.close()
in_file.close()