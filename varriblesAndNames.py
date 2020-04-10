# Simple python program to demonstrate how variables work in python

# use  to print() output without having parathesis in the outoput
from __future__ import print_function

vehicles = 100
vehicle_operators = 30
space_in_vehicle = 4.0
passengers = 120
vehicles_parked = vehicles - vehicle_operators
vehicles_driven = vehicle_operators
vehicle_capacity = vehicles_driven * space_in_vehicle
average_passengers = passengers / vehicles_driven


# Print out the details

print('There are', vehicles, 'vehicles available')
print("There are", vehicles_parked, "vehicle not available")
print("There are", vehicle_operators, "vehicle operators available")
print("There are", vehicle_capacity, "who can be transported immediately")
print("There follwong passenger require the service:", passengers)
print("There limit per vehicle is on average:", average_passengers)
