# how many cars are there?
cars = 100
# how many people fit in each car?
space_in_a_car = 4
# how many drivers are there?
drivers = 30
# how many people need a ride?
passengers = 90
# this is how many extra cars there are due to lack of drivers available
cars_not_driven = cars - drivers
# There can only be as many cars driven as there are drivers available
cars_driven = drivers
# total people able to be moved is number of cars (with drivers) * how many in each car
carpool_capacity = cars_driven * space_in_a_car
# how many people do we need to fit in each car? divide how many cars are available by passengers.
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
