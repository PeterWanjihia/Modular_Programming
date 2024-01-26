import random 

locationFile= open('locations.txt', 'r')
town_list = locationFile.readlines()


# The function that generates the  location code and the location 
def genLocations():
    
    
    locations = []
    
    for i in range(1,31):
        location_code = f'location-{i}'
        # select  a random line from  file  containing locations
        description =  random.choice(town_list)
        location_tuple = (location_code,description)
        locations.append(location_tuple)             

    # Remove leading and trailing spaces from the second element of each tuple
    cleaned_locations = [(location[0], location[1].strip()) for location in locations]      

        
    return cleaned_locations

# joe = genLocations()

# print(joe)


