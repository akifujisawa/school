# welcome message and ask for fahrenheit
print("Welcome, this program will convert Fahrenheit to Celsius and Kelvin\n")
fahr = float(input("Degrees Fahrenheit:     "))

# calculate celsius and kelvin
cels = round((fahr - 32) * (5/9), 4)
kelv = round(cels + 273.15, 4)

# print results
print("Degrees Celsius:        " + str(cels) + "\nDegrees Kelvin:         " + str(kelv))
