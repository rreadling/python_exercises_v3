
def filler(i,j,k):
	numbers = []

	while i < j:
		print(f"At the top i is {i}")
		numbers.append(i)
	
		i += k
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")

	print("The numbers: ")

	for i in numbers:
		print(i)

print("Where to start?")

top = int(input("> "))

print("Where to stop?")

bottom = int(input("> "))

print("Step size?")

step = int(input("> "))

filler(top,bottom,step)
