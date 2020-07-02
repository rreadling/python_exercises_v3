from sys import argv

#get a filename from argv
script, filename = argv

#open the file entered
txt = open(filename)

#print the filename, then read the file and print it
print "Here's your file %r:" % filename
print txt.read()

#enter the name of the file into a different variable
print "Type the filename again:"
file_again = raw_input("> ")

#open the file as a new variable
txt_again = open(file_again)

#read the file again and print it onscreen
print txt_again.read()

