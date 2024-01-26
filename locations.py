import random 

locationFile= open('locations.txt', 'r')
town_list = locationFile.readlines()

# for i in town_list:
#     print(i)

def genLocations():
    
    
    locations = []
    
    for i in range(1,31):
        location_code = f'location-{i}'
        # select  a random line from  file  containing locations
        description =  random.choice(town_list)
        location_tuple = (location_code,description)
        locations.append(location_tuple)
        
        
    # locations = [('location-1', 'Kisumu\n'), ('location-2', 'Mombasa\n'), ('location-3', 'Malindi\n'), ('location-4', 'Kakamega\n'), ('location-5', 'Karatina\n'), ('location-6', 'Kerugoya\n'), ('location-7', 'Machakos\n'), ('location-8', 'Nanyuki\n'), ('location-9', 'Voi\n'), ('location-10', 'Homa Bay\n'), ('location-11', 'Oyugis\n'), ('location-12', 'Mumias\n'), ('location-13', 'Bungoma\n'), ('location-14', 'Karatina\n'), ('location-15', 'Wote\n'), ('location-16', 'Kakamega\n'), ('location-17', 'Lamu\n'), ('location-18', 'Kisumu\n'), ('location-19', 'Kisumu\n'), ('location-20', 'Kakamega\n'), ('location-21', 'Voi\n'), ('location-22', 'Mumias\n'), ('location-23', 'Kiambu\n'), ('location-24', 'Ruiru\n'), ('location-25', 'Garissa\n'), ('location-26', 'Embu\n'), ('location-27', 'Nakuru\n'), ('location-28', 'Naivasha\n'), ('location-29', 'Malindi\n')]

        # Remove leading and trailing spaces from the second element of each tuple
    cleaned_locations = [(location[0], location[1].strip()) for location in locations]

        

        
    return cleaned_locations

joe = genLocations()

print(joe)


