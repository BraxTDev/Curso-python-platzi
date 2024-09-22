# Bucles y control de iteraciones

numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:
  print("Aqui i es igual a:", i+1)

for i in range(2 ,10):
  print(i)


fruits = ["Manzana", "Pera", "Papaya", "Banana", "uvas"]

for fruit in fruits:
  print(fruits)
  if fruits== "Naranja":
    print("Naranja encontrada")

#While - mientras
x = 0

while x < 5: #tomar en cuenta que debemos modificar al condicional para que se detenga esta ejecucion
  if x == 3:
    break 
  print(x)
  x +=1

numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:
    if i ==3:
        continue
    print("Aqui i es igual a:", i)