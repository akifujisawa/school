import datetime
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

# introduction
groceries = ["Meat", "Cheese"]
print("This is the Grocery List App.\nToday's Date and Time: " + day + "/" + month + " " + hour + ":" + minute + "\n\nYou currently have " + groceries[0] + " and " + groceries[1] + " on your list.\n")

# while less than 6 items in list, ask for things to add
while int(len(groceries)) <= 4:
    groceriesadd = input("Type of food to add to the list: ")
    groceries.append(groceriesadd.capitalize())

# print grocery list and print ordered grocery list
print("\nThis is your grocery list: \n" + str(groceries) + "\n\nHere is your grocery list ordered: \n" + str(sorted(groceries)) + "\n\nSimulating grocery shopping...")

# permanently sort groceries
groceries = (sorted(groceries))

# while there are more than two things in the list, ask for items to remove. if it isnt found in the list, ask the user to try again
while int(len(groceries)) >= 3:
    print("\nCurrent grocery list: " + str(len(groceries)) + " items \n" + str(groceries))
    bought = input("What food did you just buy: ")
    print("Removing " + bought + " from the list...")
    if bought.capitalize() in groceries:
        groceries.remove(bought.capitalize())
    else:
        print("Not found in the grocery list, try again.")

# when there are two items left, say last thing in the list is out of stock and ask for a replacement. print the new list with the replacement
print("\nCurrent grocery list: " + str(len(groceries)) + " items \n" + str(groceries) + "\n\nSorry, the store is out of " + str(groceries[1]))
groceries.remove(groceries[1])
groceriesadd = input("What food would you like instead: ")
groceries.append(groceriesadd.capitalize())
print("\nHere is what remains on your grocery list:\n" + str(groceries))