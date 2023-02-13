# introduction to the program + name
print("Letter Counter App - Aki" + "\n")
name = input("What is your name?: ")
print("\n" + "Hello, " + name.capitalize() + "\n \nThis program will count the number of times a letter occurs in a message. \n")

# ask for message + letter to search for
sentence = input("Enter a message: ")
letter = input("What letter would you like to search for?: ")

# print results, if it occurs in message once print "occurs in message once" instead of x times
count = sentence.count(letter.upper()) + sentence.count(letter.lower())
print("\n" + letter + " occurs in the message once." if count == 1 else "\n" + letter + " occurs in the message " + str(count) + " times.")
