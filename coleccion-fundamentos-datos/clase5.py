# Comprehesion list python
#la primero que se pone es la formula, lo que queremos aplicar a los elementos
squares = [x**2 for x  in range(1,11)]
print("Cuadrados:", squares)

sum = [2 + 2 for x in range(1, 10)]
print("la suma es de :", sum)

# grados celfius a faregeins

celsius = [0, 10, 20, 30, 40]
faherenheit = [(temp * 9/5) *32 for temp in celsius]
print("temperatura en F:", faherenheit )


#Numeros pares

evens = [x for x in  range(1, 21) if  x%2 ==0]
print(evens)

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

transposed = [[row[i] for row in matrix] for i in range(len(matrix [0]))]

print(matrix)
print(transposed)