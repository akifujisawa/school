# for loops challenge

# iterting over a list
print("iterating over a list\n")
collection = ["M/59 Helmet", "M/72 Surgical Kit", "Strichtarn Jacket", "East German Ushanka", "Type 11 Load-Bearing Rig"]

for x in collection:
    print(x)

# loop through a string
print("\n\nloop through a string\n")
stringloop = "String!"

for x in stringloop:
    print(x)

# stop a loop before it has finished
print("\n\nsttop a loop before it has finished\n")
for x in stringloop:
    if x == "n":
        break
    else:
        print(x)

# using continue statements
print("\n\nusing continue statement\n")
for x in stringloop:
    if x == "n":
        continue
    else:
        print(x)

# loop for a specified amount of time
print("\n\nloop for a specified amount of time\n")
for x in range(6):
    print(x)