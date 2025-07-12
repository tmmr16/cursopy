'''
Ejemplos de listas en Python
'''
array = [1,2,3,4,5,[6,7,8]]

print(array)

print(array[0])
print(array[3])
print(len(array))
array.append("Nuevo elemento") #añadir elmento al final de la lista 
print(array)
array.insert(2,"Nuevo elemento2") #Insertar elemento en posicion especifica
print(array)
array.pop(1) #Eliminar elemento de posicion especifica
print(array)
array.clear() #Limpiar la lista
array.remove

array2 = (45,46)
array3 = array + array2