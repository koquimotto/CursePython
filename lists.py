demoList = [1,'Hellow', 1.23, True, [1,2,3]]
colors = ['red','green','blue']

# Constructor
numberList = list((2,3,4,5))
print(numberList)

# Rango 
r = list(range(1,200))

print(r)

# Ver métodos lara listas
print(dir(colors))

# Longitud de la lista
print(len(colors))

# Posición
print(colors[1])

# Si un elemento esta en una lista
print('green' in colors)

# Reemplazar un valor de una lista
colors[1] ='yellow'
print(colors)

# Agregar un elemento a una lista
colors.append('violet')
print(colors)

colors.extend(['violet', 'brown'])
print(colors)

colors.insert(1,'black')
print(colors)

# Agrega un elemento en la última parte
colors.insert(-1,'black')
print(colors)

colors.insert(len(colors),'black')
print(colors)

# Eliminar o quitar el último elemento de una lista
colors.pop()
print(colors)

# Eliminar o quitar el elemento seleccionado
colors.remove('red')
print(colors) # Nombre de elemento, tipo

colors.pop(2) # Posición
print(colors)

# Ordenar alfabeticamente 
colors.sort()
print(colors)

# Ordenar alfabeticamente de manera inversa
colors.sort(reverse=True)
print(colors)

# Obtener los indices
print(colors.index('violet'))

# Cuantas veces podemos encontrar un elemento

print(colors.count('violet'))


# Limpiar todos los elementos de una lista
colors.clear()
print(colors)

