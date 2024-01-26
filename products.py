import random
import json

def genProducts():
    products = []

    for i in range(1, 101):  # Generate 100 products
        product_code = f'code-{i}'
        description = f'product-{i}'
        inventory_number = random.randint(1, 20)

        product_tuple = (product_code, description, inventory_number)
        products.append(product_tuple)

    return products

# Generate products
result = genProducts()

# Convert the result to a JSON-formatted string
json_result = json.dumps(result, indent=2)

# Print the JSON-formatted string
print(json_result)
