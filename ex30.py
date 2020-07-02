people = 30
cars = 40
buses = 15

# compare cars and people.
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."
	
# compare buses and cars.
if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

#compare people and buses.
if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."