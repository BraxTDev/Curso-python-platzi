#generadores e iteraciones

#Ejemplo iterador

#crear una lista

my_list = [ 1, 2, 3, 4, 5]

#obtener el iterador

my_iter = iter(my_list)

#Usar el iterador
print(next(my_iter)) #podamos ver cuales son los valores que se almacenan en memoria
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#iterar en cadenas
#creando la cadena
text = "Hola mundo"
#creando el iterador
iter_text = iter(text)

#Iterar en la cadena
for char in iter_text:
  print(char)


#crear un iterador para los numeros impares

#Limite

limit = 10

odd_iter = iter(range(1, limit+1,2))

#usar el iterador

for num in odd_iter:
  print(num)


def my_generartor():
  yield 1
  yield 2
  yield 3

for value in my_generartor():
  print(value)



#Fibonacci

# 0 1 1 2 3 5 8 13 21 ....

def fibonacci(limit):
  a , b = 0, 1
  while a < limit:
    yield a 
    a , b = b, a +b
for num in fibonacci(10):
  print(num)