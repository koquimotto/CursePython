#  def convierte en una función
def hellow():
    print('Hellow World')

# Llamar a una función
hellow()

# Funciones con Parámetros
def hellowName(name):
    print('Hellow '+ name)

hellowName('Luis')

# Valor por defecto si no pasamos parametros a una función
def hellowLast(name = 'Persona'):
    print('Hellow '+ name)
# Llamamos a una función sin el parámetro esperado
hellowLast()

# Retornar valores numéricos
def add(numberOne,numberTwo):
    return numberOne+numberTwo

print(add(10,30))
print(add(80,30))

# Funciones lambda, funciones anonimas, toman un número de argumentos, y se escriben utilizando solo una expresión
add = lambda numberOne,numberTwo: numberOne+numberTwo

print(add(50,50))