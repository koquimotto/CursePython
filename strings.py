myString = "hellow world"

# dir, nos muestra todas las propiedades,métodos y funciones que podemos hacer con un tipo de dato
print(dir(myString))

# declaración de metodos u propiedades
print(myString.upper()) # Cadena de texto a mayúscula

print(myString.lower()) # Cadena de texto a minúscula

print(myString.swapcase()) # Cadena de texto a mayúscula

print(myString.capitalize()) # La primera letra con mayúscula

print(myString.replace('hellow', 'Hola')) # Reemplazar la cadena seleccionada por otra

print(myString.count('o')) # Cuenta la cantidad de caracteres seleccionados

print(myString.startswith('hellow')) # Pregunta si la cadena de texto empieza con la palabra hellow, devuelve True o False 

print(myString.endswith('hellow')) # Pregunta si la cadena de texto termina con la palabra hellow, devuelve True o False 

print(myString.split()) # Divide datos basado en algun caracter, por ejemplo en este caso, en el espacio y devuelve una lista.

print(myString.split(',')) # Divide datos basado en algun caracter, por ejemplo en este caso, en la coma y devuelve una lista.

print(myString.split('o')) # Divide datos basado en algun caracter, por ejemplo en este caso, en la letra o y devuelve una lista.

print(myString.find('o')) # Devuelve la cantidad de caracteres hasta el caracter seleccionado

print(len(myString)) # Devuelve la cantidad de caracteres que contien la variable, empieza en 0

print(myString.index('o')) # Devuelve la posición de la letra seleccionada

print(myString.isnumeric())
print(myString.isalpha())

# Seleccionar el caracter de una posición
print(myString[5])
print(myString[-1]) # El signo negativo ayuda a empezar por el último caracter

osita = "te amo osa rata puc..."
print(osita)

# Concatenar
print("Message of welcome: "+myString)
print(f"Message of welcome: {myString}")
print("Message of welcome: {0}".format(myString))

