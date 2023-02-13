
# essay about yourself
name = "Aki Fujisawa"
age = "14"
middleschool = " MS 443 New Voices"
msgradyear = 2022
highschool = "Staten Island Technical High School"
hsgradyear = 2026
grade = 9
activities = ["Greenbelt", "Chess Club", "Tech Crew"]
gpa = 4.0
hobbies = ["Militaria collecting", "Reading", "Anime"]

# print basic info abt myself
# name, middle school, middle school graduation year, ,grade, high school, and high school graduation year
print(f"Hello, my name is {name}, and I graduated from {middleschool} in {msgradyear}."
      f"\nI am a {grade}th grader currently attending {highschool} and will graduate in {hsgradyear}."
      f"\nMy GPA is currently {gpa}, which is calculated by adding your grades on a 4.0 scale and dividing by the amount of classes."
      f"\n\nFor example, insert 4 grades on a 4.0 scale which will be calculated into a GPA.")

# make list called gpacalculate
gpacalculate = []
while int(len(gpacalculate)) <= 3:
    gpaadd = input("Grade: ")
    if float(gpaadd) > 4:
        print("That's above 4.0, try again.")
    else:
        gpacalculate.append(float(gpaadd))

usergpa = (sum(gpacalculate)/4)
print("\nHere's your GPA: " + str(usergpa))
# add the word "and" before final item
activities.insert(-1, 'and')
hobbies.insert(-1, 'and')

# print list of activities and hobbies, adding commas after every item except for the last two
print(f"\nIn school, I am involved in " + ', '.join(activities[:-1]) + ' ' + ' '.join(activities[-1:]) + "." +
    f"\nAs for hobbies, I am into " + ', '.join(hobbies[:-1]) + ' ' + ' '.join(hobbies[-1:]) + "." +
    "\n3Hope you enjoyed learning something about me!")
