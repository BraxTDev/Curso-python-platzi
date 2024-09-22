#Listas 

to_do = ["Digirnos al Hotel", 
          "ir a almorzar", 
          "Visitar un museo",
          "Volver al hotel"]

print(to_do)

number = [1 , 2, 3, 4, 5, "Sex"]
print(type (number))

mix = ["Uno", 2 , 3.14, True, [1,2,3,4]]
print(mix)
print("Primer elemento", mix[0])
print("Segundo elemento", mix[1])
print(type(mix))
print(len(mix))

string = "Hola Mundo"

print("Primer elemento", string[0])
print("Segundo elemento", string[1])
print("Tercer Elemento", string[-1])


# con el 0:2 le indicamos  que incial empezamos y con el otro donde termina
print(mix [0:2])
print(mix)
mix.append(False) #agregamos
print(mix)
mix.insert(1,["a", "b"]) #insertar un dato en la posicion que queremos que quede
print(mix)

#consultar la posicion o aparicion del elemento

print(mix)
print(mix.index(["a", "b"]))


#consultar el elemento mayor y menor

number = [1 , 2, 3, 100, 90, 40 , 20, 40, 200]
print("Mayor", max(number))
print("Menor", min(number))

# eliminar elementos de la lista o la lista entera

del number[0]
print(number)
del number [:2]
print(number)

#eliminar toda la lista
del number
print (number)