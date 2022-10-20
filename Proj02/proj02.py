###########################################################
#  Computer Project #1
#
#  Algorithm
#    Print out the directions for the prompts
#    start the while loop and prompt the customer to continue with the program or end it
#    Promt the customer to enter each required data value
#    Convert the entered data into usable variables
#    Depending on the code entered, use the varaiables to calculate the charge.
#    Print out the customer summary and start the while loop again
###########################################################
import math

BANNER = "\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" 
 
PROMPT = "\nWould you like to continue (A/B)? \n"

conf = 'A'
# set conf to a default value of 'A' so that it can start the while loop 

print(BANNER)
# print banner outside the while loop so that it doesnt keep printing out 
while conf == 'A':
    ans = input(PROMPT)

    while ans != 'A' and ans != 'B':
        print("\n\t*** Invalid customer code. Try again. ***")
        ans = input(PROMPT)

    if ans == 'B':
        print("Thank you for your loyalty.") 
        exit()

    code = input("\nCustomer code (BD, D, W): \n")
    while code != 'BD' and code != 'D' and code != 'W':
        print("\n\t*** Invalid customer code. Try again. ***")
        code = input("\nCustomer code (BD, D, W): \n")
        #made sure the codes are valid
    days = int(input("\nNumber of days: \n"))
    o_start = int(input("Odometer reading at the start: \n"))
    o_end = int(input("Odometer reading at the end:   \n"))
    #converted the integer values from string to int so that they may be used in the program 

    if o_start > o_end:
        m_o_start = 1000000-o_start
        miles_driven = (m_o_start + o_end) / 10
        #found out how close the odomater start value is to reseting thed added that to the end value to get the total miles driven
    else:
        miles_driven = abs(o_start-o_end) / 10

    if code == 'BD':
        charge = (40*days) + (0.25 * miles_driven)
    elif code == 'D':
        avg_mile_day = miles_driven / days
        if avg_mile_day >= 100: 
            charge = (60*days) + (0.25 * ((miles_driven/days)-100))*days
        else:
            charge = 60*days 

    if code == 'W':
        weeks = math.ceil(days/7)
        #used math.ceil to round up the number of weeks to the nearest whole number
        avg_mile_week = miles_driven / weeks
        if avg_mile_week <= 900:
            charge = (190*weeks)
        elif avg_mile_week >= 900 and avg_mile_week <= 1500:
            charge = (190*weeks) + (100*weeks)
        else:
            charge = (190*weeks) + (200*weeks) + (0.25 * (miles_driven - (1500 * weeks)))

    print(
    "\nCustomer summary:\n" + 
    f"\tclassification code: {code}\n" + 
    f"\trental period (days): {days}\n" + 
    f"\todometer reading at start: {o_start}\n" + 
    f"\todometer reading at end:   {o_end}\n" +  
    f"\tnumber of miles driven:  {miles_driven}\n" + 
    f"\tamount due: $ {float(charge)}")