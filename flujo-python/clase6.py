# Uso de funciones en python

def greet(name, lastname="No tiene apellido"):
  print("Hola mundo", name, lastname)


greet("sergio", "Quintero") #llamamos la funcion
greet("diego")
greet(lastname="Quintero", name="Sergio") 


def add (a, b):
    return a + b

def substract(a, b):
    return (a - b)

def multi (a, b):
   return a * b

def division ( a, b):
    return a / b

#funcion principal

def calculator ():
    while True:
        print("Seleccione una operacion")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")


        option = input("ingresa usu opcion (1, 2, 3, 4, 5): ")

        if option == 5:
            print("Saliendo de la calculadora")
            break

        if option in ["1", "2", "3", "4"]:
            num1 = float( input("ingrese el primero numero"))
            num2 = float(input ("ingrese el segundo numero"))

        if option == "1":
            print("La suma es:", add(num1, num2))
        elif option == "2":
            print("La resta es de:", substract(num1, num2))
        elif option == "3":
            print("la multiplicacion es de:", multi(num1, num2))
        elif option == "4":
            print("la division es de:", division(num1, num2))
        else: 
          print("Opcion no valida, intente de nuevo")
            
calculator()