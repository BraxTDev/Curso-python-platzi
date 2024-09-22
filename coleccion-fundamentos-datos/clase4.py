#Diccionarios

numbers = {1: "uno", 2:"dos", 3: "tres"}
print(numbers [2])

information = {"nombre": "Carli",
               "Apellido": "Florida",
               "altura": 1.70,
               "edad": 29  }

del information ["edad"]
print(information)
print(information)

#Metodos keys
claves = information.keys()
print(claves)
print(type(claves))
values = information.values() #acceder a los valores
print(values)

#los pares

pairs = information.items() # me separa el tuplas 
print(pairs)


contacts = {"Carli": { "Apellido": "Florida",
                "altura": 1.70,
                "edad": 29  },
                "Sergio": {"Apellido": "Quintero",
                  "altura":  1.70,
                  "edad": 20}
}
#acceder a la llave
#cada producto llevara un costo y producto
print(contacts ["Carli"])



