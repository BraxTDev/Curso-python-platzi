# Uso del print es lo mas importante mediante que tenemos nuestro codigo

#Print - basico

print("Nunca pares de aprender")

#Uso de la coma en print

print("Nunca", "Pares", "De", "Aprender")

#uso del +

print("Nunca" + "pares" + "de" + "aprender")

# Añadir un espacio explicitamente cuando concatenas cadenas

print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender")

#Uso de sep

print("Nunca", "pares", "de", "aprender", sep=", ") #incluye las comas

#Uso de end

print("Nunca", end=" ") #un salto de linea entre los textos imprimidos
print("pares de aprender")

#impresion de variables

frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author)

# Uso de formato con f-strings

frase = "Nunca pares de aprender"
author = "Platzi"
print(f"Frase: {frase}, Autor: {author}")

#Uso de formato con format

frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase: {}, Autor: {}".format(frase, author))

# Impresión con formato específico

valor = 3.14159
print("Valor: {:.2f}".format(valor))

#9. Saltos de línea y caracteres especiales

print("Hola\nmundo")

#imprimir que tengan comillas

print('Hola soy \'Carli\'')

# algun archivo imprimilo en windows

print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")