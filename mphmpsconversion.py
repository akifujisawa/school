print("Welcome to the Miles per Hour (MPH) to Meters per Second (MPS) Conversion program\n")

# get mph speed and calculate the mps
mph = input("Speed in MPH: ")
mps = float(mph)*0.4474

# print mps turned into string
print("Your speed in MPS: " + str(round(mps, 2)))