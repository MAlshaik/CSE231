###########################################################
#
#   Computer Project #5
#   Algorithm
#       Define all methods needed    
#       prompt for csv file until it the name entered is valid
#       prompt for maximum distance in light years
#       set variables using the methods defined
#       print results
#############################################################
import math
import csv
#Constants
PI = math.pi   
EARTH_MASS =  5.972E+24    # kg
EARTH_RADIUS = 6.371E+6    # meters
SOLAR_RADIUS = 6.975E+8    # radius of star in meters
AU = 1.496E+11             # distance earth to sun in meters
PARSEC_LY = 3.262
FILE = ''

def open_file():
    """
    The open file method opens the file and returns the reader as well as the file object
    """
    file = input("Input data to open: ") + ".csv"
    #adds .csv to the input
    while(True):
        try:
            data = open(file)
            csvreader = csv.reader(data)
            break
        except:
             print('\nError: file not found.  Please try again.')
             file = input('Enter a file name: ') + ".csv"
             #makes sure the csv file is valid
    return csvreader, data

def make_float(s):
    """
    trys to float a value. If the value cannot be converted into a float it will return -1 otherwise it will return the float
    """
    try:
        return float(s)
    except:
        return -1
  
def get_density(mass, radius):
    """
    given the mass and radius of the planet this method returns the density
    """
    if(mass < 0 or radius < 0):
        return -1
    mass *=  EARTH_MASS
    radius *= EARTH_RADIUS
    #converts units to metric
    volume = (4/3)*(math.pi)*(radius**3)
    try:
        density = mass/volume
        return density
    except:
        return -1

def temp_in_range(axis, star_temp, star_radius, albedo, low_bound, upp_bound):
    """
    Returns true if the temperature of the planet is within the valid range for habitation as we know it.
    """
    star_radius *= SOLAR_RADIUS
    axis *= AU
    #converts to metric units
    planet_temp = star_temp*((star_radius/(2*axis))**0.5)*(1-albedo)**0.25
    #applies the equation to get the planet temperature
    return planet_temp >= low_bound and planet_temp <= upp_bound

def get_dist_range():
    """
    Returns the maximum distance from the user input.
    """
    while(True):
        dist = input("\nEnter maximum distance from Earth (light years): ")
        try:
            dist = float(dist)
            if dist < 0:
                print("\nError: Distance needs to be greater than 0.")
                continue
            else:
                break
        except ValueError: 
            print("\nError: Distance needs to be a float.")
    return dist

    
def max_stars(file, data, range):
    """
    Returns the maximum number of stars  that are within the desired range
    """
    max_list = []
    data.seek(0)
    #starts csv file reader at the start of file 
    for line in file:
        if(make_float(line[9][0:].strip()) != -1):
            #.strip strips the string of white space at the beginning and end of string
            if(float(line[9][0:].strip()) < range):
                if(make_float(line[2][6]) != -1):
                    max_list.append(float(line[2][6]))
    return max(max_list) 

def max_planets(file, data, range):
    """
    Returns the maximum number of planets that are within the desired range
    """
    max_list = []
    data.seek(0)
    for line in file:
        if(make_float(line[9][0:].strip()) != -1):
            if(float(line[9][0:].strip()) < range):
                if(make_float(line[3][6]) != -1):
                    max_list.append(float(line[3][6]))
    return max(max_list)

def avg_mass(file, data, range):
    """
    Returns the average mass of the planets within the desired range.
    """
    data.seek(0)
    avg_list = []
    for line in file:
        if(make_float(line[9][0:].strip()) != -1):
            if(float(line[9][0:].strip()) < range):
                if(make_float(line[6][0:].strip()) != -1):
                    avg_list.append(float(line[6][0:].strip()))
    return sum(avg_list)/len(avg_list)

def get_habitable(file, data, low, up, albedo, range):
    """
    Returns the habitable planets and the number of gaseous and rocky planets as well as the closest gaseous or rocky planets 
    """
    habitable = rocky = 0
    min_gaseous = 99999
    min_rocky = 99999
    data.seek(0)
    gas_name = ''
    rock_name = ''
    
    for line in file:
        if(make_float(line[9][0:].strip()) != -1):
            if(float(line[9][0:].strip()) < range):
            # makes sure the planet is in the desired range
                try:
                    axis = float(line[4][0:].strip())
                    temp = float(line[7][0:].strip())
                    s_radius = float(line[8][0:].strip())
                    #sets the variables required to put into the temp_in_range function. If one of the value is null, then it continues to the next planet
                    try: p_radius = float(line[5][0:].strip()) 
                    except: p_radius = -1
                    try: mass = float(line[6][0:].strip())
                    except: mass = -1
                    #makes sure that the variables dont interfere with the try: except on the outside

                    if temp_in_range(axis, temp, s_radius, albedo, low, up):
                        habitable += 1
                        density = get_density(mass, p_radius)
                        if((mass >= 0 and mass <= 10) or (p_radius >=0 and p_radius <= 1.5) or (density > 2000)):
                            if(make_float(line[9][0:].strip()) != -1):
                                if(float(line[9][0:].strip()) < min_rocky):
                                    #finds min distance to rocky planet
                                    rocky += 1
                                    min_rocky = float(line[9][0:].strip())
                                    rock_name = line[0].strip()
                        else:
                            if(make_float(line[9][0:].strip()) != -1):
                                #finds min distance to gaseous planet
                                if(float(line[9][0:].strip()) < min_gaseous):
                                    min_gaseous = float(line[9][0:].strip())
                                    gas_name = line[0].strip()
                except:
                    continue
            
    return habitable,rocky, min_gaseous*PARSEC_LY, gas_name, min_rocky*PARSEC_LY, rock_name



def main():
    """

    """
    print('''Welcome to program that finds nearby exoplanets '''\
          '''in circumstellar habitable zone.''')

    FILE, data= open_file()
    
    dist = get_dist_range() /PARSEC_LY
    low_bound = 200
    upp_bound = 350
    albedo = 0.5
    
    max_s = max_stars(FILE, data, dist)
    max_p = max_planets(FILE, data, dist)
    avg_m = avg_mass(FILE, data, dist)
    habitable, rocky, min_gaseous, gas_name, min_rock, rock_name = get_habitable(FILE, data, low_bound, upp_bound, albedo, dist)
    
    print(f'\nNumber of stars in systems with the most stars: {int(max_s)}.')
    print(f'Number of planets in systems with the most planets: {int(max_p)}.')
    print(f'Average mass of the planets: {avg_m:.2f} Earth masses.')

    if(habitable > 0):
        print(f'Number of planets in circumstellar habitable zone: {int(habitable)}.')
    if(habitable <= 0):
        print(f'No planet in circumstellar habitable zone.')
    
    if(rocky > 0):
        print(f'Closest rocky planet in the circumstellar habitable zone {rock_name} is {min_rock:.2f} light years away.')
    if(rocky <= 0):
        print(f'No rocky planet in circumstellar habitable zone.')
    
    print(f'Closest gaseous planet in the circumstellar habitable zone {gas_name} is {min_gaseous:.2f} light years away.')
    



if __name__ == "__main__":
    main()