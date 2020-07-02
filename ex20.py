# import argv for use
from sys import argv

# define argument for script
script, input_file = argv

# define functions

# print entire file
def print_all(f):
	print f.read()

# return to bof	
def rewind(f):
	f.seek(0)
	
# print each line of file with line numbers - comma prevents additional newline \n between lines
def print_a_line(line_count, f):
	print line_count, f.readline(),

# set variable as argv passed from calling script	
current_file = open(input_file)

print "First let's print the whole file:\n"

# call print_all function
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# call rewind function
rewind(current_file)

print "Let's print three lines:"

# call print_a_line function and increment line number on subsequent calls.

# current_line is 1
current_line = 1
print_a_line(current_line, current_file)

# increment current_line is now 2
current_line += 1
print_a_line(current_line, current_file)

# increment current_line is now 3
current_line += 1
print_a_line(current_line, current_file)