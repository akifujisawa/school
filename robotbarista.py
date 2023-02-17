# robot barista

price = 0
drinks = ["Coffee", "Juice", "Soda"]
drinkprices = {
      "coffee": 2.25,
      "juice": 1.50,
      "soda": 2.00
}

# ask name and greet, print menu
name = input("What is your name?\n")
print(f"\nThank you for coming in today, {name.capitalize()}.\n"
      f"\nHere is our menu for today:"
      f"\nDrinks: " + str(drinks))

# forever loop, never broken
while True:
      # ask what drink, if drink is not in list then ask again
      order = input("\nWhat would you like?\n")
      if order.capitalize() in drinks:
            # if order is in menu, ask quantity
            quantity = input("\nHow many cups of " + order.lower() + " would you like?\n")
            # calculate price and print rounded to TWO decimal points. ALWAYS shows the decimal points
            price = price + round(float(drinkprices[order.lower()]) * int(quantity), 2)
            print("\nYour order so far is $" + '{0:.2f}'.format(price) + ".\n")
            while True:
                  # ask if they want something else
                  end = input("Would you like to order something else? Yes/No\n")
                  if end.lower() == "no":
                        # if they say no, print total
                        print("\n" + name.capitalize() + ", your total is $" + '{0:.2f}'.format(price) + ".")
                        exit()
                  elif end.lower() == "yes":
                        # if yes, go through order loop again
                        break
                  else:
                        # if neither yes or no, ask again
                        print("\nPlease type either yes or no.")

      else:
            # if not found in menu ask again
            print("\nSorry, that doesn't seem to be on our menu.")
