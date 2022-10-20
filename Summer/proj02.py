###########################################################

    #  Computer Project #2

    #

    #  Algorithm

    #    prompt for a purchace price (or 'q' for quit)

    #    input purchace price

    #    make sure payment is not negative 

    #    prompt for payment amount in int

    #    input payment in int 

    #    make sure payment is not less than purchace price

    #    Calculate the total change and convert it to cents 

    #    check if change == 0
    
    #    iterate through a while loop that calculates how much of each coin can be used for change 

    #    print the amount of change for each coin if any exists 

    #    reprompt user for purchace and input price (or 'q' for quit)

    ###########################################################

quarters = 10
dimes = 10
nickels = 10
pennies = 10

print("Welcome to change-making program.")

print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))

in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: \n")

while (in_str != 'q'):

    quarterCount = 0
    dimeCount = 0
    nickelCount = 0 
    pennieCount = 0
    # initates a count for the number of each coins that will be used as change
    # made sure to put it at the start of the for loop so that it will reinitalise for each calculation of change

    if(float(in_str) < 0):
    # this if statement checks to see if the price is negative 
        print("Error: purchace price must be non-negative.")
        in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: \n")
        

    payment = int(input("Input dollars paid (int): "))
    if(payment < float(in_str)):
    # this if statement checks to see if the payment is less then the cost of the item 
        print("Error: insufficant payment.\n")
        payment = int(input("Input dollars paid (int): "))

    change = int(100*(payment - float(in_str))) 
    # multiplies the change by 100 and coverts the number to an int rather than a float to avoid any errors 
    if(change == 0):
    # checks to see if payment and price are equal 
        print("No Change.")
    while (change > 0):
    # Iterates through each of the coins starting from the one with the greatest value to the least value
    # and calculates the number of each coin that will be used for the chain
        if(change >= 25 and quarters > 0):
            quarters -= 1
            change -= 25
            quarterCount += 1
        elif(change >= 10 and dimes > 0):
            dimes -= 1
            change -= 10
            dimeCount += 1
        elif(change >= 5 and nickels > 0):
            nickels -= 1
            change -= 5
            nickelCount += 1
        elif(change >= 1 and pennies > 0):
            pennies -= 1
            change -= 1
            pennieCount += 1
        if(change > 0 and pennies == 0):
            print("Error: ran out of coins.")
            break

    print("Collect change below: \n")
    
    #These series of if statements are so that if a certain coin is not used in the destribution of change, it will not be shown when the 
    #count of each coin is printed 

    #Note: There must be a better way to do this but i cant think of anything right now :)
    if(quarterCount > 0 and dimeCount > 0 and nickelCount > 0 and pennieCount > 0):
        print("Quarters: {}\nDimes: {}\nNickles: {}\nPennies {} \n".format(
        quarterCount, dimeCount, nickelCount, pennieCount))
    if(quarterCount == 0):
        print("Dimes: {}\nNickles: {}\nPennies {} \n".format(
         dimeCount, nickelCount, pennieCount))
    if(dimeCount == 0):
         print("Quarters: {}\nNickles: {}\nPennies {} \n".format(
        quarterCount, nickelCount, pennieCount))
    if(nickelCount == 0):
        print("Quarters: {}\nDimes: {}\nPennies {} \n".format(
        quarterCount, dimeCount, pennieCount))
    if(pennieCount == 0):
        print("Quarters: {}\nDimes: {}\nNickles: {}\n".format(
        quarterCount, dimeCount, nickelCount))

    
    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))

    in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: \n")