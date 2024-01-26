import random
import json

def gen_locations():
    with open('locations.txt', 'r') as location_file:
        town_list = [line.strip() for line in location_file.readlines()]

    locations = []

    for i in range(1, 31):
        location_code = f'location-{i}'
        description = random.choice(town_list)
        location_tuple = (location_code, description)
        locations.append(location_tuple)

    cleaned_locations = [(location[0], location[1].strip()) for location in locations]

    return cleaned_locations

def write_json_to_file(file_path, json_data):
    with open(file_path, 'w') as file:
        json.dump(json_data, file, indent=2)

def main():
    json_data_to_write = gen_locations()
    output_file = 'locations.json'
    write_json_to_file(output_file, json_data_to_write)

if __name__ == "__main__":
    main()
