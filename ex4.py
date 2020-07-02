#number of cars
cars = 100

#space in each car for passengers
space_in_a_car = 4

#number of drivers
drivers = 30

#number of passengers
passengers = 90

#cars that won't be driven
cars_not_driven = cars - drivers

#cars that can be driven
cars_driven = drivers

#carpool capacity
carpool_capacity = cars_driven * space_in_a_car

#average passengers per car
average_passengers_per_car = passengers / cars_driven


#print results
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put", average_passengers_per_car, "in each car.")