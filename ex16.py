from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

# open the file for writing -w.
print("Opening the file...")
target = open(filename, 'w')

# truncate the file
print("Truncating the file.  Goodbye!")
target.truncate()

# ask for input
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to a file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# It's more efficient to do it this way.
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# close the file.
print("And finally, we close it.")
target.close()