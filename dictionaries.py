# Permite almacenar datos y valores a partir de claves y valores

product ={
    'name':'book',
    'quantity':3,
    'price':4.99
}

person = {
    'firstName': 'Luis',
    'LastName':'Paredes'

}

print(person)

print(dir(person))

# Obtener las claves
print(person.keys())

print(person.items())

productos = [
    {'name':'book', 'price':10.99},
    {'name':'laptop', 'price':12323}
]

print(productos)