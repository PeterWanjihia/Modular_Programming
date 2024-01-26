import random
import json


# The function that  generates the product code, its description and  inventory number
def genProducts():
    
    products = []

    for i in range(1, 101):  # Generate 100 products
        product_code = f'code-{i}'
        description = f'product-{i}'
        inventory_number = random.randint(1, 20)

        product_tuple = (product_code, description, inventory_number)
        products.append(product_tuple)
    
    
    cleaned_locations = [(product[0], product[1].strip()) for product in products]

    

    return cleaned_locations

#Writing output to json file
def write_json_to_file(file_path,json_data):
    with open(file_path,'w') as file:
        json.dump(json_data,file,indent=2)
        
        
def main():
    json_data_to_write = genProducts()
    output_file = 'products.json'
    write_json_to_file(output_file,json_data_to_write)
    
    
if __name__ == '__main__':
    main()
