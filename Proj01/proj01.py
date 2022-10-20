  ###########################################################

    #  Computer Project #1

    #

    #  Algorithm

    #    prompt for a float

    #    input a float

    #    Convert float to diffrent conversions then print

    ###########################################################

from sklearn import metrics


rods = float(input("Input rods: "))
# converted the input to float so that the input will be conversted to a number

print("you input ", rods, " rods.\n")

meter = rods * 5.0292
feet = meter/0.3048
miles = meter/1609.34
furlongs = rods/40
minutes_to_walk_rods = (miles/3.1)*60
#converts miles per hour to miles per minute

print("Conversions")
print("Meters: ", round(meter, 3))
# used round() function to round to 3 decimal places as shown in examples 
print("Feet: ", round(feet, 3))
print("Miles: ", round(miles, 3))
print("Furlongs: ", round(furlongs, 3))
print("Minutes to walk ", rods, " rods: ", round(minutes_to_walk_rods, 3))