
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
    file = input("Input data to open: ") + ".csv"
    while(True):
        try:
            file = csv.reader(file)
            break
        except:
             print('\nError: file not found. Please try again.')
             file = input('Input a filename: ') + ".csv"
    return file

def make_float(s):
    try:
        return float(s)
    except:
        return -1
  
def get_density(mass, radius):
    mass *=  EARTH_MASS
    radius *= EARTH_RADIUS
    volume = (4/3)*(math.pi)*(radius**3)
    density = mass/volume
    return density

def temp_in_range(axis, star_temp, star_radius, albedo, low_bound, upp_bound):
    star_radius *= SOLAR_RADIUS
    axis *= AU
    planet_temp = star_temp*((star_radius/(2*axis))**0.5)*(1-albedo)**0.25
    return planet_temp >= low_bound and planet_temp <= upp_bound
def get_dist_range():
    while(True):
        dist = input("\nEnter maximum distance from Earth (light years): ")
        try:
            dist = float(dist)
            if dist < 0:
                raise ValueError("\nError: Distance needs to be greater than 0.")
            else:
                break
        except ValueError: 
            print("\nError: Distance needs to be a float.")
    return dist
def max_stars(file):
    max_list = []
    for line in file:
        if(make_float(line[50:57]) != -1):
            max_list.append(float(line[50:57]))
    return max_list  

def max_planets(file):
    max_list = []
    for line in file:
        if(make_float(line[58:65]) != -1):
            max_list.append(float(line[58:65]))
    return max_list

def avg_mass(file):
    avg_list = []
    for line in file:
        if(make_float(line[86:96]) != -1):
            avg_list.append(float(line[86:96]))
    return sum(avg_list)/len(avg_list)

def habitable(file):
    habitable = rocky = temp = mass = radius = 0
    gaseous = []
    for line in file:
        if(make_float(line[97:105]) != -1):
            temp = float(line[97:105])
            if temp_in_range(temp):
                habitable += 1
                if(make_float(line[86:96]) != -1): mass = float(line[86:96])
                if(make_float(line[78:85]) != -1): radius = float(line[78:85])
                density = get_density(mass, radius)
                if((mass >= 0 and mass <= 10 and radius >=0 and radius <= 1.5) or density > 2000):
                    rocky += 1
                else:
                    if(make_float(line[114:]) != -1):
                        gaseous.append(float(line[114:]))


    return habitable,rocky, min(gaseous)

def gaseous():
    pass

def main():
         
    print('''Welcome to program that finds nearby exoplanets '''\
          '''in circumstellar habitable zone.''')
    FILE = open_file()
    dist = get_dist_range() *PARSEC_LY
    low_bound = 200
    upp_bound = 350
    albedo = 0.5

    max_s = max_stars(FILE)
    num_p = max_planets(FILE)
    avg_m = avg_mass(FILE)
    habitable = habitable(FILE, )
    
    
    



if __name__ == "__main__":
    main()