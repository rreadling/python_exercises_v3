def filler(i,j,k):
	numbers = []

	while i < j:
		print"At the top i is %d" % i
		numbers.append(i)
	
		i = i + k
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for i in numbers:
		print i

print "Where to start?"

top = input("> ")

print "Where to stop?"

bottom = input("> ")

print "Step size?"

step = input("> ")

filler(top,bottom,step)
