from operator import itemgetter


def build_map(in_file1, in_file2):
       
    in_file1.readline()
    in_file2.readline()
    data_map = {}

    for line in in_file1.readlines():

        # Split the line into two words
        continent_list = line.strip().split()
        
        # Convert to Title case, discard whitespace
        continent = continent_list[0].strip().title()
        country = continent_list[1].strip().title()
        
        
        if continent != "":
            if continent not in data_map:
                if country != "":
                    data_map[continent] = {country:''}
            else:
                if country != "":
                    data_map[continent].update({country:''})

            
            # If country is not empty insert (continent is guaranteed to be in map)
            #YOUR CODE
            
                 # If current country not in map, insert it 
    for line in in_file2.readlines():      
    

        # Split the line into two words
        countries_list = line.strip().split()
        
        # Convert to Title case, discard whitespace
        country = countries_list[0].strip().title()
        city = countries_list[1].strip().title()
        
        # Ignore empty strings
        if country != "":
            
            # insert city (country is guaranteed to be in map)
            for continent in data_map:
                try:
                    if data_map[continent][country] == "" and city not in data_map[continent][country]:
                        data_map[continent][country] = [city]
                    else:
                        data_map[continent][country].append(city)
                except:
                    continue
    return data_map

    


def display_map(data_map):

    # Modify this code to display a sorted nested dictionary
    continents_list = []  # sorted list of the continent keys
    # For each continent
    print("{}:".format(continents))  # continents in continents_list
    countries_list = []  # sorted list of the countries keys in the continents
    # For each country
    # countries in countries_list
    print("{:>10s} --> ".format(countries), end='')
    cities = []  # sorted list of the cities
    # For each city
    # As long as not last city, add a comma and a space after the cities names
    print('{}, '.format(city), end='')  # city in cities
    # if it is the last, don't add a comma and a space.
    print('{}'.format(city))  # city in cities


def open_file():

    try:
        filename = input("Enter file name: ")
        print()
        in_file = open(filename, "r")

    except IOError:
        print("\n*** unable to open file ***\n")
        in_file = None

    return in_file


def main():

    # YOUR CODE
    data_map = {}
    in_file1 = open_file()  # Continents with countries file: continents.txt
    in_file2 = open_file()  # Countries with cities file: cities.txt

    if in_file1 != None and in_file2 != None:

        data_map = build_map(in_file1, in_file2)  # data_map is a dictionary
        display_map(data_map)
        in_file1.close()
        in_file2.close()


if __name__ == "__main__":
    main()
