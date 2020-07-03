from sys import argv
from os.path import exists

#take two arguments, the file you have and the one you want to create.
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# use a semicolon for two commands on the same line
# assign a variable the open file, assign another variable what is read there.
in_file = open(from_file); indata = in_file.read()

# print the length to show off.
print(f"The input file is {len(indata)} bytes long")

# is there already an output file?
# give a chance to abort.
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# open the new file for writing, write the data of the original file.
out_file = open(to_file, 'w')
out_file.write(indata)

# show a progress message.
print("Alright, all done.")

# close both files.
out_file.close()
in_file.close()