# Ask for your weight
import math

weight = input("What's your weight? ")

# Ask for measure
unit = input("Select unit: Pounds(L) or Kilograms(K) ")

# Conditional structure
if unit.upper() == "L":
    print(f'You are {math.floor(float(weight)*0.45)} kg')
elif unit.upper() == "K":
    print(f'You are {math.floor(float(weight) / 0.45)} lbs')
else:
    print("No measure selected.")
