import json
#lectura del archivo
with open ( './products.json', mode="r") as file:
    products = json.load(file)

#Mostrar el contenido
for product in products:
    #print(product)
    print(f"product: {product['name']}, price {product['price']}")


#añadir informacion

file_path =  'products.json'

new_product = {
     
    "name": "Jane Smith",
    "rank": "Lieutenant",
    "specialty": "Negotiator",
    "years_of_service": 8
  
}

with open(file_path, mode= 'r') as file:
    products = json.load(file)

products.append(new_product)

with open(file_path, mode=  'w') as file:
    json.dump(product, file, indent=4)