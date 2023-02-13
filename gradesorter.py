print("Welcome to the Grade Sorter App.\n")

# create empty list
grades = []

# ask for first grade and add to list
firstgrade = input("First Grade: ")
grades.append(float(firstgrade))

# ask for second grade and add to list
secondgrade = input("Second Grade: ")
grades.append(float(secondgrade))

# ask for third grade and add to list
thirdgrade = input("Third Grade: ")
grades.append(float(thirdgrade))

# ask for fourth grade and add to list
fourthgrade = input("Fourth Grade: ")
grades.append(float(fourthgrade))

# print all grades
print("\nYour grades are: " + str(grades))

# sort grades from highest to lowest
grades.sort(reverse = True)

# print grades from highest to lowest, print lowest two grades while removing them, print remaining grades, print highest grade
print("Your grades from highest to lowest: " + str(grades) + "\n\nYour two lowest grades are now being removed.\nGrade Removed: " + str(grades.pop(2)) + "\nGrade Removed: " + str(grades.pop(2)) + "\n\nYour remaining grades are: "+ str(grades) + "\nYour highest grade is a " + str(grades[0]) + ", nice work.")
