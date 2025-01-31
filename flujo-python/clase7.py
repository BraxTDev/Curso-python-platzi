# Funciones Lambda y Programación Funcional en Python
#solo necesita parametros y una funcion para aplicar a ella

add = lambda a, b: a + b              #operacion que quieor que se realize 
print(add(10, 4))

multiply = lambda a, b: a * b
print(multiply(80, 5))

#cuadrado de cada numero

numbers = range(11)

squared_numbers = list(map(lambda x: x**2, numbers))
print("Cuadrados:", squared_numbers )

#obtener numeros pares

even_numbers = list(filter(lambda x: x%2 ==0))
print("Pares:", even_numbers)